from django.contrib import admin
from .models import*
# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'organizer')


@admin.register(Register)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event_name', 'register_date')




@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_organizer')