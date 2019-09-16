from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
from django.utils import timezone

# Create your tests here.

class ProfileTestClass(TestCase):
    #Set up Method
    def setUp(self):
        '''
        test case for profiles
        '''
        self.user = User(username='tony')
        # save user
        self.user.save()
        self.profile = Profile(photo='black and white',bio='test bio',contact="abc@xyz.com",user=self.user)
        self.profile.save_profile()

def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
           # saving profile
    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
        #    delete test
    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)

def test_save_comment(self):
        reviews = Review.objects.all()
        self.assertTrue(len(reviews)>0)
       # delete comment
    def test_delete_comment(self):
        self.new_review.save_review()
        self.new_review.delete_review()
        reviews = Review.objects.all()
        self.assertTrue(len(reviews)==0)