from django.shortcuts import render

# Create your views here.
# from . import TelegramToDoI as t
def index(request):
    # t.main()
    return render(request,'Resume/index.html')

def form(request):
    return render(request,'Resume/form.html')
