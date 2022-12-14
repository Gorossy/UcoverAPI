from django.urls import path, include
from .views import CustomUserCreate
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.routers import router
app_name = 'user'

urlpatterns = [
    path('register', CustomUserCreate.as_view(), name="create_user"),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('users', include(router.urls)),
]