# Generated by Django 4.2.5 on 2023-09-14 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookdoc', '0003_doctor_dept'),
    ]

    operations = [
        migrations.CreateModel(
            name='dept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.TextField(default='')),
            ],
        ),
    ]
