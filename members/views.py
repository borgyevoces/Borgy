from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, UserUpdateForm, ProfileUpdateForm
from webapp.models import Profile
from django.contrib.auth.decorators import login_required



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.success(request,("There was an error logging in, try again"))
            return redirect('login')      
    else:
     return render(request, 'authenticate/login.html')

     return render(request, 'authenticate/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,("Successfully logged Out!"))
    return redirect('/home')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful"))
            return redirect('/home')
            
    
    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/register_user.html',{'form':form,})

def user_profile(request):
    return render(request, 'authenticate/profile.html')



def user_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)


        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account Has Been Updated')
            return redirect('profile')
       
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form': u_form,
        'p_form': p_form,
        
    }
    return render(request, 'authenticate/profile.html', context)


  
def delete_profile_image(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)

        if profile.user.profile_picture:
            profile.user.profile_picture.delete(save=True)

        profile.user.profile_picture = None
        profile.save()
        messages.success(request, 'Profile image deleted successfully.')
    else:
        messages.warning(request, 'No profile image to delete.')
    

    return redirect('profile')


@login_required
def delete_email(request):
    user = request.user

    if request.method == 'POST':
        user.email = ''
        user.save()
        messages.success(request, 'Email deleted successfully.')
        return redirect('profile') 

    return render(request, 'delete_email.html', {'user': user})

def delete_contact(request):
    user_profile = request.user.profile 

    if request.method == 'POST':
       
        user_profile.contact = None
        user_profile.save()
        messages.success(request, 'Contact information deleted successfully.')
        return redirect('profile') 

    return render(request, 'profile.html', {'user_profile': user_profile})