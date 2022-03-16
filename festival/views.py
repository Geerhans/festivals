from django.shortcuts import render
from festival.models import Country, Festival
from datetime import datetime
from story.models import Story
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
 # 1. Query the database for a list of ALL countries currently stored.
 # 2. Filter the popular festival by the number of views in ascending order.
    popular_festival = Festival.objects.order_by('views')[:3]
    country_list = Country.objects.all()

    context_dict = {}
    context_dict['popular_festival'] = popular_festival
    context_dict['countries'] = country_list
    
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'festival/index.html', context=context_dict)
    return response

def view_festivalHistory(request,festival_name_slug):
    # 1. lists the festivals of a particular country
    try:
        festival = Festival.objects.get(slug=festival_name_slug)
        

        context_dict = {}
        context_dict['festival'] = festival
        
    except Country.DoesNotExist:
        context_dict['festival'] = None


    visitor_cookie_handler(request)
    return render(request, 'festival/festivalHistory.html', context=context_dict)


@login_required
def view_shareStory(request,id):

    # 1. View the festival stories of the selected festival posted by other users 

    context_dict = {}
    try: 
       # festival = Festival.objects.get(festivalSlug=festival_name_slug)

        festival = Festival.objects.get(id=id)
        stories = Story.objects.filter(festival=id)
     #   comment = Comment.objects.filter(festival)
        context_dict['festival'] = festival
        context_dict['stories'] = stories
     #   context_dict['comments'] = comment

    except Festival.DoesNotExist:
        context_dict['stories'] = None
        context_dict['comments'] = None
        
    return render(request, 'festival/shareStory.html', context=context_dict)

@login_required
def personalCenter(request):
    return render(request, 'festival/personalCenter.html')

def about(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'festival/about.html', context=context_dict)

def contactUs(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'festival/contactUs.html', context=context_dict)

def view_country(request, country_name_slug):
    # 1. lists the festivals of a particular country
    try:
        country = Country.objects.get(slug=country_name_slug)
        festivals= Festival.objects.filter(countryname=country)
        country_list = Country.objects.all()

        context_dict = {}
        context_dict['festivals'] = festivals
        context_dict['country'] = country
        context_dict['countries'] = country_list
    except Country.DoesNotExist:
        context_dict['festivals'] = None
        context_dict['country'] = None

    visitor_cookie_handler(request)

    return render(request, 'festival/country.html', context=context_dict)

#Handle cookies
def visitor_cookie_handler(request, response):
    visits = int(request.COOKIES.get('visits', '1'))
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



#Unwanted codes
'''
def register(request):

    registered = False
    
    if request.method == 'POST':

        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid(): 
            user = user_form.save()
            user.set_password(user.password)
            user.save()
        
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture'] 
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:

        user_form = UserForm()
        profile_form = UserProfileForm()
    # Render the template depending on the context.
    return render(request, 
                  'rango/register.html',
                  context = {'user_form': user_form,
                             'profile_form': profile_form,
                             'registered': registered})
'''

'''
def user_login(request):
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

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('festival:index'))
'''