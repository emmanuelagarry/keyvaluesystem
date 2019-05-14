from django.shortcuts import render
from rest_framework import viewsets
# from rest_framework_mongoengine import viewsets
from .models import Entry
from .serializers import StoreSerializer


from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# class StoreViewSets(viewsets.ModelViewSet):
#     lookup_field = 'id'
#     serializer_class = StoreSerializer

#     def get_queryset(self):
#         return Store.objects.all()


class StoreView(APIView):

    def get(self, request, format=None):
        document_id = request.query_params.get('id')
        if document_id is None: 
            store = Entry.objects.all()
            serializer = StoreSerializer(store, many=True)
            return Response(serializer.data)

        else:
            store = Entry.objects.filter(id=document_id)
            serializer = StoreSerializer(store, many=True)
            return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        document_id = request.query_params.get('id')
        store = Entry.objects.get(id=document_id)
        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
            






# class StoreView(viewsets.ModelViewSet):
    
    # queryset = Entry.objects.all()
    # serializer_class = StoreSerializer

    # queryset = Entry.objects.filter(courseCode='EDAMI')
    # serializer_class = StoreSerializer


# class EntryView(StoreView):

    # def get_object(self, queryset=None):
        # index = [i for i in Entry.objects.mongo_aggregate([
            # {
        #         '$match': {
        #             'headline': self.kwargs['path']
        #         }
        #     },
        # ])]

        # return index

