from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        # Как будет отображаться в админке
        return f"{self.author.username}: {self.title}"

    def get_excerpt(self):
        # Возвращает первые 140 символов текста
        return self.text[:140] + "..." if len(self.text) > 140 else self.text
