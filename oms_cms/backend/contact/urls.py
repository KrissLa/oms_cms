from django.urls import path

from .views import *


urlpatterns = [
    path("feedback/", FeedbackView.as_view(), name="feedback"),
    path("feedback-gen/", FeedbackFormView.as_view(), name="feedback_gen"),
]