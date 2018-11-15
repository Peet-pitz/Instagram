from django.test import TestCase
from .models import Image,Profile

# Create your tests here.

class ProfileTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.new_profile =Profile(profile_photo="images_TcaLGxZ.png",bio="food for good life")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    #Testing Save Method
    def test_save_method(self):
        self.new_profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_delete_method(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()


class ImageTestClass(TestCase):


    def setUp(self):
        self.new_image=Image(image="image.jpg",image_name="tarick",image_caption="color image",pub_date="two minutes ago")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_method(self):
        '''
        Function that tests whether an image is saved to database
        '''
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)