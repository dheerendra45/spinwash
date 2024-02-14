# Generated by Django 4.2.5 on 2024-02-14 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('w', '0002_customerdetails_hostelslots'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField()),
                ('hostel_name', models.CharField(max_length=50)),
                ('machine_number', models.IntegerField()),
                ('mobile_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HostelSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField()),
                ('hostel_name', models.CharField(max_length=50)),
                ('machine_number', models.IntegerField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='CustomerDetails',
        ),
        migrations.DeleteModel(
            name='HostelSlots',
        ),
    ]
