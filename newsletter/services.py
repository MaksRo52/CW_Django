from datetime import datetime

import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from django.core.mail import send_mail

from newsletter.models import Mailing, Attempt


def start():
    """Функция старта периодических задач"""
    scheduler = BackgroundScheduler()
    scheduler.add_job(mail_send, "interval", seconds=10)
    scheduler.start()


def mail_send(mail, client):
    """Отправляет письма пользователям из рассылки по расписанию"""
    mail_send_ = send_mail(
        mail.name,
        mail.body,
        settings.EMAIL_HOST_USER,
        [client.email],
    )

    return mail_send_


# def send_mailing():
#     """Главная функция по отправке рассылки"""
#     zone = pytz.timezone(settings.TIME_ZONE)
#     current_datetime = datetime.now(zone)
#     # создание объекта с применением фильтра
#     mailings = Mailing.objects.filter(дата__lte=current_datetime).filter( status in=["C", "W", "F"])
#
#     for mailing in mailings:
#         send_mail(
#                 subject=theme,
#                 message=content,
#                 from_email=settings.EMAIL_HOST_USER,
#                 recipient_list=[client.email for client in mailing.клиенты.all()]
#            )
#
#
# Attempt.filter(рассылка=рассылка).order_by('-дата_рассылки').first()
#
# ...
# if Mailing.periodicity == Ежедневная_приодичность and разница_времени_текущего_и_последней_отправки.days >= 1:
#    next_send_time = дата_последней_отправки + timezone.timedelta(days=1, hours=рассылка.time.hour,
#                                                                         minutes=рассылки.time.minute)
# ...
