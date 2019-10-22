from django.urls import path

from games import views

urlpatterns = [
    path('games/', views.GameList.as_view(),
        name=views.GameList.name),
    path('games/<int:pk>/', views.GameDetail.as_view(),
        name=views.GameDetail.name),
    path('game-categories/', views.GameCategoryList.as_view(),
        name=views.GameCategoryList.name),
    path('game-categories/<int:pk>/', views.GameCategoryDetail.as_view(),
        name=views.GameCategoryDetail.name),
    path('users/', views.UserList.as_view(),
        name=views.UserList.name),
    path('users/<int:pk>/', views.UserDetail.as_view(),
        name=views.UserDetail.name),
    path('', views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
]
