from django.contrib import admin
from .models import *
class StudentAdmin(admin.ModelAdmin):
	fieldsets = [
		('Personal Info :',{'fields':['first_name','last_name','stno','id_code','national_id',
		'phone','mobile','father_name','father_phone','father_job',
		'birthday','address','study_field','probation']})
	]
	
class TeacherAdmin(admin.ModelAdmin):
	fieldsets = [
		('Info : ',{'fields':['first_name','last_name','tno','phone',
		'mobile','address','teach_hour']})
	]
	
class LessonAdmin(admin.ModelAdmin):
	fieldsets = [
		('Lesson Info : ',{'fields':['name','code','capacity','uno','cno','hour']})
	]
admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Lesson,LessonAdmin)