from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, default='No Comment')

    def get_absolute_url(self):
        # return f"http://wtodd98.pythonanywhere.com/{self.id}/"
        return f"http://127.0.0.1:8000/questions/{self.id}/"

class Question(models.Model):
    question_text = models.TextField()
    answer_text = models.TextField(blank=True, null=True)
    answered = models.BooleanField(default='False')
    category = models.CharField(max_length=255, default='No Category')
    tag = models.CharField(max_length=255, default='No Tags')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='4')

    def get_absolute_url(self):
        # return f"http://wtodd98.pythonanywhere.com/{self.id}/"
        return f"http://127.0.0.1:8000/questions/{self.id}/"

    # def __str__(self):
    #     return self.question_text + '|' + str(self.auth)

class Tag(models.Model):
    name = models.CharField(max_length=255, default='No Tag')

    def get_absolute_url(self):
        # return f"http://wtodd98.pythonanywhere.com/{self.id}/"
        return f"http://127.0.0.1:8000/questions/{self.id}/"