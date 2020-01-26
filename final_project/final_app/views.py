from django.shortcuts import render
from .forms import UserForm,UserProfile

# login
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        user_profile = UserProfile(data = request.POST)

        if user_form.is_valid and user_profile.is_valid:
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = user_profile.save(commit = False)
            profile.user = user

            if 'profile_pics' in request.FILES:
                profile.profile_pics = request.FILES['profile_pics']
                profile.save()

                registered = True

        else:
            print(user_form.errors,user_profile.errors)

    else:
        user_form = UserForm
        user_profile = UserProfile

    return render(request,'register.html',{ "user_form":user_form, "user_profile":user_profile,"registered":registered })



def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:

            if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))

            else:
                print('User not active')


        else:
             print('invalid login detail')

    else:
        return render(request,'login.html')
