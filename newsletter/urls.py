from django.urls import path

from newsletter.apps import NewsletterConfig
from newsletter.views import MessageListView, MessageCreateView, MessageUpdateView, MessageDeleteView, \
    MessageDetailView, MailingCreateView

app_name = NewsletterConfig.name

urlpatterns = [
    path('', MessageListView.as_view(), name='message_list'),
    path("create/", MessageCreateView.as_view(), name="message_create"),
    path("update/<int:pk>", MessageUpdateView.as_view(), name="message_update"),
    path("delete/<int:pk>", MessageDeleteView.as_view(), name="message_delete"),
    path("message/<int:pk>", MessageDetailView.as_view(), name="message_info"),
    path('mailing/create/', MailingCreateView.as_view(), name="mailing_create")
]