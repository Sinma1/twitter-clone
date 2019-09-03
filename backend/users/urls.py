from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/obtain-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
]
