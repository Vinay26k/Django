from django import forms
from AppTwo.models import User

class NewUserForm(forms.ModelForm):
    #f_name = forms.CharField()
    class Meta():
        model = User
        fields = '__all__'
