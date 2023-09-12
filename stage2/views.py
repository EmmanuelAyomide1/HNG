from stage2.serializer import PersonSerializePOST,PersonSerializeGET
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from stage2.models import Person
from rest_framework import status
# Create your views here.

@api_view(['GET','DELETE','PATCH'])
def Person_detail(request,id):
        person=get_object_or_404(Person,pk=id)
        if request.method=='GET':
            person_serialize=PersonSerializeGET(person)
            return Response(person_serialize.data)
        elif request.method=='DELETE':
            person.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            person_serialize=PersonSerializePOST(data=request.data)
            person_serialize.is_valid(raise_exception=True)
            person.name=request.data["name"]
            person.save()
            person_serialize=PersonSerializeGET(person)
            return Response(person_serialize.data,status=status.HTTP_200_OK)
@api_view(['POST','GET'])
def Person_list(request):
    if request.method=='POST':
        person=PersonSerializePOST(data=request.data)
        person.is_valid(raise_exception=True)
        person.save()
        return Response(person.data,status.HTTP_201_CREATED)
    else:
        person=Person.objects.all()
        person_serialize=PersonSerializeGET(person,many=True)
        return Response(person_serialize.data)


