from django.contrib import admin
from .models import Restaurant, Photo, Dish, Cuisine, BookmarkAndVisited, ReviewAndRating

# Register your models here.
admin.site.register(Restaurant),
admin.site.register(Photo),
admin.site.register(Dish),
admin.site.register(Cuisine),
admin.site.register(BookmarkAndVisited),
admin.site.register(ReviewAndRating)