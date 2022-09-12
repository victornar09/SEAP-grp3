from register.models.owner import owner
from rest_framework import serializers

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = owner
        fields = ['nameOwner', 'addressOwner', 'emailOwner']