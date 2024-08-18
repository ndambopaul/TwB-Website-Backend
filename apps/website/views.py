from django.shortcuts import render

from rest_framework import generics

from apps.website.models import Team, Testimonial, Client, Message
from apps.website.serializers import (
    TeamSerializer,
    TestimonialSerializer,
    ClientSerializer,
    MessageSerializer,
)


# Create your views here.
class TeamAPIView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetailAPIVIew(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    lookup_field = "pk"


class MessageAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    lookup_field = "pk"


class ClientAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    lookup_field = "pk"


class TestimonialAPIView(generics.ListCreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


class TestimonialDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

    lookup_field = "pk"
