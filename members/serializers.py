from rest_framework import serializers

from .models import Address, Member

class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['city', 'street', 'zipcode']

class MemberSerializer(serializers.ModelSerializer):
    address = AdressSerializer()

    class Meta:
        model = Member
        fields = ['name', 'address']

    def create(self, validated_data):
        address_validated_data = validated_data.pop('address')
        member = Member.objects.create(**validated_data)
        Address.objects.create(member=member, **address_validated_data)
        return member