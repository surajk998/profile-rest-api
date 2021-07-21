from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework import viewsets

from profile_api import serializers
from profile_api import models

from profile_api import permissions
from rest_framework.authentication import TokenAuthentication 

from rest_framework import filters

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from rest_framework.permissions import IsAuthenticated


class HelloApiView(APIView):
  '''test api view'''

  serializer_class = serializers.HelloSerializer

  def get(self, request, format=None):
    '''Returns list of APIView features'''
    an_apiview = [
      'Uses HTTP methods as function (get, post, put, patch, delete)',
      'Is similar to traditional Django View',
      'Gives you the most control over your application logic',
      'Is mapped manually to URLs'
    ]

    return Response({'message':'Hello','an_apiview': an_apiview})

  def post(self, request):
    '''Create a Hello message with our name'''
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f"Hello {name}"
      return Response({'message':message})
    else:
      return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )

  def put(self, request, pk=None):   # pk = primary key of item id to be updated
    '''Handle updating object'''
    return Response({'method':'PUT'})

  def patch(self, request, pk=None):
    '''Handling partial update of an object, failed request updates'''
    return Response({'method':'PATCH'})

  def delete(self, request, pk=None):
    '''Delete an object'''
    return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
  '''Test APi viewset'''
  
  serializer_class = serializers.HelloSerializer

  def list(self,request):
    a_viewset = [
      'Hi this is a viewset.'
     ]
    return Response({'Message':'Hello','ViewSet':a_viewset})

  def create(self, request):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      return Response({'message':f"Hello {name}"})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def retrieve(self, request, pk=None):
    return Response({'message':'GET'})
  
  def update(self, request, pk=None):
    return Response({'message':"PUT"})

  def partial_update(self,request,pk=None):
    return Response({'method':'PATCH'})

  def destroy(self, request, pk=None):
    return Response({'method':"DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.UserProfileSerializer
  queryset = models.UserProfile.objects.all().order_by('id')
  authentication_classes = (TokenAuthentication, )
  permission_classes = (permissions.UpdateOwnProfile, )
  filter_backends = (filters.SearchFilter, filters.OrderingFilter, )
  search_fields = ('id', 'name')
  ordering_fields = ('id', 'name')
  ordering = ['id']


class UserLoginApiView(ObtainAuthToken):
  '''handling create user authentication tokens'''
  renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
  ''' handling creating, reading and updating profile feed items'''

  authentication_classes = (TokenAuthentication, )
  serializer_class = serializers.ProfileFeedItemSerializer
  queryset = models.ProfileFeedItem.objects.all().order_by('id')
  permission_classes = ( permissions.UpdateOwnStatus, IsAuthenticated )

  def perform_create(self, serializer):
    '''sets the user profile to the logged in user'''
    serializer.save(user_profile = self.request.user)