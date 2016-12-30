from IPython import embed

from django.shortcuts import render
from django.http import JsonResponse

from .models import Comment
from .forms import CommentForm
# Create your views here.

def index(request):
    comments = Comment.objects.order_by('created_at')
    context = {'comments': comments}
    return render(request, 'comments/index.html', context)

def post(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return JsonResponse({'email': comment.email, 'body': comment.body, 'created_at': comment.created_at.strftime("%d.%m.%Y %H:%M:%S")})
        else:
            return JsonResponse(form.errors, status=422)
