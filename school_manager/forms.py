from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django import forms
from .models import *

class BootstrapForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(BootstrapForm, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({'class': 'form-control yekan-small'})

class LoginForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({'class': 'form-control yekan-small'})

class StudentForm(BootstrapForm):
	class Meta:
		model = Student
		fields = ('first_name', 'last_name', 'stno', 'id_code', 'national_id',
		'phone', 'mobile', 'father_name', 'father_phone', 'father_job',
		'birthday', 'address', 'study_field', 'probation')		

class TeacherForm(BootstrapForm):
	class Meta:
		model = Teacher
		fields = ('first_name', 'last_name', 'tno','phone',
		'mobile', 'address', 'teach_hour')

class LessonForm(BootstrapForm):
	class Meta:
		model = Lesson
		fields = ('name', 'code', 'capacity', 'uno', 'cno', 'hour')

class UnitSelectForm(BootstrapForm):
	class Meta:
		model = UnitSelect
		fields = ('lesson_code', 'student_code')
		
class UserForm(LoginForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Users
		fields = ('username', 'password')