from django.test import TestCase
from django.contrib.auth import get_user_model # import the get_user_model() to refer to our User
from django.test import TestCase # import the TestCase
from .models import Post # import our Post model
from django.urls import reverse # import reverse 

# to begin, we can set up our test data and check the Post model's content. Our class BlogTests contain set up data for both
# a test user and a test post.
class BlogTests():
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model.objects.create_user(username="testuser",email="test@email.com",password="secret")
        cls.post = Post.objects.create(
            title = "A good title",
            body = "Nice body content",
            author = cls.user,
        )
    #At the moment, all the tests are focused on the Post model, so we name our test test_post_model. It checks that all three
    # model fields return the expected values.
    def test_post_model(self):
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(self.post.author.username, "testuser")
        # There are also new tests for the __str__ and get_absolute_url methods on our model.
        self.assertEqual(str(self.post), "A good title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")

    # first, we check that the URL exists at the proper location for listview
    def test_url_exists_at_correct_location_listview(self): # new
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    # next, we check that the URL exists at the proper location for detailview
    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code, 200)
    # create a test_post_listview to confirm that the named URL is used, this should return a 200 status code, contain the
    # expected content, and use the home.html template
    def test_post_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nice body content")
        self.assertTemplateUsed(response, "home.html")
    # same thing as test_post_listview, but here we have to pass in the primary key of our post to the test the response
    # the same template is used, but we add new tests for what we don't want to see. For example, we don't want a response
    # at the URL /post/100000/ because we have not created that many posts yet; and we don't want a 404 http status response
    # either.
    def test_post_detailview(self):
        response = self.client.get(reverse("post_detail",kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/100000/")
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "post_detail.html")

    # for test_post_createview, we create a new response to check that the page has a 302 redirect status code and the 
    # last() object created on our model matches the new response.
    def test_post_createview(self):
        response = self.client.post(
            reverse("post_new"),
            {
                "title": "New title",
                "body": "New text",
                "author": self.user.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "New title")
        self.assertEqual(Post.objects.last().body, "New text")

    # for test_post_updateview, we see if we can update the initial post created in setUpTestData since the data is
    # available througout our entire test class
    def test_post_updateview(self):
        response = self.client.post(
            reverse("post_edit", args="1"),
            {
                "title": "Updated title",
                "body": "Updated text",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "Updated title")
        self.assertEqual(Post.objects.last().body, "Updated text")

    # this test confirms that a 302 redirect occurs when deleting a post
    def test_post_deleteview(self):
        response = self.client.post(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code, 302)