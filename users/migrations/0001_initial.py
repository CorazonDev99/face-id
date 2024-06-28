# Generated by Django 5.0.6 on 2024-06-25 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200, unique=True)),
                ('image', models.ImageField(upload_to='user_images/')),
                ('face_encoding', models.BinaryField()),
            ],
        ),
    ]
