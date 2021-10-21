# Generated by Django 3.2 on 2021-10-21 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeeksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image_main', models.ImageField(upload_to='pics')),
                ('image_1', models.ImageField(upload_to='pics')),
                ('image_2', models.ImageField(upload_to='pics')),
                ('image_link', models.URLField()),
                ('image_link_1', models.URLField()),
                ('image_link_2', models.URLField()),
            ],
        ),
    ]
