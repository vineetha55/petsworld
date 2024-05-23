from django.db import models

# Create your models here.
class tbl_category(models.Model):
    name=models.CharField(max_length=20,null=True)
    image=models.ImageField(upload_to="media",null=True)
    description=models.CharField(max_length=20,null=True)

class tbl_adding_pets(models.Model):
    category=models.CharField(max_length=20,null=True)
    breed=models.CharField(max_length=20,null=True)
    stock=models.CharField(max_length=20,null=True)
    age=models.CharField(max_length=20,null=True)
    gender=models.CharField(max_length=20,null=True)
    birthdate=models.CharField(max_length=20,null=True)
    pic=models.ImageField(upload_to="media",null=True)
    characteristics=models.CharField(max_length=20,null=True)
    description=models.CharField(max_length=20,null=True)
    price=models.CharField(max_length=20,null=True)
    status=models.CharField(max_length=20,null=True)

# class tbl_booking(models.Model):
#     user=models.ForeignKey()

class tbl_register_login(models.Model):
    firstname = models.CharField(max_length=20, null=True)
    lastname = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=20, null=True)

class tbl_Booking_Pets(models.Model):
    user=models.ForeignKey(tbl_register_login,on_delete=models.CASCADE,null=True)
    pet=models.ForeignKey(tbl_adding_pets,on_delete=models.CASCADE,null=True)
    total=models.IntegerField(null=True)
    purchased_at=models.DateTimeField(auto_now_add=True)

class tbl_adding_products(models.Model):
    category=models.CharField(max_length=20,null=True)
    image=models.ImageField(upload_to="media", null=True)
    product_name=models.CharField(max_length=20,null=True)
    price=models.CharField(max_length=20,null=True)

class tbl_dr(models.Model):
    doctors_name=models.CharField(max_length=20, null=True)
    image=models.ImageField(upload_to="media", null=True)
    specialised=models.CharField(max_length=20,null=True)

class tbl_appoinment(models.Model):
    name=models.CharField(max_length=20, null=True)
    age=models.IntegerField(null=True)
    birthdate=models.IntegerField(null=True)
    symptoms=models.CharField(max_length=20, null=True)
    district=models.CharField(max_length=20, null=True)
    place=models.CharField(max_length=20, null=True)

class tbl_pet_booking(models.Model):
    select_pet=models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=20, null=True)
    age=models.IntegerField(null=True)
    profession=models.IntegerField(null=True)
    address=models.CharField(max_length=20, null=True)
    landmark=models.CharField(max_length=20, null=True)

class tbl_product_booking(models.Model):
    user=models.ForeignKey(tbl_register_login,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(tbl_adding_products,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=20, null=True)
    landmark = models.CharField(max_length=20, null=True)
    phone = models.IntegerField(null=True)
