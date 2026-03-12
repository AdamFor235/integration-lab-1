from django.urls import path
from .views import PostListView, PostDetailView, posts_api

urlpatterns = [
    path('', PostListView.as_view(), name='postList'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='postDetail'),
    path('api/posts/', posts_api, name='posts_api'),
]