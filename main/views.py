from random import shuffle
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models.query_utils import Q
from django.db.models.aggregates import Count
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required   
from rooms.models import Room
from itertools import chain
from tours.models import Tour
from blog.models import Post
from about.models import About
from .models import Home_Cart, Newsletter_Email, Place,Category
# Create your views here.

class HomeView(TemplateView):
    template_name = 'main/home.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['places'] = Place.objects.all().annotate(rooms=Count('room'),tours=Count('tour'))
        context['Categorys']=Category.objects.all()
        context['Home_Carts']=Home_Cart.objects.all()[:4]
        context['top_tours']=Tour.objects.all().order_by('tour_Reservation')[:5]
        context['popular_rooms'] = Room.objects.order_by('total_rating')[:5]
        res = list(chain(Room.objects.filter(category__name='Restaurant'),Tour.objects.filter(category__name='Restaurant')));shuffle(res)
        context['popular_restaurants']= res[:4]
        posts =Post.objects.all().order_by('-id')[:20];shuffle(list(posts))
        context['recent_blog']=posts[:4]
        context['users_count'] = get_user_model().objects.all().count()
        context['places_count']=Place.objects.all().count()
        context['hotels_count']=Room.objects.all().count()
        context['restaurants_count']=Room.objects.all().count() + Tour.objects.all().count() 
        context["about"] = About.objects.last()
        return context
    
def places_search(request):
    name = request.GET.get('name','')
    place = request.GET.get('place','')
    rooms=Room.objects.filter(
        Q(city__name__icontains=place) &
        Q(title__icontains=name) |
        Q(descriptions__icontains=name)
    )
    tours=Tour.objects.filter(
        Q(city__name__icontains=place) &
        Q(title__icontains=name) |
        Q(descriptions__icontains=name)
    )
    res = list(chain(rooms,tours))
    shuffle(res)
    return render(request,'main/search.html',{'response':res})

def category_filter(request,category):
    rooms=Room.objects.filter(category__name=category)
    tours=Tour.objects.filter(category__name=category)
    res = list(chain(rooms,tours))
    shuffle(res)
    return render(request,'main/search.html',{'response':res})

def place_filter(request,place):
    rooms=Room.objects.filter(city__name=place)
    tours=Tour.objects.filter(city__name=place)
    res = list(chain(rooms,tours))
    shuffle(res)
    return render(request,'main/search.html',{'response':res})
@login_required
def news_letter_Subcriber(request):
    email = request.POST.get('email',None)
    Newsletter_Email.objects.create(email=email) if email else JsonResponse({'done':'no'})
    return JsonResponse({'done':'success'})