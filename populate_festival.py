import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','festivals.settings')

import django
django.setup()
from festival.models import Country, Festival

def populate():

    china_festivals = [
        {"festivalname": "National Day","body":"the history about the festival","festivalID":1,"image_url":"National Day.jpg"},
        {"festivalname":"Dragon Boat Festival","body":"the history about the festival","festivalID":2,"image_url":"National Day.jpg"},
        {"festivalname":"Army Day","body":"the history about the festival","festivalID":3,"image_url":"National Day.jpg"}]

    india_festivals = [
        {"festivalname":"Holi","body":"the history about the festival","festivalID":1,"image_url":"National Day.jpg"},
        {"festivalname":"Independence Day","body":"the history about the festival","festivalID":2,"image_url":"National Day.jpg"},
        {"festivalname":"Dussehra","body":"the history about the festival","festivalID":3,"image_url":"National Day.jpg"}]

    uk_festivals = [
        {"festivalname":"All Saints Day","body":"the history about the festival","festivalID":1,"image_url":"National Day.jpg"},
        {"festivalname":"Christmas Day","body":"the history about the festival","festivalID":2,"image_url":"National Day.jpg"}]

    us_festivals = [
        {"festivalname":"Independence Day","body":"the history about the festival","festivalID":1,"image_url":"National Day.jpg"},
        {"festivalname":"Thanksgiving Day","body":"the history about the festival","festivalID":2,"image_url":"National Day.jpg"}]

    italy_festivals = [
        {"festivalname":"Carnevale","body":"the history about the festival","festivalID":1,"image_url":"National Day.jpg"},
        {"festivalname":"Natale","body":"the history about the festival","festivalID":2,"image_url":"National Day.jpg"}]
    
    countries = {"china": {"festivals": china_festivals,"countryID":1},
        "india": {"festivals": india_festivals,"countryID":2},
        "uk": {"festivals": uk_festivals,"countryID":3},
        "us": {"festivals": us_festivals,"countryID":4},
        "italy": {"festivals": italy_festivals,"countryID":5}}

 
    for cou,cou_data in countries.items():
        c = add_country(cou,cou_data["countryID"])
        for f in cou_data["festivals"]:
            add_festival(c,f["festivalname"],f["body"],f["festivalID"])

 
    for c in Country.objects.all():
        for f in Festival.objects.filter(countryname=c):
            print("-{0}-{1}".format(str(c),str(f)))

def add_festival(countryname,festivalname,body,festivalID):
    f = Festival.objects.get_or_create(countryname=countryname,festivalname=festivalname)[0]
    f.body =body
    f.festivalID=festivalID
    f.save()
    return f

def add_country(countryname,countryID):
    c = Country.objects.get_or_create(countryname=countryname)[0]
    c.countryID=countryID
    c.save()
    return c

if __name__ == '__main__':
        print("Starting Festival population script...")
        populate()
    
