# Generated by Django 4.1.6 on 2023-05-30 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='image',
            field=models.FileField(default='', max_length=250, null=True, upload_to='image/'),
        ),
    ]