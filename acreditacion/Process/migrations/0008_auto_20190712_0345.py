# Generated by Django 2.2.2 on 2019-07-12 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Process', '0007_auto_20190707_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='close_date',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
