from django.test import TestCase
from . import models
# Create your tests here.
class PostModelTest(TestCase):
    def test_post_model_exists(self):
        post_count = models.Post.objects.count()

        self.assertEqual(post_count,0)

class StringRepresentationTest(TestCase):
    def test_str_value(self):
        
        post = models.Post.objects.create(
            title = "this is a very long test title",
            body = "test body"
        )

        self.assertEqual(str(post), post.title[:20] + "....")