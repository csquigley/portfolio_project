from django import forms
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'name',"class":"form-control"}))
    subject = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'subject',"class":"form-control"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'your message goes here',"class":"form-control"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'email address',"class":"form-control"}))
 
    captcha = CaptchaField()