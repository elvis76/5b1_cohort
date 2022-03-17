# from ast import Delete
# from email import message_from_string

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from .managers import PublishedManager

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    # author = models.CharField(User, on_delete=models.CASCADE,related_name='blog_posts')
    author = models.CharField(max_length=225)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,default='published')
    
    
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
    class Meta:
        ordering = ('-publish',)
        
    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('main:post_detail',
                       args=[self.publish.year,
                            self.publish.month,
                            self.publish.day, 
                            self.slug]) 


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'



# from django.urls import reverse

# Create your models here.

# class Employee(models.Model):
#     name = models.CharField(max_length=255)
#     email= models.EmailField(unique=True)
#     job_desc = models.TextField()
#     age = models.IntegerField()
#     img = models.ImageField(null=True, blank=True)
#     salary = models.FloatField()
#     date_joined = models.DateTimeField(auto_now_add=True)
#     is_active = models.BooleanField(default=True)

# class Student(models.Model):
#     name = models.CharField(max_length=255)
#     email= models.EmailField(unique=True)
#     message = models.TextField()
#     score = models.IntegerField()
#     subject = models.CharField(max_length=255)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     is_active = models.BooleanField(default=True)

    


    # def __str__(self):
    #     return self.email


    # def delete(self):
    #     self.is_active=False
    #     self.save

    # def get_absolute_url(self):
    #     return reverse("student_detail", kwargs={"student_id": self.pk})    