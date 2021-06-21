from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

from profile_api import serializers

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