# Generated by Django 2.2.2 on 2019-07-07 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Process', '0006_task_id_process'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='id_process',
            new_name='id_phase',
        ),
    ]
