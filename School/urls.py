from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls import patterns
from django.contrib import admin
from school_manager import views
from datetime import datetime
admin.autodiscover()

urlpatterns = [
	## Main URL ##
	url(r'^$',views.Main,name='main'),
	## About URL ##
	url(r'^about/$',views.About,name='about'),
	## Student URL ##
	url(r'^students/$',views.StudentIndex,name='student_index'),
	url(r'^students/(?P<student_id>[0-9]+)/$',views.StudentDetail,name='student_detail'),
	url(r'^students/(?P<student_id>[0-9]+)/update/$',views.UpdateStudentDetail,name='update_student_detail'),
	url(r'^students/new_student/$',views.AddStudent,name='add_student'),
	url(r'^students/(?P<student_id>[0-9]+)/delete/$',views.DeleteStudent,name='delete_student'),
	## Teacher URL ##
	url(r'^teachers/$',views.TeacherIndex,name='teacher_index'),
	url(r'^teachers/(?P<teacher_id>[0-9]+)/$',views.TeacherDetail,name='teacher_detail'),
	url(r'^teachers/(?P<teacher_id>[0-9]+)/update/$',views.UpdateTeacherDetail,name='update_teacher_detail'),
	url(r'^teachers/new_teacher/$',views.AddTeacher,name='add_teacher'),
	url(r'^teachers/(?P<teacher_id>[0-9]+)/delete/$',views.DeleteTeacher,name='delete_teacher'),
	## Lesson URL ##
	url(r'^lessons/$',views.LessonIndex,name='lesson_index'),
	url(r'^lessons/(?P<lesson_id>[0-9]+)/$',views.LessonDetail,name='lesson_detail'),
	url(r'^lessons/(?P<lesson_id>[0-9]+)/update/$',views.UpdateLessonDetail,name='update_lesson_detail'),
	url(r'^lessons/new_lesson/$',views.AddLesson,name='add_lesson'),
	url(r'^lessons/(?P<lesson_id>[0-9]+)/delete/$',views.DeleteLesson,name='delete_lesson'),
	## Unit Select ##
	url(r'^other/select_unit/$',views.SelectUnit,name='select_unit'),
	## Report ##
	url(r'^other/report/$',views.Report,name='report'),
    url(r'^admin/', include(admin.site.urls)),
    ##url(r'^school_manager/',include('school_manager.urls'))
]
