from django.db import models
# Create your models here.


class Classes(models.Model):
    name = models.CharField(max_length=16, verbose_name='班级名称')
    teacher_id = models.IntegerField(verbose_name='代课教师')
    number = models.IntegerField(verbose_name='学生人数')


class Teacher(models.Model):
    name = models.CharField(max_length=16, verbose_name='教师姓名')
    lesson_name = models.CharField(max_length=16, verbose_name='可以教授的课程')


class Student(models.Model):
    name = models.CharField(max_length=16, verbose_name='学生姓名')
    class_id = models.ForeignKey('Classes', on_delete=models.CASCADE)