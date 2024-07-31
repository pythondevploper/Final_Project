from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name=''),
    path('registration',views.registration,name='registration'),
    path('my-login',views.my_login,name='my-login'),
    path('user-logout',views.user_logout,name='user-logout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('create-movies',views.create_movie,name='create-movies'),
    path('details/<int:movie_id>/', views.details, name='details'),
      path('movie_detail/<int:movie_id>/', views. movie_detail, name=' movie_detail'),

    path('update/<int:id>/', views.update, name='update'),

    path('delete/<int:id>/', views.delete, name='delete'),
]
