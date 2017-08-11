from django.contrib import admin

# Register your models here.
from FirstApp.models import AccessRecord,Topic,WebPage

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebPage)
