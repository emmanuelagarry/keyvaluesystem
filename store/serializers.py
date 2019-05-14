# from rest_framework_mongoengine import serializers
from rest_framework import serializers
from .models import Entry


# class StoreSerializer(serializers.DocumentSerializer):
#     class Meta:
#         model = MyStore
#         fields = '_all_'





class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = "__all__"
