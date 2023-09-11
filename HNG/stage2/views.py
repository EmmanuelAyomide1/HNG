from stage2.serializer import PersonSerialize,PersonSerializePOST
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from stage2.models import Person
from rest_framework import status
# Create your views here.

@api_view(['GET','DELETE','PATCH'])
def Person_detail(request,id):
        print(id)
        person=get_object_or_404(Person,pk=id)
        if request.method=='GET':
            person_serialize=PersonSerialize(person)
            return Response(person_serialize.data)
        elif request.method=='DELETE':
            person.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            person_serialize=PersonSerializePOST(data=request.data)
            person_serialize.is_valid(raise_exception=True)
            person.name=request.data["name"]
            person.save()
            return Response(status=status.HTTP_202_ACCEPTED)
@api_view(['POST'])
def Person_list(request):
    print(request)
    person=PersonSerializePOST(data=request.data)
    person.is_valid(raise_exception=True)
    person.save()
    return Response(person.data,status.HTTP_201_CREATED)


