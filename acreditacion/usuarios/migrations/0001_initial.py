# Generated by Django 2.2.2 on 2019-06-27 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('id_usertype', models.CharField(blank=True, max_length=10, null=True)),
                ('photo', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, default='1', max_length=1, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('status', models.CharField(blank=True, default='1', max_length=1, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
