from django.db import models
import datetime


#  모델에서 양식을 정의하고 migrations에서 정의한것을 admin파일에 어떻게 보낼건지 결정!
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # data published 이름을 가질것임 만들어진 날짜에!

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        # 최근에 만들어졌는지 아닌지... 만들어진날짜가 더크면.. 뭐보다?
        # 현재시간에서 하루 뺀거 보다! 즉 어제만들어진것보다 최근이면 true


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE)  # 질문을 포린키로 받는다!
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
