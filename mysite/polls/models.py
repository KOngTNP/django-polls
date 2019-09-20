import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def vote_count(id):
        """Return total votes for a given poll. id is poll id"""
       # Hint: get the question from the database 
       #       Easiest is use Question.objects.get(...) 
       # question has a choice_set attribute that is a set of choices
       # for that question.
        total = 0
        for i in Question.objects.get(id=id).choice_set.all():
            total += i.votes
        return total



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

    def find_polls_for_text(text):
       """Return list of Question objects for all polls containing some text"""        # Hint: Question.objects.filter( expression )
       # and use the relations question_text__contains or __icontains 
       ques = Question.objects.filter(question_text__contains=text)
       return ques
