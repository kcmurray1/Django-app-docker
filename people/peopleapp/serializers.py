from rest_framework import serializers
from peopleapp.models import Person

class PersonSerializer(serializers.ModelSerializer):

    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        return PersonSerializer(obj.children.all(), many=True).data
    
    class Meta:
        model = Person
        fields = "__all__"