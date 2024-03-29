from django import forms
from .models import *
class StudentForm(forms.ModelForm):
    s_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=60,error_messages={'required': 'Please enter your Name'})
    s_pass=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,error_messages={'required': 'Please enter your Password'})
    s_branch=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=5,error_messages={'required': 'Please select your Branch'})
    s_year=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,error_messages={'required': 'Please select your Year'})
    class Meta:
        model=Student
        fields="__all__"

class TeacherForm(forms.ModelForm):
    t_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=60,error_messages={'required': 'Please enter your Name'})
    t_pass=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,error_messages={'required': 'Please enter your Password'})
    
    class Meta:
        model=Teacher
        fields="__all__"        

class TacherUploadForm(forms.ModelForm):
    send_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=10,error_messages={'required': 'Please enter your Name'})
    branch=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=5,error_messages={'required': 'Please select your Branch'})
    year=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,error_messages={'required': 'Please enter Year'})
    sub_id=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=15,error_messages={'required': 'Please enter the subject id'})
    upload_file=forms.FileField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=60,error_messages={'required': 'Please upload a file'})
    class Meta:
        model=TeacherUpload
        fields="__all__"

class StudentUploadForm(forms.ModelForm):
    send_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=10,error_messages={'required': 'Please enter your Name'})
    t_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=10,error_messages={'required': 'Please enter your Name'})
    branch=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=5,error_messages={'required': 'Please select your Branch'})
    year=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,error_messages={'required': 'Please enter Year'})
    sub_id=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=15,error_messages={'required': 'Please enter the subject id'})
    upload_file=forms.FileField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=60,error_messages={'required': 'Please upload a file'})
    class Meta:
        model=StudentUpload
        fields="__all__"

class BranchesForm(forms.ModelForm):
    teacher_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=10,error_messages={'required': 'Please enter your Name'})
    branch=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=5,error_messages={'required': 'Please select your Branch'})
    year=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,error_messages={'required': 'Please enter Year'})        
    class Meta:
        model=Branches
        fields="__all__"