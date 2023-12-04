# Generated by Django 4.2.7 on 2023-12-04 00:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=120)),
                ('lastname', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('phonenumber', models.IntegerField(unique=True)),
                ('birthday', models.DateTimeField()),
                ('image', models.ImageField(upload_to='profiles')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'کاربر',
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=datetime.datetime(2023, 12, 4, 0, 8, 20, 559963))),
                ('name_list', models.CharField(max_length=120, unique=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('note', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.member')),
            ],
            options={
                'verbose_name_plural': 'لیست های خرید',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=120)),
                ('item_price', models.IntegerField()),
                ('item_quantity', models.IntegerField()),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.list')),
            ],
        ),
    ]