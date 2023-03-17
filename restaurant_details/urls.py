from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('allrestaurants/', views.RestaurantList, name='restaurants'),
    path('allrestaurants/<int:id>', views.RestaurantDetail, name='restaurant_detail'),
    path('restaurants/sort/<str:order>/', views.SortRestaurantsByRating, name='sort_by_rating'),
    path('restaurants/city/<str:city>/', views.RestaurantListByCity, name='sort_by_city'),
    path('restaurants/rating/<int:restaurant_id>/get/<int:user_id>', views.Review_Rating, name='rating_all'),
    path('restaurants/rating/<int:restaurant_id>/update/<int:user_id>', views.Review_Rating, name='rating_update'),
    path('restaurants/rating/<int:restaurant_id>/delete/<int:user_id>', views.Review_Rating, name='rating_delete'),
    path('restaurants/<int:restaurant_id>/bookmark/<int:user_id>', views.bookmark, name='bookmark'),
    path('restaurants/bookmarked/<int:user_id>', views.user_bookmarked, name='user_bookmarked'),
    path('restaurants/visited/<int:user_id>', views.user_visited, name='user_visited'),


    # path('restaurants/<int:restaurant_id>/mark_visited/', views.mark_visited, name='mark_visted'),    
    # path('restaurants/<int:restaurant_id>/remove_bookmark/', views.remove_bookmark, name='remove_bookmark'),   
    # path('restaurants/<int:restaurant_id>/remove_visited/', views.remove_visited, name='remove_visited')
]
