import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','festivals.settings')

import django
django.setup()
from festival.models import Country, Festival

def populate():

    china_festivals = [
        {"festivalname":"National Day","body":
        "Celebrated on: 1 October\n""\n"
        "Festival history:\n""\n"
        "National Day is a public holiday in China celebrated annually as the national day of the People's Republic of China, commemorating the formal proclamation of the establishment of the People's Republic of China on 1 October 1949.\n""\n"
        "Main attraction:\n""\n"
        "The flag-raising ceremony at Tian'anmen Square held exactly at sunrise. Thousands of people line up before sunrise just to witness this special occasion. Every true patriot can sing along to all the words of the national anthem.\n""\n"
        "National Day Parade by the civil-military.\n""\n"
        "Fireworks and light show in every city are organized by the government.",
        "festivalID":1,"image_url":"National Day.jpg"},

        {"festivalname":"Dragon Boat Festival","body":
        "Celebrated on: Fifth day of the fifth lunar month\n""\n"
        "Festival history:\n""\n"
        "Dragon Boat Festival, also known as Duanwu Festival, is a traditional and important celebration in China. The Dragon Boat Festival date is based on the lunar calendar, therefore the date varies from year to year on the Gregorian calendar. Dragon boat racing is said to originate from the legend of people paddling out on boats to seek the body of patriotic poet Qu Yuan (343-278 BC), who drowned himself in a River. The festival has long been a traditional holiday in China.\n""\n"
        "Main attraction:\n""\n"
        "Dragon boat racing is the most important activity during the Dragon Boat Festival. The wooden boats are shaped and decorated in the form of a Chinese dragon. The boat size varies by region. Generally, it is about 20–35 meters in length and needs 30–60 people to paddle it. Boat racing is held in many places in China as an important competitive sport.",
        "festivalID":2,"image_url":"National Day.jpg"},

        {"festivalname":"Army Day","body":
        "Celebrated on: 1 August\n""\n"
        "Festival history:\n""\n"
        "PLA Day also known as Army Day is a professional military holiday celebrated by the People's Liberation Army of the People's Republic of China recognizing China's armed forces.\n""\n"
        "Main attraction:\n""\n"
        "A number of ceremonies are common on Army Day. They range from a synchronized “Honor Guard” march, a flag raising ceremony that takes place in Tiananmen Square, military bands performing various renditions of the Chinese national anthem, and military parades.",
        "festivalID":3,"image_url":"National Day.jpg"}]

    india_festivals = [
        {"festivalname":"Holi","body":
        "Celebrated on: Holi marks the arrival of spring and the end of winter. It is usually celebrated in March\n""\n"
        "Festival history:\n""\n"
        "Holi is a Hindu festival that celebrates spring, love, and new life. It is also known as Festival of colours. It is believed the Holi colours came from Krishna mischievously throwing coloured water over his milkmaids when he was a boy. This developed into the practical jokes and games of Holi.\n""\n"
        "Main attraction:\n""\n"
        "On the first night of Holi, people light bonfires and throw roasting grains, popcorn, coconut and chickpeas onto them. Following day, people of all ages go into the streets for fun and paint-throwing. Everyone gets involved!\n""\n"
        "Hindus have fun by smearing each other with paint and throwing coloured water.\n",
        "festivalID":1,"image_url":"National Day.jpg"},

        {"festivalname":"Diwali","body":
        "Celebrated on: Some time between October and November.\n""\n"
        "Festival history:\n""\n"
        "Diwali is the five-day Festival of Lights, celebrated by millions of Hindus, Sikhs and Jains across the world. Diwali, which for some also coincides with harvest and new year celebrations, is a festival of new beginnings and the triumph of good over evil and light over darkness. Houses, shops and public places are decorated with small oil lamps called diyas. People also enjoy fireworks and sweets too, so it's really popular with children.\n""\n"
        "Main attraction:\n""\n"
        "Many lights and oil lamps are lit on the streets and in houses.\n""\n"
        "Fireworks and festivities.\n""\n"
        "Lakshmi, the Hindu goddess of wealth, is worshipped as the bringer of blessings for the new year.",
        "festivalID":2,"image_url":"National Day.jpg"},


        {"festivalname":"Dussehra","body":
        "Celebrated on: 10th day of the bright half (Shukla Paksha) of the month of Ashvin (Ashwayuja), according to the Hindu calendar.\n""\n"
        "Festival history:\n""\n"
        "Dussehra (Vijaya Dashami, Dasara, or Dashain) is a Hindu festival that celebrates the victory of good over evil. It is a gazetted holiday in India.\n""\n"
        "Main attraction:\n""\n"
        "Performances of the Ramlila (a short version of the epic Ramayana).\n""\n"
        "A large festival and procession including the goddess Chamundeshwari on a throne mounted on elephants.\n""\n"
        "The blessing of household and work-related tools",
        "festivalID":3,"image_url":"National Day.jpg"}]

    uk_festivals = [
        {"festivalname":"Burns Night","body":
        "Celebrated on: 15 January.\n""\n"
        "Festival history:\n""\n"
        "Burns Night is annually celebrated in Scotland on or around January 25. It commemorates the life of the bard (poet) Robert Burns, who was born on January 25, 1759. The day also celebrates Burns' contribution to Scottish culture. His best known work is Auld Lang Syne.\n""\n"
        "Main attraction:\n""\n"
        "Traditional food - Serve up a Scottish supper to remember with a classic smoked fish soup and the essential haggis, neeps, and tatties - all rounded off with a traditional clootie dumpling.",
        "festivalID":1,
        "image_url":"National Day.jpg"},

        {"festivalname":"Guy Fawke's Night","body":
        "Celebrated on: 5 November.\n""\n"
        "Festival history:\n""\n"
        "Guy Fawkes Night, also known as Guy Fawkes Day, Bonfire Night and Fireworks Night, is an annual commemoration observed primarily in Great Britain involving bonfires and fireworks displays. This annual tradition is a way of remembering the events of November 5th 1605 when a plot to blow up the Houses of Parliament, killing all inside it including the King, was foiled.\n""\n"
        "Main attraciton:\n""\n"
        "Fireworks, a major component of most Guy Fawkes Day celebrations, represent the explosives that were never used by the plotters.",
        "festivalID":2,"image_url":"National Day.jpg"},

        {"festivalname":"Remembrance Sunday","body":
        "Celebrated on: second Sunday in November.\n""\n"
        "Festival history:\n""\n"
        "Remembrance Sunday is a national opportunity to remember the service and sacrifice of all those that have defended our freedoms and protected our way of life. Remembrance poppies are a traditional symbol of Remembrance Sunday; they may be worn on clothing.\n""\n"
        "Main attraction:\n""\n"
        "The national ceremony is held in London at the Cenotaph on Whitehall, starting with two minutes' silence at 11am and concluding with the end of The Nation's Thank You procession at 1:30 pm.",
        "festivalID":3,"image_url":"National Day.jpg"}]

    us_festivals = [
        {"festivalname":"Burning Man Festival","body":
        "Celebrated on: from the last Sunday in August to the first Monday in September.\n""\n"
        "Festival history:\n""\n"
        "Burning Man is an event focused on community, art, self-expression, and self-reliance held annually in the western United States. Under a sweltering sun, and during the freezing nights, they enjoy a week of community, art, counterculture, free expression, and celebration of identity. The party culminates in a symbolic burning of a large wooden effigy, after which all the attendees meticulously clean up after themselves.",
        "festivalID":1,"image_url":"National Day.jpg"},

        {"festivalname":"Thanksgiving Day","body":
        "Celebrated on: fourth Thursday of November.\n""\n"
        "Festival history:\n""\n"
        "It originated as a day of thanksgiving and harvest festival, with the theme of the holiday revolving around giving thanks and the centerpiece of Thanksgiving celebrations remaining a Thanksgiving dinner. In American culture Thanksgiving is regarded as the beginning of the fall-winter holiday season, which includes Christmas and the New Year.\n""\n"
        "Main attraction:\n""\n"
        "Thanksgiving customs include charitable organizations offering Thanksgiving dinner for the poor, attending religious services, watching parades, and viewing football games.",
        "festivalID":2,"image_url":"National Day.jpg"},

        {"festivalname":"Coachella Valley Music And Arts Festival","body":
        "Celebrated on: Consecutive 3-day weekends in April.\n""\n"
        "Festival history:\n""\n"
        "The Coachella Valley Music and Arts Festival (commonly called the Coachella Festival or simply Coachella) is an annual music and arts festival held at the Empire Polo Club in Indio, California, in the Coachella Valley in the Colorado Desert.\n""\n"
        "Main attraction:\n""\n"
        "Features musical artists from many genres of music, including rock, pop, indie, hip hop and electronic dance music, as well as art installations and sculptures.",
        "festivalID":3,"image_url":"National Day.jpg"}]

    italy_festivals = [
        {"festivalname":"Carnevale","body":
        "Celebrated on: fourth Thursday of November.\n""\n"
        "Festival history:\n""\n"
        "Carnevale in Italy brings a burst of color to the dark, cold months of winter. A huge final celebration to eat, drink and be merry before the restrictions and solemnity of Lent. Repeatedly described as one of Italy's most beautiful Carnivals, this is likely thanks to the intricate floats decorated with fresh flowers, adding beauty and perfume to the streets of Acireale.",
        "festivalID":1,"image_url":"National Day.jpg"},

        {"festivalname":"Palio of Siena","body":
        "Celebrated on: 2 July and 16 August.\n""\n"
        "Festival history:\n""\n"
        "The Palio di Siena is a horse race that is held twice each year, in Siena, Italy. Ten horses and riders, bareback and dressed in the appropriate colours, represent ten of the seventeen contrade, or city wards. The city hosts 6 trial runs before the official race, one in the morning and one in the afternoon. The races are preceded by a historic procession and are followed by open-air dinners in each contrada.\n""\n"
        "Main attraction:\n""\n"
        "The race which only lasts about a minute, as the horses must complete three full laps around piazza del Campo.",
        "festivalID":2,"image_url":"National Day.jpg"}]
    
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
    
