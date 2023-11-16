from rest_framework import serializers
from .models import *


class DragonAddedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DragonAdded
        fields = "__all__"


class DragonRemovedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DragonRemoved
        fields = "__all__"


class DragonLocationUpdatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DragonLocationUpdated
        fields = "__all__"


class DragonFedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DragonFed
        fields = "__all__"


class MaintenancePerformedSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenancePerformed
        fields = "__all__"
