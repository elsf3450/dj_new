from django.urls import path
from  . import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('', views.ProuductMixinView.as_view()),
    path('update_detroy/<int:pk>/', views.ProductUpdateAPIView.as_view()),
    
 
]
