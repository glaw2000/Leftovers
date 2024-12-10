# Generated by Django 4.2.16 on 2024-12-06 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_like_unique_together_remove_post_thumbsup_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='alt_image',
            field=models.CharField(default='dish', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(default=False, related_name='posts', to='blog.like'),
        ),
    ]