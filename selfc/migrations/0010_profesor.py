# Generated by Django 4.2.5 on 2023-10-08 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selfc', '0009_remove_activity_completed_space'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('email', models.EmailField(max_length=200, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('role', models.CharField(default='admin', max_length=50)),
            ],
        ),
    ]
