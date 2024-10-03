from django.urls import path

from newsletter.apps import NewsletterConfig
from newsletter.views import MessageListView, MailingCreateView, MailingDetailView, MailingDeleteView, MailingUpdateView

app_name = NewsletterConfig.name

urlpatterns = [
    path('', MessageListView.as_view(), name='message_list'),
    path("create/", MailingCreateView.as_view(), name="message_create"),
    path("update/<int:pk>", MailingUpdateView.as_view(), name="message_update"),
    path("delete/<int:pk>", MailingDeleteView.as_view(), name="message_delete"),
    path("message/<int:pk>", MailingDetailView.as_view(), name="message_info"),
]