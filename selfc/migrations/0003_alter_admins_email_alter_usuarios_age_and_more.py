# Generated by Django 4.2.5 on 2023-10-01 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('selfc', '0002_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admins',
            name='email',
            field=models.EmailField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='age',
            field=models.IntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='email',
            field=models.EmailField(max_length=500, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('autocontrol', models.IntegerField()),
                ('liderazgo', models.IntegerField()),
                ('conciencia', models.IntegerField()),
                ('innovacion', models.IntegerField()),
                ('sistemico', models.IntegerField()),
                ('cientifico', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='selfc.usuarios')),
            ],
        ),
    ]
