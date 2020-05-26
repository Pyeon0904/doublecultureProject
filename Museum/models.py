from django.db import models
from django.contrib.auth.models import User
from django_db_views.db_view import DBView #pip install django-db-views , installed app='django_db_views',


# Create your models here.


class Museum(models.Model):
    museum_number = models.CharField(max_length=13, primary_key=True)
    howtogo = models.CharField(max_length=20)
    quiz1 = models.CharField(max_length=50)
    quiz2 = models.CharField(max_length=50)
    quiz3 = models.CharField(max_length=50)

    class Meta:
       ordering = ['museum_number']


class StudentProject(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    CompleteState = models.BooleanField(default=False)  # 이수 여부
    # Museum1_State = models.BooleanField(default=False)  # 이수 여부
    # Museum2_State = models.BooleanField(default=False)  # 이수 여부
    # Museum3_State = models.BooleanField(default=False)  # 이수 여부

    created = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)           # 수정일

    class Meta:
        ordering = ['created']


class Watch(models.Model):
    project = models.ForeignKey(StudentProject, on_delete=models.CASCADE,null=True)     # 만든 유저
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE,null=True)              # 해당 박물관

    stampStatus = models.BooleanField(default=False)                                    # 스탬프 상태
    create_Stamp_date = models.DateField(null=True)
    create_Stamp_time = models.TimeField(null=True)                                     # 스팸프 장소

    quiz1_answer = models.CharField(max_length=50, default=" ")                         # 퀴즈에 대한 답변
    quiz2_answer = models.CharField(max_length=50, default=" ")
    quiz3_answer = models.CharField(max_length=50, default=" ")

    modify_date = models.DateField(auto_now=True)                                       # 수정일

    class Meta:
       ordering = ['modify_date']


class Total(DBView):
    # view_definition 쿼리문 작성하면된다.
    view_definition = """
    select * from Museum_Watch
    """
    class Meta:
        managed = False
        db_table = "Total"