# Generated by Django 3.1.6 on 2021-02-18 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=30, unique=True)),
                ('spwd', models.CharField(max_length=30)),
            ],
        ),
    ]