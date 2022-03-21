from django.test import TestCase
import festival
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

class CountryMethodTests(TestCase):
    def test_ensure_countryID_are_positive(self):
        country = Country(countryname='test', countryID=-1)
        country.save()
        self.assertEqual((country.countryID >= 0), True)
    
    def test_ensure_storyID_are_positive(self):
        china = add_country('China', 1)
        festival = Festival(countryname=china, festivalID=-1, festivalname='test')
        festival.save()
        self.assertEqual((festival.festivalID >= 0), True)

    def test_country_slug_line_creation(self): 
        country = Country(countryname='Random Country String')
        country.save()
        self.assertEqual(country.slug, 'random-country-string')

    def test_festival_slug_line_creation(self): 
        china = add_country('China', 1)
        festival = Festival(festivalname='Random Country String', countryname=china)
        festival.save()
        self.assertEqual(festival.slug, 'random-country-string')
    


class IndexViewTests(TestCase):
    def test_index_view_with_no_countries(self):
        response = self.client.get(reverse('festival:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no countries present.')
        self.assertQuerysetEqual(response.context['countries'], [])

    def test_country_view_with_no_festival(self):
        china = add_country('China', 1)
        response = self.client.get(reverse('festival:view_country', kwargs={'country_name_slug': china.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No festivals currently in the selected country.')
        self.assertQuerysetEqual(response.context['festivals'], [])

    def test_shareStory_view(self):
        festival = add_festival('NationalDay', 1)
        response = self.client.get(reverse('festival:view_shareStory', kwargs={'id': festival.id}))
        self.assertEqual(response.status_code, 302)

    def test_festivalHistory_view(self):
        festival = add_festival('NationalDay', 1)
        response = self.client.get(reverse('festival:view_festivalHistory', kwargs={'festival_name_slug': festival.slug}))
        self.assertEqual(response.status_code, 200)

    def test_about_view(self):
        response = self.client.get(reverse('festival:about'))
        self.assertEqual(response.status_code, 200)
        
    def test_personalCenter_view(self):
        response = self.client.get(reverse('festival:personalCenter'))
        self.assertEqual(response.status_code, 302)
    
    def test_contact_view(self):
        response = self.client.get(reverse('festival:contact'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_with_countries(self): 
        add_country('China', 1)
        add_country('India', 2)
        add_country('UK', 3)
        response = self.client.get(reverse('festival:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "China")
        self.assertContains(response, "India")
        self.assertContains(response, "UK")
        num_categories = len(response.context['countries'])
        self.assertEquals(num_categories, 3)