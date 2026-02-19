from django.urls import path
from user.views import *
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('signup/', RegisterUserAPI.as_view()),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]