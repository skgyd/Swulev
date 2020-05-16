from django.db import models

from django.urls import reverse

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    nickname = models.TextField(default='nickname')
    student_id = models.TextField()
    email = models.TextField()
    school = models.CharField(max_length = 50, default='서울여자대학교')


    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Student_User(models.Model):
    userid = models.CharField(max_length = 20, unique=True, primary_key=True)

    def __str__(self):
        return self.userid

class UserLecture(models.Model):

    RATING_FIELD = (
        ('on', 'on'),
        ('off', 'off'),
    )
    
    myuserid = models.ForeignKey('Student_User', on_delete=models.CASCADE, to_field='userid', related_name='myuserid')
    mylectureid = models.ForeignKey('Lecture', to_field='lectureid',on_delete=models.CASCADE, related_name='mylectureid')
    rating = models.CharField(max_length=10, choices=RATING_FIELD, default = "off")
    
    def get_absolute_url(self):
        return reverse('new', args=[self.mylectureid.lectureid])

class Lecture(models.Model):
    semester = models.CharField(max_length = 30)
    lectureid = models.CharField(max_length=20, primary_key=True, unique=True)
    lecturename = models.CharField(max_length=50)
    professor = models.CharField(max_length=50)
    
    def get_absolute_url(self):
        return reverse('detail', args=[self.lectureid])



class Board(models.Model):
    content = models.TextField()
    quality = models.IntegerField()
    challenge = models.IntegerField()
    recommend = models.IntegerField()
    user = models.ForeignKey('Student_User', on_delete=models.CASCADE, related_name='user_id')
    lecture = models.ForeignKey('Lecture', on_delete=models.CASCADE, related_name='lecture')

    def get_absolute_url(self):
        return reverse('detail', args=[self.lecture.lectureid])