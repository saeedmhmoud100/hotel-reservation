from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.generic import ListView,DeleteView
from django.views.generic.edit import FormMixin
from django_filters.views import FilterView
from django.contrib import messages
from random import *
from .models import Room,Room_Rating
from .forms import RoomReservationForm
# Create your views here.




def random_rooms(rooms,num=None):
    try:
        x =[p for p in rooms.objects.all()]
    except AttributeError:
        x = rooms   
    if num:
        return list(x[:num])
    return list(x)



def home(request):
    return render(request,'room/home.html')

class HotelListView(FilterView):
    template_name = 'room/hotel.html'
    model = Room
    paginate_by = 2
    filterset_fields = ['country', 'locality','data_from','data_to','total_rating']
    
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class HotelRoomView(DeleteView,FormMixin):
    template_name = 'room/hotel_room.html'
    model = Room
    form_class = RoomReservationForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_and_room"] = [self.request.user,self.get_object().pk]
        context["our_rooms"] = random_rooms(Room.objects.all().order_by('?'),3)
        context['related_rooms'] = random_rooms(Room.objects.all().order_by('total_rating'),3)
        return context
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        my_form = form.save(commit=False)
        my_form.user = self.request.user
        my_form.room = self.get_object()
        my_form.email_registered = self.request.user.email
        my_form.price = self.get_object().price
        my_form.save()
        print('yes')
        messages.success(self.request,'Yor are booking successfully!!')
        return super(HotelRoomView, self).form_valid(form)
    
    def form_invalid(self, form):
        print(form.data)
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('rooms:hotel_room', kwargs={'pk': self.get_object().pk,'slug':self.get_object().slug})
    
def room_rate(request):
    room = request.GET.get('room_id')
    rating = request.GET.get('rating')
    rooms = Room_Rating.objects.filter(room__id=room,user=request.user)
    if rooms.exists():
        message= 'you are alraly rating!!'
        tag = 'warning'
    else:
        Room_Rating.objects.create(rating=rating,user=request.user,room=Room.objects.get(id=room)).save()
        message = 'thanks for your rating'
        tag = 'success'
    return JsonResponse({'message':message,'tag':tag})

def tour(request):
    return render(request,'room/tour.html')

def tour_single(request):
    return render(request,'room/tour.html')
