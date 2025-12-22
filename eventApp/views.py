from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseForbidden
from .models import*
from django.http import JsonResponse
# Create your views here.


@login_required
def event(request):
    events = Event.objects.all().order_by('-id')
    return render(request, 'index.html', {'events': events})


@login_required
def register_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.user.is_organizer:
        return HttpResponseForbidden("Organizers cannot register for events.")

    Register.objects.create(user=request.user, event_name=event)
    return redirect('event')


@login_required
def organizer_dashboard(request):
    if not request.user.is_organizer:
        return HttpResponseForbidden("You do not have access to this page.")

    organized_events = Event.objects.filter(organizer=request.user).order_by('-id')
    register_event = Register.objects.filter(event_name__organizer=request.user).order_by('-id')
    # print(register_event)
    return render(request, 'organizer_dashboard.html', {'organized_events': organized_events,'register_event':register_event})

@login_required
def event_organize(request):
    if not request.user.is_organizer:
        return HttpResponseForbidden("you do not have accesss to this page.")
    
    if request.method == 'POST' and request.FILES.get('event_image'):
        event_title = request.POST.get('event_title')
        event_date = request.POST.get('event_date')
        event_location = request.POST.get('event_location')
        event_description = request.POST.get('event_description')
        organizer = request.user

        Event.objects.create(
            title = event_title,
            date = event_date,
            location = event_location,
            description = event_description,
            organizer = organizer,
            event_image = request.FILES['event_image']
        )
        return redirect('event')
    return render(request, 'organizer.html')


# User Profile Image Upload
@login_required
def upload_profile_image(request):
    if request.method == 'POST' and request.FILES.get('profile_images'):
        user = request.user
        user.profile_image = request.FILES['profile_images']
        user.save()
        return redirect('profile')




       

@login_required
def admin_dashboard(request):
    if not request.user.is_admin:
        return HttpResponseForbidden("You do not have access to this page.")

    all_registrations = Register.objects.all()
    return render(request, 'admin_dashboard.html', {'all_registrations': all_registrations})


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        is_organizer = False
        # is_organizer = request.POST.get('is_organizer') == 'on'
        if password[:3]=="coc":
            is_organizer = True

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_organizer=is_organizer,
        )
        user.save()
        login(request, user)
        return redirect('event')

    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('event')
        else:
            return render(request, 'signin.html', {'error': 'Invalid username or password'})

    return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect('signin')


def profile(request):
    if  request.user.is_organizer:
        return redirect('organizer_dashboard')
    else :
        register_event = Register.objects.filter(user=request.user).order_by('-id')
        return render(request, 'profile.html', {'user':request.user,'register_event':register_event})