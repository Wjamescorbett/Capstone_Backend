# Generated by Django 3.2.8 on 2022-01-17 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quoteShare', '0006_postedcomment_postedquote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postedquote',
            name='comments',
        ),
    ]
