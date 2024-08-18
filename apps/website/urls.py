from django.urls import path
from apps.website.views import (
    TeamAPIView,
    TeamDetailAPIVIew,
    TestimonialAPIView,
    TestimonialDetailAPIView,
    ClientAPIView,
    ClientDetailAPIView,
    MessageAPIView,
    MessageDetailAPIView,
)

urlpatterns = [
    path("team-members/", TeamAPIView.as_view(), name="team-members"),
    path("team/<int:pk>/", TeamDetailAPIVIew.as_view(), name="team-member-details"),

    path("testimonials/", TestimonialAPIView.as_view(), name="testimonials"),
    path("testimonials/<int:pk>/", TestimonialDetailAPIView.as_view(), name="testimonial-details"),

    path("clients/", ClientAPIView.as_view(), name="clients"),
    path("clients/<int:pk>/", ClientDetailAPIView.as_view(), name="client-details"),
    
    path("messages/", MessageAPIView.as_view(), name="messages"),
    path("messages/<int:pk>/", MessageDetailAPIView.as_view(), name="message-details"),
]