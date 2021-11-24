from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField()

    def __str__(self):
        return self.name

class ToDo(models.Model):
    title = models.CharField(max_length=40)
    details = models.CharField(max_length=300)
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_completion = models.DateTimeField(blank=True)
    deadline_date = models.DateTimeField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
