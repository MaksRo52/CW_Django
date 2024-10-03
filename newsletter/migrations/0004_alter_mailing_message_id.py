# Generated by Django 5.1.1 on 2024-10-03 10:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newsletter", "0003_mailing_client_id_mailing_message_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="message_id",
            field=models.OneToOneField(
                help_text="Выберите сообщение",
                on_delete=django.db.models.deletion.CASCADE,
                to="newsletter.message",
                verbose_name="Сообщение",
            ),
        ),
    ]
