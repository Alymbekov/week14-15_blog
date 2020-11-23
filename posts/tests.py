from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        #create user

        testuser1 = User.objects.create_user(
            username='testuser1', password='helloworld123'
        )
        testuser1.save()

        # Create blog post

        test_post = Post.objects.create(
            author=testuser1, title='GameOfThrones', body='JohnSnow'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        expected_author = f'{post.author}'
        expected_title = f'{post.title}'
        expected_body = f'{post.body}'
        self.assertEqual(expected_author, 'testuser1')
        self.assertEqual(expected_title, 'GameOfThrones')
        self.assertEqual(expected_body, 'JohnSnow')







