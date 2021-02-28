from django.db import models
from django.contrib.auth.models import User

class TodoItem(models.Model):
    work = models.CharField(max_length=100)
    checked = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(blank=True, null=True)

    def check_item(self):
        self.checked = True

    def __str__(self):
        return self.work
    

