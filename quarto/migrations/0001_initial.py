# Generated by Django 3.0.8 on 2020-07-08 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Images_Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image_1', models.URLField()),
                ('image_2', models.URLField()),
                ('image_3', models.URLField(blank=True)),
                ('image_4', models.URLField(blank=True)),
                ('image_5', models.URLField(blank=True)),
                ('image_6', models.URLField(blank=True)),
                ('image_7', models.URLField(blank=True)),
                ('image_8', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Jhon', max_length=100)),
                ('lastname', models.CharField(default='Doe', max_length=120)),
                ('password', models.CharField(default='0000', max_length=20)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('anfitrion', models.BooleanField(default=False)),
                ('location', models.CharField(default='bogota', max_length=120)),
                ('description', models.TextField(blank=True)),
                ('phone', models.PositiveIntegerField(blank=True, default=1112223344)),
                ('active', models.BooleanField(default=True)),
                ('picture', models.ImageField(blank=True, default='/media/rooms/pictures/user_profile.png', null=True, upload_to='users/pitures/', verbose_name='profile picture')),
                ('favorite_rooms', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quarto.Favorites')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField(blank=True, default=999999)),
                ('nearest_places', models.CharField(max_length=120)),
                ('mts2', models.CharField(default='10mts2', max_length=120)),
                ('furniture', models.TextField(blank=True)),
                ('private_bath', models.BooleanField(default=False)),
                ('wifi', models.BooleanField(default=False)),
                ('closet', models.BooleanField(default=False)),
                ('kitchen', models.BooleanField(default=False)),
                ('pet', models.BooleanField(default=False)),
                ('washing_machine', models.BooleanField(default=False)),
                ('furnish', models.BooleanField(default=False)),
                ('tv', models.BooleanField(default=False)),
                ('smoke', models.BooleanField(default=False)),
                ('couple', models.BooleanField(default=False)),
                ('family_atmosphere', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
                ('available', models.BooleanField(default=True)),
                ('id_images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quarto.Images_Room')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quarto.User')),
            ],
        ),
        migrations.AddField(
            model_name='favorites',
            name='id_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quarto.Room'),
        ),
        migrations.AddField(
            model_name='favorites',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quarto.User'),
        ),
    ]
