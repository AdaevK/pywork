from django.shortcuts import render

from .models import Comment
# Create your views here.

def index(request):
    comments = Comment.objects.order_by('created_at')
    context = {'comments': comments}
    return render(request, 'comments/index.html', context)
