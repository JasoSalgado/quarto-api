from rest_framework.decorators import api_view
from .models import User, Room
from .serializers import UserSerializer, RoomSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import viewsets


"""
To have access to the functions below, we just need the serializer_class and queryset
"""
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


"""
UserApiView class allows us to see a user´s list
"""
class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
UserDetail class allows us to see details from a user
We can get, put and delete a user
"""
class UserDetail(APIView):
    def get_object(self, id):
        try:
            return User.objects.get(id=id)

        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def get(self, request, id):
        user = self.get_object(id)
        serializer = UserSerializer(user)
        return Response(serializer.data)


    def put(self, request, id):
        user = self.get_object(id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        user = self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
RoomViewSet brings the complete list.
"""

class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


"""
RoomApiView class allows us to see a room´s list
"""
class RoomAPIView(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = RoomSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
RoomDetail allows us to see details from a room
We can get, put and delete a room
"""
class RoomDetail(APIView):
    def get_object(self, id):
        try:
            return Room.objects.get(id=id)

        except Room.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def get(self, request, id):
        room = self.get_object(id)
        serializer = RoomSerializer(room)
        return Response(serializer.data)


    def put(self, request, id):
        room = self.get_object(id)
        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        room = self.get_object(id)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
Favorites
"""
def return_favorites(request, id):
    favorites = Favorites.objects.all()
    print(favorites[0])
    favorites = favorites.filter(id_user=id)
    print(favorites)   
    print('Existe favoritos : {exists}'.format(exists=favorites.exists()))
    if(favorites.exists() == False):
        error = {
            'status': 204,
            'message': 'El usuario no tiene favoritos.'
        }
        return Response(error)
    data = []
    for favorite in favorites:
        aux = {
            #'oa': str(favorite)
            'id': favorite.id_room.id,  
            'created': str(favorite.id_room.created_date),
            'id_user': {
                'name': favorite.id_room.id_user.name,
                'last_name': favorite.id_room.id_user.lastname,
                'phone': favorite.id_room.id_user.phone,
                'email': favorite.id_room.id_user.email,
            },
            #'picture': str(favorite.id_room.picture),
            'pictures': {
                'image_1': favorite.id_room.id_images.image_1,
                'image_2': favorite.id_room.id_images.image_2,
            },
            'price': favorite.id_room.price,
            'nearest_places': favorite.id_room.nearest_places,
            'mts2': favorite.id_room.mts2,
            'furniture': favorite.id_room.furniture,
            'private_bath': favorite.id_room.private_bath,
            'wifi': favorite.id_room.wifi,
            'closet': favorite.id_room.closet,
            'kitchen': favorite.id_room.kitchen,
            'pet': favorite.id_room.pet,
            'washing_machine': favorite.id_room.washing_machine,
            'furnished': favorite.id_room.furnish,
            'tv': favorite.id_room.tv,
            'smoke': favorite.id_room.smoke,
            'couple': favorite.id_room.couple,
            'family_atmosphere': favorite.id_room.family_atmosphere,
            'description': favorite.id_room.description,
            'available': favorite.id_room.available,
        } 
        data.append(aux)
    return Response(data)