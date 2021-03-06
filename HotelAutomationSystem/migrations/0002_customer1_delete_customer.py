# Generated by Django 4.0.4 on 2022-04-24 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelAutomationSystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('checkin', models.DateField()),
                ('checkout', models.DateField()),
                ('no_of_rooms', models.IntegerField()),
                ('no_of_members', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(default='')),
                ('city', models.CharField(max_length=30)),
                ('phone_no', models.IntegerField()),
                ('Room_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
