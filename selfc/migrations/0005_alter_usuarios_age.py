# Generated by Django 4.2.5 on 2023-10-05 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selfc', '0004_school_admins_role_alter_usuarios_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='age',
            field=models.CharField(max_length=20),
        ),
    ]
