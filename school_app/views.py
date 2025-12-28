from django.shortcuts import render
from school_app.models import Post
from random import randint
# Create your views here.
def PostListView(request):
    posts = Post.objects.prefetch_related("pictures")
    context = {
        "posts" : posts,
    }
    return render(request, "school_app/main_page.html",context)

def PostByMonthView(request):
    month = request.GET.get("month")
    posts = Post.objects.filter(month=month)
    context = {
        "posts" : posts,
    }
    return render(request, "school_app/main_page.html",context)

def PostByCategoryView(request):
    category = request.GET.get("category")
    posts = Post.objects.filter(category=category)
    context = {
        "posts" : posts,
    }
    return render(request, "school_app/main_page.html",context)

def RandomPostView(request):
    posts= []
    postl = Post.objects.count()
    post = Post.objects.get(id=randint(1,postl))
    posts.append(post)
    context = {
        "posts" : posts,
    }
    return render(request, "school_app/main_page.html",context)

def SearchView(request):
    return 0
