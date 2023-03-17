from rest_framework import serializers
from .models import Restaurant, ReviewAndRating, BookmarkAndVisited

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['title','rating','owner','cost_for_two','location','address','timings']

class ReviewAndRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewAndRating
        fields = '__all__'

class BookmarkAndVisitedSerializer(serializers.ModelSerializer):
     class Meta:
        model = BookmarkAndVisited
        fields = '__all__'

class UserBookmarkedSerializer(serializers.Serializer):
    restaurant_title = serializers.CharField(source='restaurant.title')
    class Meta:
        model = BookmarkAndVisited
        fields = ['restaurant_title', 'visited', 'bookmarked', 'date_added', 'date_modified']

class UserVisitedSerializer(serializers.Serializer):
    restaurant_title = serializers.CharField(source='restaurant.title')
    class Meta:
        model = BookmarkAndVisited
        fields = ['restaurant_title', 'visited', 'bookmarked', 'date_added', 'date_modified']