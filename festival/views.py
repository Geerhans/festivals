from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
from django.http import HttpResponse 
def index(request):
 # 1. Query the database for a list of ALL countries currently stored.
 # 2. Order the countries by the number of views in ascending order.
    #country_list = Country.objects.order_by('views')[:5]
    context_dict = {}
    #context_dict['countries'] = country_list

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
    return render(request, 'festival/contactUs.html')

def India(request):
    return render(request, 'festival/india.html')

def UK(request):
    return render(request, 'festival/UK.html')

def USA(request):
    return render(request, 'festival/USA.html')

def Italy(request):
    return render(request, 'festival/italy.html')

def China(request):
    return render(request, 'festival/china.html')