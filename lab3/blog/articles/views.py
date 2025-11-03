from django.shortcuts import render
from .models import Article

def archive(request):
    posts = Article.objects.all().order_by('-created_date')
    return render(request, 'templates/archive.html', {'posts': posts})
