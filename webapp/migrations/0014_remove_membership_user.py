# Generated by Django 4.2.7 on 2024-02-03 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_rename_title_plan_name_plan_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='user',
        ),
    ]