from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from advat.choices import *
from time import time

def file_upload_name(instance, filename):
    return "banner/%s_%s" % (str(time()).replace('.','_'),filename)


class Post(models.Model):

    vendor = models.ForeignKey('users.User')
    sale_title = models.CharField(max_length=20)
    sale_description = models.TextField(max_length=5000)
    url = models.SlugField(max_length=200, blank=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    location = models.IntegerField(choices=LOCATIONS, default=1)
    category = models.IntegerField(choices=CATEGORIES, default=1)
    address = models.CharField(max_length=200, default="")
    banner = models.FileField(upload_to=file_upload_name , null=True, blank=True)


    def publish(self):
        self.save()

    def save(self, *args, **kwargs):
        if self.url == '':
            self.url = slugify(self.sale_title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.sale_title

