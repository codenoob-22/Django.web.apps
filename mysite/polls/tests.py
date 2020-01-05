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

    