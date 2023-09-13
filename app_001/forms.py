from django import forms 
from django.forms import Form
from app_001 .models import *


class DateInput(forms.DateInput):
    input_type = "date"


class AddStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    rollnumber=forms.CharField(label="RollNumber", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))  
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )
    
    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))


class EditStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    rollnumber=forms.CharField(label="RollNumber", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )
    
    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    

class CouRegForm(forms.Form):

        cor_list = (
                       ('A','select'),
                       ('Course1','Course1'),
                        ('Course2','Course2'),
                        ('Course3','Course3'),

                 )
        stff_list=(
             ('A','select'),
                 ('Name1','Name1'),
                 ('Name2','Name2'),
                 ('Name3','Name3'),
                 ('Name4','Name4'),
                 )
        time_list=(
             ('select','select'),
             ('F/N',"F/N"),
             ('A/N','A/N'),
        )
        corselist = forms.ChoiceField(choices=cor_list, widget=forms.Select(attrs={"class":"form-control"}))
        stafflist=forms.ChoiceField( choices=stff_list, widget=forms.Select(attrs={"class":"form-control"}))
        timess=forms.ChoiceField( choices=time_list, widget=forms.Select(attrs={"class":"form-control"}))