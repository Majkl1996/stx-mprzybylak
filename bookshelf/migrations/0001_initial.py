# Generated by Django 3.1.2 on 2020-10-21 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('author', models.CharField(max_length=128)),
                ('date_of_publication', models.DateField(auto_now_add=True)),
                ('isbn', models.IntegerField()),
                ('number_of_pages', models.IntegerField()),
                ('cover_url', models.URLField()),
                ('language', models.CharField(max_length=32)),
            ],
        ),
    ]
