from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers, models
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from . import permissions
# Create your views here.

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Kasarla',
        'Shiva',
        'Sai',
        'Charan',
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        """creae a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle uodating an object"""
        return Response({'method':'PUT'})

    def patch(self,request, pk=None):
        """Handle and update partial data of the object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an Object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API view Set"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello Message"""
        a_viewset = [
            'Kasarla',
            'Shiva',
            'Sai',
            'Charan'
        ]
        return Response({'message':'Hello','a_viewset':a_viewset})


    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'

            return Response({'message':message})
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handling objects by its ID"""
        return Response({'method':'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def partially_update(self,request, pk=None):
        """Handle and update part of an object"""
        return Response({'method':'PATCH'})

    def destroy(self, request, pk=None):
        """Delete an Object"""
        return Response({'method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
