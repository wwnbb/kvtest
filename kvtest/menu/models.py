from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.postgres.fields import ArrayField

class Menu(models.Model):
    name = models.fields.CharField(max_length=255)


class Link(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='links')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='childs') 
    text = models.fields.CharField(max_length=255)

    named_url = models.fields.CharField(max_length=255, blank=True, default='')
    path = models.fields.CharField(max_length=255, blank=True, default='')

    @property
    def url(self):
        if self.named_url:
            url = reverse(self.named_url)
        elif self.path:
            url = self.path
        else:
            url = ''
        return url
    
    class Meta:
        ordering = ['text']

    def __str__(self):
        return self.text
