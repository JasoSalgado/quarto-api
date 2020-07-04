from django.urls import path, include
from .views import user_list, user_detail, UserAPIView, UserDetail, UserGenericAPIView, UserViewSet, room_list, room_detail, RoomAPIView, RoomDetail, RoomGenericAPIView, RoomViewSet #SignUpView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', UserViewSet, basename = 'user')
router.register('room', RoomViewSet, basename = 'room')

urlpatterns = [
    # viewset urls
    path('viewset/', include(router.urls)),
    path('viewset/<int:id>/', include(router.urls)),
    
    path('user/', user_list),
    path('room/', room_list),
    
    path('user/', UserAPIView.as_view()),
    path('room/', RoomAPIView.as_view()),
    
    # UserDetail shows user detail
    path('user_detail/<int:id>/', UserDetail.as_view()),
    path('room_detail/<int:id>/', RoomDetail.as_view()),
    
    
    # UserGenericAPIViews allows to create another user
    path('generic/user/<int:id>/', UserGenericAPIView.as_view()),
    path('generic/room/<int:id>/', RoomGenericAPIView.as_view()),
    
]


