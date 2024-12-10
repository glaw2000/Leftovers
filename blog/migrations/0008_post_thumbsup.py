# Generated by Django 4.2.16 on 2024-12-06 19:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_alter_category_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbsup',
            field=models.ManyToManyField(related_name='post_thumbsup', to=settings.AUTH_USER_MODEL),
        ),
    ]