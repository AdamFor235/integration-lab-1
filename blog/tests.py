
from .models import Post
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class PostModelTest(TestCase):
    def test_create_post(self):
        user = User.objects.create_user(
            username="testuser",
            password="testpass"
        )
        post = Post.objects.create(
            title="Test title",
            content="Test content",
            author=user
        )
        self.assertEqual(post.title, "Test title")
        self.assertEqual(post.content, "Test content")


class PostViewTest(TestCase):
    def test_post_list_view(self):
        response = self.client.get(reverse('postList'))
        self.assertEqual(response.status_code, 200)
