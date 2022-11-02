from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from ApiApp import views

# Defining the URL patterns for the API:
urlpatterns = [
    # URL pattern for the UserList view:
    path('users/', views.UserList.as_view()),
    # URL pattern for the UserDetail view:
    path('users/<int:pk>/', views.UserDetail.as_view()),
    # URL pattern for the PostList view:
    path('posts/', views.PostList.as_view()),
    # URL pattern for the PostDetail view:
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    # URL pattern for the CommentList view:
    path('comments/', views.CommentList.as_view()),
    # URL pattern for the CommentDetail view:
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    # URL pattern for the CategoryList view:
    path('categories/', views.CategoryList.as_view()),
    # URL pattern for the CategoryDetail view:
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
]

# Adding format suffixes to the URL patterns:
urlpatterns = format_suffix_patterns(urlpatterns)