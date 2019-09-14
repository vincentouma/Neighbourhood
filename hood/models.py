from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import IntegrityError
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    profile_picture = models.ImageField(upload_to='prof_pics/',blank=True)
    prof_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    bio = models.TextField(default="")
    location = models.CharField(max_length=200,blank=True)
    contact_info = models.CharField(max_length=200,blank=True)
    profile_Id = models.IntegerField(default=0)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_location(self, location):
        self. location = location
        self.save()

    def update_bio(self,bio):
        self.bio = bio
        self.save()    


class Neighbourhood(models.Model):
    name = models.CharField(max_length = 65)
    locations = (
        ('Nairobi', 'Nairobi'),
        ('Kisumu', 'Kisumu'),
        ('Mombasa', 'Mombasa'),
        ('Nakuru', 'Nakuru'),
        ('Berlin', 'Berlin')
    )
    loc  = models.CharField(max_length=65, choices=locations)
    occupants = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Location'

    @classmethod
    def search_hood(cls, search_term):
        hoods = cls.objects.filter(name__icontains=search_term)
        return hoods




    def __str__(self):
        return f"{self.loc}"


    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()        



class Join(models.Model):
    user_id = models.OneToOneField(User)
    hood_id = models.ForeignKey(Neighbourhood)

    def __str__(self):
        return self.user_id        