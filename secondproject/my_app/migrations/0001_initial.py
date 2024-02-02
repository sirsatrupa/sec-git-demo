# Generated by Django 5.0 on 2024-01-15 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_no', models.CharField(max_length=30, unique=True)),
                ('module_name', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('lab_no', models.IntegerField()),
            ],
        ),
    ]
