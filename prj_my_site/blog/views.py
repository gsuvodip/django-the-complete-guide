from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View

from .models import Post
from .forms import CommentForm

# Create your views here.

# Class Based Views

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset =  super().get_queryset()
        data = queryset[:3]
        return data
    
class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

class PostDetailPageView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        }
        return render(request, "blog/post-detail.html", context)
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False) # not committed to DB, instead create a new model
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post_detail_page", args=[slug]))
        
        # if in_valid
        
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form
        }
        return render(request, "blog/post-detail.html", context) 
        


# class PostDetailPageView(DetailView):
#     template_name = "blog/post-detail.html"
#     model = Post

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["post_tags"] = self.object.tags.all()
#         context["comment_form"] = CommentForm()
#         return context

# Function Based Views

# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3] # -date => descending order and [:3] => latest 3 posts
#     return render(request, "blog/index.html", {
#         "posts": latest_posts,
#     })

# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {
#         "all_posts": all_posts,
#     })

# def post_detail(request, slug):
#     identified_post = get_object_or_404(Post, slug=slug)
#     # identified_post = Post.objects.get(slug=slug)
#     return render(request, "blog/post-detail.html", {
#         "post": identified_post,
#         "post_tags": identified_post.tags.all(),
#     })
