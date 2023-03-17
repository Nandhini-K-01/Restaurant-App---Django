from django.http import JsonResponse
from django.shortcuts import render
from .models import Restaurant, ReviewAndRating, Photo, Cuisine, BookmarkAndVisited
from .serializers import RestaurantSerializer, ReviewAndRatingSerializer, BookmarkAndVisitedSerializer, UserBookmarkedSerializer, UserVisitedSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@api_view(['GET','POST'])
def RestaurantList(request):
    if request.method == 'GET':
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        print("restaurant",restaurants)  
        return Response(serializer.data)
    # if request.method == 'POST':
    #     serializer = RestaurantSerializer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
      

@api_view(['GET','PUT','DELETE'])
def RestaurantDetail(request,id):
    try:
        restaurant = Restaurant.objects.get(pk=id)
    except Restaurant.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

@api_view(['GET'])
def SortRestaurantsByRating(request, order):
    if order == 'high_to_low':
        restaurants = Restaurant.objects.all().order_by('-rating').values()
    elif order == 'low_to_high':
        restaurants = Restaurant.objects.all().order_by('rating').values()
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    print("restaurant",restaurants)

    if request.method == 'GET':
        # Convert restaurant data to JSON and return it in the response
        serializer = RestaurantSerializer(restaurants, many=True)
        print("serializer",serializer)
        # restaurant_data = [{'name': r.name, 'address': r.address, 'rating': r.rating} for r in restaurants]
        return Response(serializer.data)

@api_view(['GET'])
def RestaurantListByCity(request, city):
    if request.method == 'GET':
        restaurants = Restaurant.objects.filter(location__iexact=city).order_by('title')
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)
    
@api_view(['GET','POST','DELETE','PUT'])
def Review_Rating(request,restaurant_id, user_id):
    try:
        review_rating = ReviewAndRating.objects.filter(restaurant=restaurant_id, user=user_id)
    except ReviewAndRating.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        all_data = ReviewAndRating.objects.all()
        serializer = ReviewAndRatingSerializer(all_data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReviewAndRatingSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        serializer = ReviewAndRatingSerializer(review_rating, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
            review_rating.delete()
            return Response(status=status.HTTP_204_NO_CONTENT) 
    
# @api_view(['GET','POST','DELETE','PUT'])
# def Bookmark_Visited(request, restaurant_id):
#     restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
#     bookmark, created = BookmarkAndVisited.objects.get_or_create(user=request.user, restaurant=restaurant)
#     bookmark.bookmarked = True
#     bookmark.save()
#     return JsonResponse({'status': 'success'})

@api_view(['GET','POST','DELETE','PUT'])
def bookmark(request, restaurant_id, user_id):
    try:
        bookmark = BookmarkAndVisited.objects.get(restaurant=restaurant_id, user=user_id)
    except BookmarkAndVisited.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print("request",request)
    # restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    # bookmark, created = BookmarkAndVisited.objects.get_or_create(user=request.user, restaurant=restaurant)
    if request.method == 'GET':
        all_data = BookmarkAndVisited.objects.all()
        serializer = BookmarkAndVisitedSerializer(all_data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = BookmarkAndVisitedSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    if request.method == 'PUT':
        serializer = BookmarkAndVisitedSerializer(bookmark, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_bookmarked(request, user_id):
    try:
        bookmarks = BookmarkAndVisited.objects.filter(user=user_id, bookmarked=True)
        # find_user = BookmarkAndVisited.objects.get(user=user_id)
    except BookmarkAndVisited.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        # all_data = BookmarkAndVisited.objects.filter(user=user_id, bookmarked=True).values('restaurant__title')
        serializer = UserBookmarkedSerializer(bookmarks, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def user_visited(request, user_id):
    try:
        visited = BookmarkAndVisited.objects.filter(user=user_id, visited=True)
        # find_user = BookmarkAndVisited.objects.get(user=user_id)
    except BookmarkAndVisited.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        # all_data = BookmarkAndVisited.objects.filter(user=user_id, bookmarked=True).values('restaurant__title')
        serializer = UserVisitedSerializer(visited, many=True)
        return Response(serializer.data)






    # print("bookmark", bookmark)
    # if created:
    #     bookmark.bookmarked = True
    # else:
    #     bookmark.bookmarked = not bookmark.bookmarked
    # bookmark.save()
    # return JsonResponse({'status': 'success'})

# def mark_visited(request, restaurant_id):
#     restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
#     bookmark, created = BookmarkAndVisited.objects.get_or_create(user=request.user, restaurant=restaurant)
#     bookmark.visited = not bookmark.visited
#     bookmark.save()
#     return JsonResponse({'status': 'success'})

# def remove_bookmark(request, restaurant_id):
#     restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
#     bookmark = get_object_or_404(BookmarkAndVisited, user=request.user, restaurant=restaurant)
#     bookmark.delete()
#     return JsonResponse({'status': 'success'})

# def remove_visited(request, restaurant_id):
#     restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
#     bookmark = get_object_or_404(BookmarkAndVisited, user=request.user, restaurant=restaurant)
#     bookmark.visited = False
#     bookmark.save()
#     return JsonResponse({'status': 'success'})







