from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    author = models.CharField(max_length=42)
    content = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de parution")
    category = models.ForeignKey('Category')

    def __unicode__(self):
        """
        to recognize an Article
        """
        return u"%s" % self.title


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    activation_key = models.CharField(max_length=45)
    key_expires = models.DateTimeField()

    def __unicode__(self):
        return u"%s" % self.user
