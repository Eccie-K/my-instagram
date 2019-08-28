from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Image, Profile
from django.contrib.auth.decorators import login_required
from .forms import  ImageForm, SignupForm, ProfileForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site






# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()

            return render(request, 'success.html')

    else:
        form = SignupForm()
    return render(request, 'signup.html', {"form":form})


            
@login_required(login_url='/accounts/login')
def index(request):
    form = ImageForm()
    image = Image.objects.all()
    
    return render(request,'index.html', {"image":image})


def upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('index')

    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})


def profile(request):
    images = Image.objects.all()
    current_user = request.user
    profile = Profile.objects.filter(user=current_user)
    posts = Image.objects.filter(user=current_user)
    image_form = ProfileForm()
    if request.method == 'POST':
        image_form = ProfileForm(
            request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            image_form.save()
        else:
            image_form = ProfileForm()

    return render(request, 'profile.html', {"image_form": image_form, "posts": posts, "profile": profile, "images": images})

def update_profile(request):
    # current_user = request.user
    if request.method == 'POST':
        me = User.objects.get(username=request.user)
        user = Profile.objects.get(user=request.user)
        print(user)
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'update_profile.html', {"form": form})



    
