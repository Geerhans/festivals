import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','festivals.settings')

import django
django.setup()
from festival.models import Category,Page

def populate():
    # 首先创建一些字典，列出想添加到各分类的网页
    # 然后创建一个嵌套字典，设置各分类
    # 这么做看起来不易理解，但是便于迭代，方便为模型添加数据

    python_pages = [
        {"title": "Official Python Tutorial","url":"http://docs.python.org/2/tutorial/","views":32},
        {"title":"How to Think like a Computer Scientist","url":"http://www.greenteapress.com/thinkpython/","views":16},
        {"title":"Learn Python in 10 Minutes","url":"http://www.korokithakis.net/tutorials/python/","views":8}]

    django_pages = [
        {"title":"Official Django Tutorial","url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/", "views":32},
        {"title":"Django Rocks","url":"http://www.djangorocks.com/","views":16},
        {"title":"How to Tango with Django","url":"http://www.tangowithdjango.com/","views":8}]

    other_pages = [
        {"title":"Bottle","url":"http://bottlepy.org/docs/dev/","views":32},
        {"title":"Flask","url":"http://flask.pocoo.org","views":16}]

    cats = {"Python": {"pages": python_pages,'views':128,'likes':64},
        "Django": {"pages": django_pages,'views':64,'likes':32},
        "Other Frameworks": {"pages": other_pages,'views':32,'likes':16}}

    # 下述代码迭代 cats 字典，添加各分类，并把相关的网页添加到分类中
    for cat,cat_data in cats.items():
        c = add_country(cat,cat_data['views'],cat_data['likes'])
        for p in cat_data["pages"]:
            add_page(c,p["title"],p["url"],p['views'])

    # 打印添加的分类
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("-{0}-{1}".format(str(c),str(p)))

def add_page(cat,title,url,views):
    p = Page.objects.get_or_create(category=cat,title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_country(name,views,likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
    
