# Generated by Django 4.2.5 on 2023-09-21 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookdoc', '0009_makeappointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='makeappointment',
            name='emailid',
            field=models.EmailField(default=0, max_length=254),
        ),
    ]
