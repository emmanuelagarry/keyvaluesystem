

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Store, StoreUpdate
from .serializers import StoreSerializer, StoreUpdateSerializer, StoreDeleteSerializer

import sys
class StoreView(APIView):

    def get(self, request):
        serializer = StoreSerializer(Store.objects.all(), many=True)
        response = serializer.data
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        serializer = StoreSerializer(data=data)
        if serializer.is_valid():
            store = Store(**data)
            store.save()
            response = serializer.data
            return Response(response, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        data = request.data
        serializer = StoreUpdateSerializer(data=data)
        if serializer.is_valid():
            # storeUpdate = StoreUpdate(**data)
            Store.objects(
                id=data["objectId"]).update_one(courseName=data["courseName"])
            response = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response('not valid')

    def delete(self, request, format=None):
        data = request.data
        print(data)
        serializer = StoreDeleteSerializer(data=data)
        if serializer.is_valid():
            Store.objects(id=data["objectId"]).delete()
            response = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response('not valid')


# git commit - am " djongo deleted changed to mongoengine. added update and delete methods"
