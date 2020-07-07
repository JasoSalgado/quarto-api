from django.contrib import admin
from django.urls import path, include
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

"""
JWT endpoints: /api/token/ and /api/token/refresh/
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls')),
    
    
<<<<<<< HEAD
    path('', include('quarto.urls')),

    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
=======
    path(r'^api-token-auth/', obtain_jwt_token),
    path(r'^api-token-refresh/', refresh_jwt_token),
    path(r'^api-token-verify/', verify_jwt_token),
]
>>>>>>> master
