from django import forms

class UserForm(forms.Form):
    user_name=forms.CharField(required=False,label="Name")
    user_email=forms.EmailField(label="Email")
    user_phone=forms.IntegerField(label="Phone No")