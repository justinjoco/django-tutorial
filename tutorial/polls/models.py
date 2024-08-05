from django.db.models import Model, CharField, DateTimeField, ForeignKey, IntegerField, CASCADE
import datetime
from django.utils import timezone
# Create your models here.
class Question(Model):
    question_text = CharField(max_length=200)
    pub_date = DateTimeField("date published")

    def __str__(self):
        return f"{self.pk} : {self.question_text}"
    
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >=  now - datetime.timedelta(days=1)

class Choice(Model):
    question = ForeignKey(Question, on_delete=CASCADE)
    choice_text = CharField(max_length=200)
    votes = IntegerField(default=0)

    def __str__(self):
        return self.choice_text