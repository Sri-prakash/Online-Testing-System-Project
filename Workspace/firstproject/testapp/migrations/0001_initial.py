# Generated by Django 4.0.3 on 2022-05-23 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField(max_length=100)),
                ('ename', models.CharField(max_length=200)),
                ('esal', models.FloatField(max_length=100)),
            ],
        ),
    ]
