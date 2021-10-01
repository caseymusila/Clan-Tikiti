from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .forms import CreateUserForm , EventForm
import datetime as dt
from .models import Event
from django.http import HttpResponseRedirect


# Create your views here.
# login
def loginPage(request):
	
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

# Register
def registerPage(request):
  form = CreateUserForm()

  if request.method =='POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      user = form.cleaned_data.get('username')
      messages.success(request,'Account was created for ' + user)
      return redirect('login')



  context = {'form': form}
  return render(request, 'accounts/registration.html',context)


# displaying all events
@login_required(login_url="login")
def home(request):
  title="Clan Tikiti"
  date=dt.date.today()
  events =Event.display_all_events()
  return render(request, 'home.html', {"date":date, "title":title, "events":events})

# create an event
@login_required(login_url="login/")
def create_event(request):
  title="Create Event"
  current_user = request.user
  if request.method == "POST":
    form = EventForm(request.POST, request.FILES)
    if form.is_valid():
      event = form.save(commit=False)
      event.user = current_user
      event.save()

    return HttpResponseRedirect("/")

  else:
    form = EventForm()
  return render(request, "event.html", {"form": form,"title": title})

# displaying single event
@login_required(login_url="login/")
def disp_event(request,event_id):
    event=Event.objects.get(pk=event_id)
    title=event.name.title()
    return render(request, 'dispevents.html', {"title":title, "event":event })