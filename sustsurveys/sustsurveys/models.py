from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)



# Define Teacher Model
class Teacher(models.Model):
    # Define the fileds
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    # current_courses = models.OneTo(Course, through='')
    # past_course = models.OneToOneField(Course,)
    def __str__(self):
        return self.user.username
class Student(models.Model):
    user         = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name         = models.CharField(max_length=100, default="")
    session_begin      =models.CharField(max_length=4,validators=[RegexValidator(r'^\d{1,10}$')],default="")
    session_end = models.CharField(max_length=2,validators=[RegexValidator(r'^\d{1,10}$')],default="")
    year = models.CharField(max_length=30,default="")
    semester = models.CharField(max_length=4,default="")
    department = models.CharField(max_length=40, default="")
    reg_no       = models.CharField(max_length=10,validators=[RegexValidator(r'^\d{1,10}$')],default="")
  
    # def get_unanswered_questions(self, quiz):
    #     answered_questions = self.quiz_answers \
    #         .filter(answer__question__quiz=quiz) \
    #         .values_list('answer__question__pk', flat=True)
    #     questions = quiz.questions.exclude(pk__in=answered_questions).order_by('text')
    #     return questions

    def __str__(self):
        return self.user.username