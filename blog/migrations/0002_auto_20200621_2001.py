# Generated by Django 3.0.7 on 2020-06-21 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.AddField(
            model_name='profile',
            name='company_name',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
