# Generated by Django 4.2.5 on 2023-09-19 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookdoc', '0004_dept'),
    ]

    operations = [
        migrations.CreateModel(
            name='makeappointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docname', models.CharField(max_length=100)),
                ('appDate', models.DateTimeField()),
                ('patientname', models.CharField(max_length=100)),
                ('iswaiting', models.BooleanField(default=False)),
            ],
        ),
    ]
