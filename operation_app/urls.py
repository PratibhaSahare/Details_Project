from django.urls import path
from . import views

urlpatterns = [
     
     #path("add-data/",views.add_data,name="add_data"),
     path("student-add/",views.student_add,name="student_add"),
     path("student-details/",views.student_details,name="student_details"),
     path("teacher-add/",views.teacher_add,name="teacher_add"),
     path("teacher-details/",views.teacher_details,name="teacher_details"),
     path("study/",views.my_study,name="my_study_data"),
]