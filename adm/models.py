from django.db import models
from django.utils import timezone
from django.urls import reverse

from django.contrib.auth.models import User


class Note(models.Model):
    photo = models.ImageField(upload_to="photos", default=None, blank=True, null=True, verbose_name="Фото")
    date = models.DateField(default=timezone.now)
    name = models.CharField('Наименование записи', max_length = 200)
    
    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'Записи'


    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        
    def __str__(self):
        return self.name
    

class Comment(models.Model):
    note = models.ForeignKey(Note, related_name='comments', on_delete = models.CASCADE)
    name = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"{self.name} - {self.note}"
    
    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'