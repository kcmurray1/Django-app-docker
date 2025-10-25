from rest_framework import generics
from peopleapp.models import Person
from peopleapp.serializers import PersonSerializer

class PersonRecord(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonCollection(generics.ListCreateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


