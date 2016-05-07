from django.db import models

class Student(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField("نام ", max_length=100,null=True)
	last_name = models.CharField("نام خانوادگی ",max_length=100,null=True)
	birthday = models.CharField("تاریخ تولد ",max_length=10,null=True)
	phone = models.CharField("تلفن ثابت ",max_length=20,null=True)
	mobile = models.CharField("تلفن همراه ",max_length=20,null=True)
	stno = models.CharField("شماره دانشجویی ",max_length=10,null=True)
	father_name = models.CharField("نام پدر ",max_length=100,null=True)
	father_job = models.CharField("شغل پدر ",max_length=100,null=True)
	father_phone = models.CharField("تلفن پدر ",max_length=20,null=True)
	id_code = models.CharField("شماره شناسنامه ",max_length=10,null=True)
	national_id = models.CharField("کد ملی ",max_length=10,null=True)
	address = models.CharField("آدرس ",max_length=200,null=True)
	study_field = models.CharField("رشته تحصیلی ",max_length=100,null=True)
	probation = models.BooleanField("مشروطی ",default=False)
	
	def __str__(self): 
		return self.stno
	
	class Meta:
		ordering = ('id', 'first_name', 'last_name', 'stno', 'id_code', 'national_id', 'phone', 'mobile', 'father_name', 'father_phone', 'father_job', 'birthday', 'address', 'study_field', 'probation')
		
class Teacher(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField("نام ",max_length=100,null=True)
	last_name = models.CharField("نام خانوادگی ",max_length=100,null=True)
	tno = models.CharField("کد ملی ",max_length=10,null=True)
	phone = models.CharField("تلفن ثابت ",max_length=20,null=True)
	mobile = models.CharField("تلفن همراه ",max_length=20,null=True)
	address = models.CharField("آدرس ",max_length=200,null=True)
	teach_hour = models.CharField("ساعت تدریس ",max_length=20,null=True)
	
	def __str__ (self):
		return self.tno
	
	class Meta:
		ordering = ('id', 'first_name', 'last_name', 'tno', 'phone', 'mobile', 'address', 'teach_hour')
		
class Lesson(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField("نام درس ",max_length=100,null=True)
	code = models.CharField("کد درس ",max_length=100,null=True)
	capacity = models.CharField("ظرفیت ",max_length=20,null=True)
	uno = models.CharField("تعداد واحد ",max_length=20,null=True)
	cno = models.CharField("شماره کلاس ",max_length=20,null=True)
	hour = models.CharField("ساعت ",max_length=20,null=True)
	
	def __str__ (self):
		return self.code
	
	class Meta:
		ordering = ('id', 'name', 'code', 'capacity', 'uno', 'cno', 'hour')
		
class UnitSelect(models.Model):
	lesson_code = models.ForeignKey(Lesson)
	student_code = models.ForeignKey(Student)
	
	class Meta:
		ordering = ('lesson_code', 'student_code')
		
class Users(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)