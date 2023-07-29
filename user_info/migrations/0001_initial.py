# Generated by Django 4.1.6 on 2023-05-28 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=25)),
                ('password', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=25)),
                ('gender', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to='user_info/user_image')),
            ],
        ),
    ]