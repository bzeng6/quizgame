from django.db import models


class Exam(models.Model):
    exam_title = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.exam_title

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    is_last_question = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField()

    def __str__(self):
    	return self.choice_text

