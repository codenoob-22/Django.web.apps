from django.test import TestCase
from django.utils import timezone
import datetime

from .models import Question, Choice
# Create your tests here.

class QUestionModelTests(TestCase):
    
    def test_was_published_recently_with_future_question(self):
        """
        was published recently should return false forquestions whose pub_date is in future 
        """
        time = timezone.now() +datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently, False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() +datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(),False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(),True)