# Generated by Django 3.2.5 on 2022-01-17 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='request_id',
            field=models.CharField(auto_created=True, max_length=30, primary_key=True, serialize=False),
        ),
    ]