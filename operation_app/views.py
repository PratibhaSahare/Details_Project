from django.shortcuts import render
from django.http import HttpResponse, request

# import models in views

from . models import Student,Teacher

# Create your views here.


# direct add data
#def add_data(request):
     
     #Student.objects.create(roll_number=5,first_name='ram',last_name='mario',age=23)
     # print('data added')
     
     # Student.objects.create(roll_number=6,first_name='radha',last_name='dekate',age=22)
     
     # Teacher.objects.create(age=25,first_name='rahul',)
     
     # Student.objects.create(roll_number=8,first_name=None,age=30)
     #return HttpResponse('data added')



# add student data from templates and then add into database

def student_add(request):
     
     
     if request.method== "POST":
     

          roll_no = request.POST.get('roll')
          first_name = request.POST.get('first_name')
          last_name = request.POST.get('last_name')
          age = request.POST.get('age') 
          Student.objects.create(roll_number=roll_no,first_name=first_name,last_name=last_name,age=age)
          
          return HttpResponse("data added")

          
     return render(request,'get_add_data.html')

#####get students details

def student_details(request):
     
     student_data = Student.objects.all()
     teacher_data = Teacher.objects.all()
     
     # for student in student_data:
     #      print(student.first_name,student.last_name,student.age)
     
     # print(student_data[1])
     
     # return HttpResponse("Hello, world!")
     
     return render(request,'all_data.html',{'student_data':student_data,'teacher_data':teacher_data})

     # add teachers data from templates and then add into database

def teacher_add(request):
     
     
     if request.method== "POST":
     

          first_name = request.POST.get('first_name')
          last_name = request.POST.get('last_name')
          subject=request.POST.get('subject')
          age = request.POST.get('age') 
          Teacher.objects.create(first_name=first_name,last_name=last_name,subject=subject,age=age)
          
          return HttpResponse("data added")

     return render(request,'add_teacher_data.html')