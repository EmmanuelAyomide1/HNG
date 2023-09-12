from rest_framework import serializers
from stage2.models import Person

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
    def validate_name(self,data):
        print(data)
        print(type(data))
        try:
            int(data)
        except ValueError:   
            return data
        else:
            raise serializers.ValidationError("Name must be a string.")