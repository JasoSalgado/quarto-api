from django.urls import path, include
from .views import UserAPIView, UserDetail, UserViewSet, RoomAPIView, RoomDetail, RoomViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('user', UserViewSet, basename = 'user')
router.register('room', RoomViewSet, basename = 'room')

urlpatterns = [
    # viewset url
    path('viewset/', include(router.urls)),

    path('user/', UserAPIView.as_view()),
    path('room/', RoomAPIView.as_view()),

    # UserDetail shows user detail
    path('user_detail/<int:id>/', UserDetail.as_view()),
    path('room_detail/<int:id>/', RoomDetail.as_view()),

]


