from django import forms

class HelloForm(forms.Form):
#    name=forms.CharField(label="name")
#    mail=forms.CharField(label="mail")
#    age=forms.IntegerField(label="age")
    id=forms.IntegerField(label="ID")
