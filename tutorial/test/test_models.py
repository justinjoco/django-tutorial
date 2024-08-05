from django.test import TestCase
import datetime

from django.utils import timezone
from polls.models import Question
# Create your tests here.

class QuestionModelTests(TestCase):
    def test_pub_recently_future(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date = time)
        self.assertIs(future_question.was_published_recently(), False)
    
    def test_pub_recently_old_question(self):
        time = timezone.now() - datetime.timedelta(days = 1, seconds = 1)
        old_question = Question(pub_date = time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_pub_recent_w_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours = 23, minutes = 59)
        recent_question = Question(pub_date = time)
        self.assertIs(recent_question.was_published_recently(), True)

