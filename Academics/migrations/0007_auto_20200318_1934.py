# Generated by Django 3.0.2 on 2020-03-18 14:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Academics', '0006_auto_20200318_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academics',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]