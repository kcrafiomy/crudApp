# Generated by Django 4.2.4 on 2023-08-15 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('class_name', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
