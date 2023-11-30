from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts/", views.AllPostsView.as_view(), name="posts_page"),
    path("posts/<slug:slug>", views.PostDetailPageView.as_view(), name="post_detail_page"),

    # path("", views.starting_page, name="starting-page"),
    # path("posts/", views.posts, name="posts_page"),
    # path("posts/<slug:slug>", views.post_detail, name="post_detail_page"),  # /posts/my-first-post
]