# Generated by Django 4.1.4 on 2023-03-28 02:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogPost",
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
                ("post_title", models.CharField(max_length=70)),
                ("post_content", models.TextField(max_length=10000)),
                (
                    "img",
                    models.ImageField(
                        blank=True,
                        default="https://www.iforium.com/wp-content/uploads/Placeholder-Image-400.png",
                        upload_to="blog_images/",
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(blank=True, default=datetime.datetime.now),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
