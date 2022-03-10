from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse
from festival.models import Country, Festival, Story, Comment
from datetime import datetime


# Create your views here.
from django.http import HttpResponse 
def index(request):
 # 1. Query the database for a list of ALL countries currently stored.
 # 2. Filter the popular festival by the number of views in ascending order.
    popular_festival = Festival.objects.order_by('views')[:3]
    country_list = Country.objects.all()

    context_dict = {}
    context_dict['popular_festival'] = popular_festival
    context_dict['countries'] = country_list

    visitor_cookie_handler(request)

    response = render(request, 'festival/index.html', context=context_dict)
    return response

def festivalHistory(request):
    festival_history = Festival.objects.all()

    context_dict = {}
    context_dict['festivalHistory'] = festival_history
    context_dict['visits'] = request.session['visits']

    visitor_cookie_handler(request)
    
    return render(request, 'festival/festivalHistory.html', context=context_dict)

def shareStory(request):
    story = Story.objects.all()
    comment = Comment.objects.all()

    context_dict = {}
    context_dict['stories'] = story
    context_dict['comments'] = comment
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
            print("Invalid login details: {username}, {password}")
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
    #list of festivals by a particular country
    festival_list = Festival.objects.filter(festival__countryname='India')

    context_dict = {}
    context_dict['festivals'] = festival_list
    context_dict['visits'] = request.session['visits']
    
    visitor_cookie_handler(request)

    return render(request, 'festival/country/india.html', context=context_dict)

def UK(request):
    festival_list = Festival.objects.filter(festival__countryname='UK')

    context_dict = {}
    context_dict['festivals'] = festival_list
    context_dict['visits'] = request.session['visits']

    visitor_cookie_handler(request)

    return render(request, 'festival/country/UK.html', context=context_dict)

def USA(request):
    festival_list = Festival.objects.filter(festival__countryname='USA')

    context_dict = {}
    context_dict['festivals'] = festival_list
    context_dict['visits'] = request.session['visits']

    visitor_cookie_handler(request)

    return render(request, 'festival/country/USA.html', context=context_dict)

def Italy(request):
    festival_list = Festival.objects.filter(festival__countryname='Italy')
    
    context_dict = {}
    context_dict['festivals'] = festival_list
    context_dict['visits'] = request.session['visits']

    visitor_cookie_handler(request)

    return render(request, 'festival/country/italy.html', context=context_dict)

def China(request):
    festival_list = Festival.objects.filter(festival__countryname='China')
    
    context_dict = {}
    context_dict['festivals'] = festival_list
    context_dict['visits'] = request.session['visits']

    visitor_cookie_handler(request)

    return render(request, 'festival/country/china.html', context=context_dict)

#Handle cookies
def visitor_cookie_handler(request, response):
    visits = int(request.COOKIES.get('visits', '1'))
    last_visit_cookie = request.COOKIES.get('last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
    '%Y-%m-%d %H:%M:%S')
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        response.set_cookie('last_visit', str(datetime.now()))
    else:
        response.set_cookie('last_visit', last_visit_cookie)
    response.set_cookie('visits', visits)

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,
    'last_visit',
    str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
    '%Y-%m-%d %H:%M:%S')
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
        
    request.session['visits'] = visits