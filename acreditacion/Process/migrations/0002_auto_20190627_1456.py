# Generated by Django 2.2.2 on 2019-06-27 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Process', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phase',
            name='finished',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
