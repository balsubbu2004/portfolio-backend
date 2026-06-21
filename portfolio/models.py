from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, storage=MediaCloudinaryStorage())
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=80)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class HeroProfile(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    tagline = models.TextField()
    years_experience = models.IntegerField(default=0)
    projects_completed = models.IntegerField(default=0)
    hero_image = models.ImageField(upload_to='hero/', storage=MediaCloudinaryStorage())
    resume_url = models.URLField(blank=True)
    
    def __str__(self):
        return self.name


class AboutSection(models.Model):
    subtitle = models.CharField(max_length=200)
    heading = models.CharField(max_length=300)
    description = models.TextField()
    about_image = models.ImageField(upload_to='about/', storage=MediaCloudinaryStorage())

    def __str__(self):
        return self.heading


class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    tag = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/', storage=MediaCloudinaryStorage())
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title