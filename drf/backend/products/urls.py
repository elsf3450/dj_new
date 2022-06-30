from django.urls import path
from  . import views

urlpatterns = [
    path('<int:pk>/', views.ProuductMixinView.as_view()),
    path('', views.ProuductMixinView.as_view()),
    path('update_detroy/<int:pk>/', views.ProductUpdateAPIView.as_view()),
    path("UserView/", views.UserView.as_view({'get': 'list', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy','post': 'create'})),
    path("UserView_append/", views.UserView_append.as_view({'get': 'list', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy','post': 'create'})),



 
]
