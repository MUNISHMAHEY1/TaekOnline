# Generated by Django 2.2.1 on 2019-06-14 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taekonline', '0009_auto_20190613_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassAgenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_day', models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], default='Mon', max_length=3)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ClassCathegory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='rankings',
        ),
    ]