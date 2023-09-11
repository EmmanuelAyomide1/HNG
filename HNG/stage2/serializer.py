from rest_framework import serializers
from stage2.models import Person

class PersonSerialize(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=100)
class PersonSerializeGET(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=[
            "id",
            'name'
        ]
class PersonSerializePOST(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=[
            'name'
        ]