import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','FirstProject.settings')

import django
django.setup()


##Fake POp Script
import random
from FirstApp.models import AccessRecord,Topic,WebPage
from faker import Faker
#import Faker
fakegen = Faker()

topics = ['Search','Social','MarketPlace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        ## Create new topic
        top = add_topic()

        ##generate fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        ##Create new WebPage entry

        webpg = WebPage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        ##create fake entry for AccessRecord
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__=='__main__':
    print("Populating Script!")
    populate(20)
    print("Populating Completed!")
