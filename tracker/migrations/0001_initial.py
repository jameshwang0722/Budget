# Generated by Django 4.0.2 on 2022-02-26 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('comment', models.TextField()),
            ],
        ),
    ]
