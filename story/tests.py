from django.test import TestCase
from festival.models import Country, Festival
from django.urls import reverse
# Create your tests here.
def add_country(countryname, countryID=0):
    country = Country.objects.get_or_create(countryname=countryname)[0] 
    country.countryID = countryID
    country.save() 
    return country

def add_festival(festivalname, festivalID=0):
    china = add_country('China', 1)   
    festival = Festival.objects.get_or_create(festivalname=festivalname, countryname=china)[0] 
    festival.festivalID = festivalID
    festival.countruname = china
    festival.save() 
    return festival

class IndexViewTests(TestCase):
    def test_postStory_view(self):
        festival = add_festival('NationalDay', 1)
        response = self.client.get(reverse('story:post_story', kwargs={'festival_id': festival.id}))
        self.assertEqual(response.status_code, 302)