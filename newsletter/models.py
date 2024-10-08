from django.db import models

from users.models import User

NULLABLE = {"null": True, "blank": True}


class Client(models.Model):
    """Клиент сервиса"""

    name = models.CharField(
        max_length=255, verbose_name="ФИО", help_text="Введите имя клиента"
    )
    email = models.EmailField(
        max_length=100, verbose_name="Почта для рассылки", help_text="Заполните почту"
    )
    comment = models.TextField(max_length=250, verbose_name="Комментарий")
    autor = models.ForeignKey(
        User, verbose_name="автор", on_delete=models.SET_NULL, **NULLABLE
    )

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Message(models.Model):
    """Сообщение для рассылки"""

    theme = models.CharField(max_length=100, verbose_name="Тема письма")
    content = models.TextField(max_length=500, verbose_name="Содержание письма")
    autor = models.ForeignKey(
        User, verbose_name="автор", on_delete=models.SET_NULL, **NULLABLE
    )

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["theme"]

    def __str__(self):
        return self.theme


class Mailing(models.Model):
    """Рассылка"""

    date_of_first_mail = models.DateTimeField(verbose_name="Дата первой отправки")
    periodicity = models.CharField(
        max_length=1,
        verbose_name="Периодичность",
        choices={"D": "Раз в день", "W": "Раз в неделю", "M": "Раз в месяц"},
    )
    status = models.CharField(
        max_length=20,
        verbose_name="Статус рассылки",
        choices={"C": "Создана", "W": "Запущена", "F": "Завершена"},
    )
    message_id = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        verbose_name="Сообщение",
        help_text="Выберите сообщение",
    )
    client_id = models.ManyToManyField(Client, verbose_name="Клиенты")
    autor = models.ForeignKey(
        User, verbose_name="автор", on_delete=models.SET_NULL, **NULLABLE
    )

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ["message_id"]
        permissions = [
            ("can_view_mailing", "Can view mailing"),
            ("can_disable_mailing", "Can disable mailing"),
        ]

    def __str__(self):
        return str(self.date_of_first_mail)


class Attempt(models.Model):
    """Попытка отправки письма"""

    date_first_attempt = models.DateTimeField(
        verbose_name="Дата первой попытки", auto_now_add=True
    )
    date_last_attempt = models.DateTimeField(
        verbose_name="Дата последней попытки", auto_now=True
    )
    status = models.BooleanField(verbose_name="Статус попытки")
    server_response = models.CharField(max_length=100, verbose_name="Ответ сервера")
    mailing_id = models.ForeignKey(
        Mailing, on_delete=models.CASCADE, verbose_name="Рассылка", **NULLABLE
    )

    class Meta:
        verbose_name = "Попытка отправки"
        verbose_name_plural = "Попытки отправки"
        ordering = ["-date_first_attempt"]

    def __str__(self):
        return self.date_first_attempt
