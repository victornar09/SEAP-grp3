
from dataclasses import field
from rest_framework import serializers
from register.models.owner import owner
from register.models.property import property
from register.serializers.ownerSeriaizer import OwnerSerializer


class PropertySerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()
    class Meta:
        model= property
        field = ['idProperty', 'addressProperty', 'idOwner', 'typeProperty']

    def registrar(self, validated_data):
        ownerData = validated_data.pop('owner')
        propertyInstance = property.objects.registrar(**validated_data)
        owner.objects.create(user=propertyInstance, **ownerData)
        return propertyInstance

    def to_representation(self, obj):
        property = owner.objects.get(id=obj.id)
        owner= owner.objects.get(user=obj.id)
        return {
            'idproperty': property.idproperty,
            'addressProperty': property.addressProperty,
            'typeProperty': property.typeProperty,
            'idOwner': {
                'idowner': owner.idOwner,
                'nameOwner': owner.nameOwner,
                'addressOwner': owner.addressOwner,
                'emailOwner': owner.emailOwner
            }
        }

