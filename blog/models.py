from django.db import models
from course.models import Teacher
from django.contrib.auth.models import User


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Blog(models.Model):
    title = models.CharField(max_length=39)
    post = models.TextField()
    image = models.ImageField(upload_to='blog/blog/')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
