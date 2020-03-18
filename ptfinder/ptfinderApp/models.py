from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    firstname = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField()
    experience = models.CharField(max_length=512)
    sex = models.CharField(max_length=16) 
    location = models.CharField(max_length=30)
    img = models.ImageField(upload_to='userProfile_images',blank=True)
   
class Gym(models.Model):
    #g_id = models.AutoField(primary_key)
    name = models.CharField(max_length=20)
    owner = models.CharField(max_length=20)
    address_line1 = models.CharField(max_length=20)
    address_line2 = models.CharField(max_length=20)
    address_postcode = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    images = models.ImageField(upload_to='gym_images',blank=True)
    description = models.CharField(max_length=512)
    
    @property
    def g_id(self):
        return self.id
   
class Trainer(models.Model):
    t_username = models.CharField(max_length=30, unique=True)
    g_id = models.ForeignKey(Gym, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField()
    contact_no = models.CharField(max_length=14)
    specialism = models.CharField(max_length=512)
    sex = models.CharField(max_length=16)
    img = models.ImageField(upload_to='trainerProfile_images',blank=True)
    price = models.CharField(max_length=10)
    
class Bookings(models.Model):
    #b_id = models.AutoField(unique=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    t_username = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    datetime = models.DateField()
    location = models.CharField(max_length=30)
    
    @property
    def b_id(self):
        return self.id
        
class Trainer_Comment(models.Model):
    #tc_id = models.AutoField(unique=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    t_username = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    comment = models.CharField(max_length=512)
    datetime = models.DateField()
    
    @property
    def tc_id(self):
        return self.id