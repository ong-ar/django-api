from rest_framework import serializers
from . import models
from django_api.users import serializers as user_serializers
from django_api.images import serializers as image_serializers


class NotificationsSerializer(serializers.ModelSerializer):

    creator = user_serializers.ListUserSerializer()
    image = image_serializers.SmallImageSerializer()

    class Meta:
        model = models.Notification
        fields = '__all__'
