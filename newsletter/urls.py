from django.urls import path

from newsletter.apps import NewsletterConfig
from newsletter.models import Mailing
from newsletter.views import MessageListView, MailingCreateView, MailingDetailView, MailingDeleteView, \
    MailingUpdateView, MailingListView

app_name = NewsletterConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing_list'),
    path("create/", MailingCreateView.as_view(), name="mailing_create"),
    path("update/<int:pk>", MailingUpdateView.as_view(), name="mailing_update"),
    path("delete/<int:pk>", MailingDeleteView.as_view(), name="mailing_delete"),
    path("message/<int:pk>", MailingDetailView.as_view(), name="mailing_info"),
]