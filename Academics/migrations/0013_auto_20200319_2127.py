# Generated by Django 3.0.2 on 2020-03-19 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Academics', '0012_academics'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='des',
            new_name='des1',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='pdf',
            new_name='pdf1',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='points',
            new_name='points1',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='pointsaward',
            new_name='pointsaward1',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='user',
            new_name='user1',
        ),
    ]