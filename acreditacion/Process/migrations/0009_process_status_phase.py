# Generated by Django 2.2.2 on 2019-07-14 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Process', '0008_auto_20190712_0345'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='status_phase',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]