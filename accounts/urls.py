from django.urls import path, include
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.update_profile,name='profile'),
    path('login/', views.user_login,name = 'login'),
    path('logout/', views.user_logout,name = 'logout'),
    path('add_user_review/<int:product_id>/', views.add_user_review, name='add_user_review'),
]
