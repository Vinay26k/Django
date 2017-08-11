from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# from AppTwo.models import User
from AppTwo.forms import NewUserForm
def index(request):
    # return HttpResponse('<em>My Second App</em>')
    return render(request,'AppTwo/index.html')
def help(request):
    myDict = {'ins':"Hey Help page from views.py :)"}
    return render(request,'AppTwo/help.html',context=myDict)

def users(request):
    # user_list = User.objects.order_by('FirstName')
    # user_dict = {'users':user_list}
    # return render(request,'AppTwo/users.html',context=user_dict)

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error Form Invalid")
    return render(request,'AppTwo/users.html',{'form':form})
