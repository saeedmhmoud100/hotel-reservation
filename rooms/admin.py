from django.contrib import admin
from .models import Room,Room_image,Room_Rating,Room_Reservation,Place
from .db.model import Active_Room
# Register your models here.



class Room_imageAdmin(admin.TabularInline):
    model = Room_image
    max_num = 4
    readonly_fields = ('image_preview',)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [Room_imageAdmin]
    list_display = ('title','img_tag','city', 'locality', 'days_number', 'update_at','total_rating' )
    readonly_fields = ['created_at']
    search_fields = ('title','descriptions')
    class Meta:
        model = Room
        fields = '__all__'


# @admin.register(Room_image)
# class Room_imageAdmin(admin.ModelAdmin):
#     list_display = ('room','img_tag')
#     class Meta:
#         model = Room_image
#         fields = '__all__'


class Active_RoomAdmin(admin.ModelAdmin):
    list_display = ('title','city','locality', 'update_at','total_rating','active')
    list_editable = ('active',)
    inlines = [Room_imageAdmin]
    def get_queryset(self, request):
        return self.model.objects.active()
    class Meta:
        model = Active_Room


admin.site.register(Active_Room,Active_RoomAdmin)


class Room_RatingAdmin(admin.ModelAdmin):
    list_display = ('room','user','rating')
    search_fields = ('room__title','room__descriptions','user__username')
    class Meta:
        model = Room_Rating

admin.site.register(Room_Rating,Room_RatingAdmin)



class Room_ReservationAdmin(admin.ModelAdmin):
    list_display  = ('pk','room','user','email_registered','price','canceled','done')
    list_editable = ('canceled','done')
    list_filter = ('canceled','done')
    search_fields = ('room__title','room__descriptions','user__username','price')
    class Meta:
        model = Room_Reservation
        fields = '__all__'

admin.site.register(Room_Reservation,Room_ReservationAdmin)

