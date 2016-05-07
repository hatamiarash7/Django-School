from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django import forms
from .models import *
from .forms import *

def Main(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.author = request.user
			new_user.save()
			return redirect('../')
	else:
		form = UserForm()
	return render(request, 'school_manager/main.html', {'form': form})

def StudentIndex(request):
	student_list = Student.objects.all()
	context = {'Students':student_list}
	return render(request,'school_manager/students/index.html',context)

def StudentDetail(request, student_id):
	list = get_object_or_404 ( Student, pk=student_id)
	return render(request, 'school_manager/students/student_detail.html', {'Student' : list})

def UpdateStudentDetail(request, student_id):
	list = get_object_or_404 ( Student, pk=student_id)
	if request.method == 'POST' :
		list.first_name = request.POST.get('update_first_name')
		list.last_name = request.POST.get('update_last_name')
		list.birthday = request.POST.get('update_birthday')
		list.phone = request.POST.get('update_phone')
		list.mobile = request.POST.get('update_mobile')
		list.stno = request.POST.get('update_stno')
		list.father_name = request.POST.get('update_father_name')
		list.father_job = request.POST.get('update_father_job')
		list.father_phone = request.POST.get('update_father_phone')
		list.id_code = request.POST.get('update_id_code')
		list.national_id = request.POST.get('update_national_id')
		list.address = request.POST.get('update_address')
		list.study_field = request.POST.get('update_study_field')
		check = request.POST.get('update_probation')
		if check :
			list.probation = 1
		else :
			list.probation = 0
	list.save()
	return HttpResponseRedirect('/students/' + student_id)

def AddStudent(request):
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			new_student = form.save(commit=False)
			new_student.author = request.user
			new_student.save()
			return redirect('../')
	else:
		form = StudentForm()
	return render(request, 'school_manager/students/new_student.html', {'form': form})

def DeleteStudent(request, student_id):
	Student.objects.filter(id=student_id).delete()
	return redirect('../../')

def TeacherIndex(request):
	teacher_list = Teacher.objects.all()
	context = {'Teachers':teacher_list}
	return render(request,'school_manager/teachers/index.html',context)

def TeacherDetail(request, teacher_id):
	list = get_object_or_404 ( Teacher, pk=teacher_id)
	return render(request, 'school_manager/teachers/teacher_detail.html', {'Teacher' : list})

def UpdateTeacherDetail(request, teacher_id):
	list = get_object_or_404 ( Teacher, pk=teacher_id)
	if request.method == 'POST' :
		list.first_name = request.POST.get('update_first_name')
		list.last_name = request.POST.get('update_last_name')
		list.tno = request.POST.get('update_tno')
		list.phone = request.POST.get('update_phone')
		list.mobile = request.POST.get('update_mobile')
		list.address = request.POST.get('update_address')
		list.teach_hour = request.POST.get('update_teach_hour')
	list.save()
	return HttpResponseRedirect('/teachers/' + teacher_id)

def AddTeacher(request):
	if request.method == "POST":
		form = TeacherForm(request.POST)
		if form.is_valid():
			new_teacher = form.save(commit=False)
			new_teacher.author = request.user
			new_teacher.save()
			return redirect('../')
	else:
		form = TeacherForm()
	return render(request, 'school_manager/teachers/new_teacher.html', {'form': form})
	
def DeleteTeacher(request, teacher_id):
	Teacher.objects.filter(id=teacher_id).delete()
	return redirect('../../')

def LessonIndex(request):
	lesson_list = Lesson.objects.all()
	context = {'Lessons':lesson_list}
	return render(request,'school_manager/lessons/index.html',context)

def LessonDetail(request, lesson_id):
	list = get_object_or_404 ( Lesson, pk=lesson_id)
	return render(request, 'school_manager/lessons/lesson_detail.html', {'Lesson' : list})

def UpdateLessonDetail(request, lesson_id):
	list = get_object_or_404 ( Lesson, pk=lesson_id)
	if request.method == 'POST' :
		list.name = request.POST.get('update_name')
		list.code = request.POST.get('update_code')
		list.capacity = request.POST.get('update_capacity')
		list.uno = request.POST.get('update_uno')
		list.cno = request.POST.get('update_cno')
		list.hour = request.POST.get('update_hour')
	list.save()
	return HttpResponseRedirect('/lessons/' + lesson_id)

def AddLesson(request):
	if request.method == "POST":
		form = LessonForm(request.POST)
		if form.is_valid():
			new_lesson = form.save(commit=False)
			new_lesson.author = request.user
			new_lesson.save()
			return redirect('../')
	else:
		form = LessonForm()
	return render(request, 'school_manager/lessons/new_lesson.html', {'form': form})

def DeleteLesson(request, lesson_id):
	Lesson.objects.filter(id=lesson_id).delete()
	return redirect('../../')
	
def About(request):
	return render(request,'school_manager/about/about.html')

def SelectUnit(request):
	if request.method == "POST":
		form = UnitSelectForm(request.POST)
		if form.is_valid():
			new_unitselect = form.save(commit=False)
			new_unitselect.author = request.user
			new_unitselect.save()
			return redirect('../../')
	else:
		form = UnitSelectForm()
		unitselect_list = UnitSelect.objects.all()
		student_list = Student.objects.all()
		lesson_list = Lesson.objects.all()
		context = {'form': form, 'Students': student_list, 'Lessons': lesson_list, 'UnitSelects': unitselect_list}
	return render(request, 'school_manager/other/select_unit.html',context)

def Report(request):
	return render(request,'school_manager/other/report.html')