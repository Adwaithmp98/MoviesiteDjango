# Generated by Django 4.1.6 on 2023-02-14 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='p1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=250)),
                ('desc', models.TextField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]