from django.db import models

# Create your models here.

class ToDo(models.Model): # new
    title = models.CharField(max_length=80)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) # new

    def __str__(self): # new
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDos'


