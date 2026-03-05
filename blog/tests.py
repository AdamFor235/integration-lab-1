from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
    
    def test_post_creation(self):
        post = Post.objects.create(
            title="Test Post",
            content="Test Content",
            author=self.user
        )

        self.assertEqual(post.title, "Test Post")
        self.assertEqual(str(post), "Test Post")
