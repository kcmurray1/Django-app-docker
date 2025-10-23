from django.urls import path
from peopleapp.views import PersonRecord, PersonCollection

urlpatterns = [
    path("people", PersonCollection.as_view(), name="people-collection"),
    path("people/<int:pk>", PersonRecord.as_view(), name="people-record"),
]