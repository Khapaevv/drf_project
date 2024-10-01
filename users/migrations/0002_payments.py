# Generated by Django 5.1.1 on 2024-10-01 15:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "payment_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="Введите дату и время оплаты",
                        null=True,
                        verbose_name="Дата и время оплаты",
                    ),
                ),
                (
                    "payment_amount",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="Введите сумму оплаты",
                        null=True,
                        verbose_name="Сумма оплаты",
                    ),
                ),
                (
                    "payment_method",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Наличные", "Наличные"),
                            ("Перевод на счет", "Перевод на счет"),
                        ],
                        null=True,
                        verbose_name="Способ оплаты",
                    ),
                ),
                (
                    "paid_course",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите оплаченный курс",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="course.course",
                        verbose_name="Опалченный курс",
                    ),
                ),
                (
                    "paid_lesson",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите оплаченный урок",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="course.lesson",
                        verbose_name="Опалченный урок",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите пользователя",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Платеж",
                "verbose_name_plural": "Платежи",
            },
        ),
    ]
