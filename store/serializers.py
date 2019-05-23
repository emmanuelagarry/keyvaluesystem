

from rest_framework_mongoengine import serializers

from .models import Store, StoreUpdate, StoreDelete


class StoreSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class StoreUpdateSerializer(serializers.DocumentSerializer):
    class Meta:
        model = StoreUpdate
        fields = '__all__'


class StoreDeleteSerializer(serializers.DocumentSerializer):
    class Meta:
        model = StoreDelete
        fields = '__all__'
