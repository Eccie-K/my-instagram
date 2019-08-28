from django.test import TestCase
from .models import Image,Profile,Comment
from django.contrib.auth.models import User

# Create your tests here.

class ImageTestCase(TestCase):
    """
    this class is for testing ImageTestCase
    """
    def setUp(self):
        """
        Creating a new image before each test
        """
        self.new_user = User(
            username="Don", email="don.gmail.com", password="$#tyuohg")
            self.new_user.save()
            self.new_image = Image(name="Don", user=self.new_user)
            self.new_image.save()


    def tearDown(self):
        """
        for clearing the database after each test
        """
        Image.objects.all().delete()

    def test_instance(self):
        """
        To test whether the new image uploaded is an instance of the Image Class
        """
        self.assertTrue(isinstance(self.new_image, Image))

    def test_init(self):
        """
        To test whether the new image is instatiated correctly
        """
        self.assertTrue(self.new_image == "Don")

    def test_image_image(self):
        """
        To test whether the new image can be added to the database.
        """
        self.new_image.save_image()
        self.assertTrue(len(Image.objects.all())>0)

class ProfileTestcases(TestCase):
    """
    This will test the profiles
    """

    def setUp(self):
        """
        This will add a new profile before each test
        """
        self.new_user = User(username="Hey")
        self.new_user.save()

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()

    def test_is_instance(self):
        """
        This will test whether the new profile is an instance of the Profile class
        """
        self.assertTrue(isinstance(self.new_user.profile, Profile))

    def test_init(self):
        """
        This will test whether the new profile is created coreectly
        """
        self.assertTrue(self.new_user.profile.bio == "Hi!")

    def test_search_users(self):
        """
        This will test whether the search function works
        """
        users = Profile.search_user("hey")
        self.assertTrue(len(users) == 1)
