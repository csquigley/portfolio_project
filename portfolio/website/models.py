from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image_url = models.ImageField(upload_to='media/post_images',null=True)
    
    def __str__(self):
        return f'{self.title}'
class Projects(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image_url = models.ImageField(upload_to='media/post_images',null=True)
    github_url = models.URLField()
    
    def __str__(self):
        return f'{self.title}'