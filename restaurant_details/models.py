from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    title = models.CharField(max_length=255)
    reviews = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    cost_for_two = models.DecimalField(max_digits=5, decimal_places=2, default=None)
    owner = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    timings = models.CharField(max_length=255)
    VEG = 'V'
    VEGAN = 'VG'
    NON_VEG = 'NV'
    FOOD_TYPE_CHOICES = [
        (VEG, 'Vegetarian'),
        (VEGAN, 'Vegan'),
        (NON_VEG, 'Non-Vegetarian'),
    ]
    food_type = models.CharField(max_length=2, choices=FOOD_TYPE_CHOICES)
    photos = models.ManyToManyField('Photo')
    cuisines = models.ManyToManyField('Cuisine')
    menu = models.ManyToManyField('Dish')
    def __str__(self):
        return self.title
    
class Photo(models.Model):
    image = models.ImageField(upload_to='restaurant_photos/')
    def __str__(self):
        return self.image.name

class Dish(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    VEG_CHOICES = [
        ('VEG', 'Vegetarian'),
        ('NVEG', 'Non-Vegetarian')
    ]
    veg_type = models.CharField(max_length=4, choices=VEG_CHOICES)
    # restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dishes')
    # VEG = 'V'
    # NON_VEG = 'NV'
    # VEG_CHOICES = [
    #     (VEG, 'Vegetarian'),
    #     (NON_VEG, 'Non-Vegetarian')
    # ]
    def __str__(self):
        return f"{self.name} - {self.price}"

class Cuisine(models.Model):
    name = models.CharField(max_length=255)

class ReviewAndRating(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    review = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class BookmarkAndVisited(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    visited = models.BooleanField(default=False)
    bookmarked = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

# class ReviewAndRating(models.Model):
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#     author = models.CharField(max_length=100)
#     review = models.TextField()
#     rating = models.IntegerField()
    

