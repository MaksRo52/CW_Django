from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from newsletter.forms import MessageForm, MailingForm
from newsletter.models import Mailing, Message


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("newsletter:mailing_list")


class MessageUpdateView(UpdateView):
    model = Message


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("newsletter:mailing_list")


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(ListView):
    model = Mailing


class MailingCreateView(ListView):
    model = Mailing
    form_class = MailingForm



class MailingUpdateView(ListView):
    model = Mailing


class MailingDeleteView(ListView):
    model = Mailing
