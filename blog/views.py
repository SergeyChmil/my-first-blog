from django.shortcuts import render
# from django.http import JsonResponse
# from django.core import serializers
from django.utils import timezone
from .models import Post


# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# def post_list(request):
#     posts = serializers.serialize('json', Post.objects.all())
#     response = JsonResponse(posts, safe=False)
#     return render(request, 'blog/post_list.html', {'posts': response})
