# Generated by Django 5.0.3 on 2024-03-18 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_notes_semester_signup_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='semester',
        ),
    ]
