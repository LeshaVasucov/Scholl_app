from django.shortcuts import render
from school_app.models import Post
# Create your views here.
def PostListView(request):
    posts = Post.objects.all()
    context = {
        "posts" : posts,
    }
    return render(request, "school_app/main_page.html",context)