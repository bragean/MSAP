# Generated by Django 2.2.2 on 2019-07-03 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Process', '0004_indicator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_indicator', models.CharField(blank=True, max_length=10, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('user_list', models.CharField(blank=True, max_length=200, null=True)),
                ('close_date', models.DateTimeField(blank=True, null=True)),
                ('documents_list', models.CharField(blank=True, max_length=200, null=True)),
                ('status_task', models.CharField(blank=True, max_length=15, null=True)),
                ('status', models.CharField(blank=True, default='1', max_length=1, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
