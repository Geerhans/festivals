from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
from django.http import HttpResponse 
def index(request):
    context_dict = {}
    #return HttpResponse("Welcome to shareFestival!")
    response = render(request, 'festival/index.html', context=context_dict)
    return response

def festivalHistory(request):
    return render(request, 'festival/festivalHistory.html')

def shareStory(request):
    return render(request, 'festival/shareStory.html')

def personalCenter(request):
    return render(request, 'festival/personalCenter.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:

                login(request, user)
                return redirect(reverse('festival:index'))
            else:
                return HttpResponse("Your shareStory account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'festival/Login.html')

def user_logout(request):
    logout(request)
    return redirect(reverse('festival:index'))

def signUp(request):
    return render(request, 'festival/signUp.html')

def about(request):
    return render(request, 'festival/about.html')

def contactUs(request):
    return render(request, 'festival/contactUs')
