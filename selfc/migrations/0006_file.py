# Generated by Django 4.2.5 on 2023-10-05 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selfc', '0005_alter_usuarios_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/')),
            ],
        ),
    ]