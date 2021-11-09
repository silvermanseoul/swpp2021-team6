from django.urls import path
from posts import views

urlpatterns = [
    path("", views.posts, name="posts"),
    path("<int:post_id>", views.post_detail, name="post_detail"),
    path("<int:post_id>/comments", views.comments, name="comments"),
    path("comments/<int:comment_id>", views.comment_detail, name="comment_detail"),
]