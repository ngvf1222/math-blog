from django.db import models
from django.db.models.fields import BigIntegerField
class Question(models.Model):
    ids = models.TextField()
    subject = models.TextField()
    content = models.TextField()
    series = models.TextField()
    point = BigIntegerField(default=0)
    create_date = models.DateTimeField()
    def __str__(self):
        return self.subject
        


class Answer(models.Model):
    ids = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
# Create your models here.
