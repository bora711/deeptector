from rest_framework import serializers
from .models import Member,D1,D2

class D1Serializer(serializers.ModelSerializer):
    class Meta:
        model = D1
        fields = ['TIME', 'LOSS']


class D2Serializer(serializers.ModelSerializer):
    class Meta:
        model = D2
        fields = ['age_group','EX_HIGH','EX_MID']


class memberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id','mask','name','in_enter','bodyTemp','state']