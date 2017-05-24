from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class RagistrationFrom(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.EmailField(max_length=50)
    email = models.CharField(max_length=30)
    password = models.IntegerField(default=30)
    gender = models.CharField(max_length=5)
    mobileno = models.IntegerField(default=0)

