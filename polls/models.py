from django.db import models
import datetime
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=50)
    display_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.display_name} @{self.username}'
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question_text} by {self.author}'

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text