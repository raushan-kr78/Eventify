from django.urls import path
from .import views
urlpatterns = [
    path('',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('event/',views.event,name='event'),
    path('register/<int:event_id>/', views.register_event, name='register_event'),
    path('adminDashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('organizerDashboard/',views.organizer_dashboard,name='organizer_dashboard'),
    path('organizer/',views.event_organize,name='organizer'),
    path('profile/',views.profile,name='profile'),
    path('upload-profile-image/', views.upload_profile_image, name='upload_profile_image'),
    # path('upload-event-image/', views.upload_event_image, name='upload_event_image'),

]