
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import  ProuductMixinView,RefreshView,MyTokenObtainPairView

urlpatterns = [

    path('auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # 新添加
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),      # 新添加
    path('takeall/', ProuductMixinView.as_view()),
    path('login/',MyTokenObtainPairView.as_view(),name='login'),
    path('login2/',RefreshView.as_view()),

]
