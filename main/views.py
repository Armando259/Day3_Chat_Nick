from django.shortcuts import render
from django.views import View
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .form import *
from django.contrib.sites.shortcuts import get_current_site

from django.views.generic import ListView, DeleteView , TemplateView, UpdateView, CreateView, DetailView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

from django.http import HttpResponse, HttpResponseNotFound

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from .form import RegisterUserForm
from .models import Korisnik
from django.http import HttpResponse
## Create your views here.

def LandingPageView(request):
    return render(request, 'landing.html')
def not_found(request):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def login_user (request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:landing')
        else:
            messages.success(request, ("Krivi unos! Pokusajte ponovo..."))	
            return redirect('main:login')
    else:
        return render(request, 'registration/login.html', {})
    

def logout_user (request):
    logout(request)
    return redirect('main:landing')

class profile (ListView):
    model = Korisnik
    template_name = 'profile.html'


def register(request):
    if request.method == 'POST':
        form1 = KorisnikForm(request.POST)
        form = RegisterUserForm(request.POST)

        if form.is_valid() and form1.is_valid():
            user = form.save(commit=False)
            user.save()
            korisnik = form1.save(commit=False)
            korisnik.user = user
            korisnik.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main:landing')

    else:
        form1 = KorisnikForm()
        form = RegisterUserForm()

    context = {'form': form, 'form1': form1}

    return render(request, 'registration/register.html', context)


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_user(request):
    logout(request)
    return redirect('main:landing')  # Zamijenite 'landing' s URL-om vaše početne stranice



def add_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            return redirect('main:landing')  # Promijenite na URL imena za listu događaja
        else:
            print(event_form.errors)  # Ispisivanje grešaka forme
    else:
        event_form = EventForm()
    return render(request, 'add_event.html', {'event_form': event_form})       

from django.shortcuts import render, redirect
from .models import Event
from django.shortcuts import render
from django.views import View
from .models import Event

class SearchResultsView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        results = Event.objects.filter(name__icontains=query)
        return render(request, 'search_results.html', {'results': results, 'query': query})

def pretrazi_eventove(request):
    query = request.GET.get('q', '')
    events = Event.objects.filter(name__icontains=query)
    return render(request, 'pretraga_eventova.html', {'query': query, 'events': events})


def add_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            return redirect('event_list')
        else:
            print(event_form.errors)
    else:
        event_form = EventForm()
    return render(request, 'add_event.html', {'event_form': event_form})

def event_list(request):
    events = Event.objects.all()  # Dohvaća sve događaje iz baze podataka
    return render(request, 'event_list.html', {'events': events})


def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event_form = EventForm(request.POST, instance=event)
        if event_form.is_valid():
            event_form.save()
            return redirect('main:event_list')
    else:
        event_form = EventForm(instance=event)
    return render(request, 'edit_event.html', {'event_form': event_form})





from django.shortcuts import render, redirect, get_object_or_404
from .models import Event

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event_form = EventForm(request.POST, instance=event)
        if event_form.is_valid():
            event_form.save()
            return redirect('main:event_list')
    else:
        event_form = EventForm(instance=event)
    return render(request, 'edit_event.html', {'event_form': event_form})

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('main:event_list')
    return render(request, 'confirm_delete.html', {'event': event})
