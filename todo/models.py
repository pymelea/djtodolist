from django.db import models
from django.urls import reverse
# Create your models here.

class ToDo(models.Model): #
    title = models.CharField(max_length=80)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "ToDo"
        verbose_name_plural = "ToDos"


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("todo:detail", kwargs={"pk": self.pk})

    def is_complete(self):
        return self.complete

    def get_mark_complete_url(self):
        return reverse("todo:mark_complete", kwargs={"pk": self.pk})


