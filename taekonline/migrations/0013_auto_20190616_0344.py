# Generated by Django 2.2.1 on 2019-06-16 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taekonline', '0012_auto_20190616_0145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classagenda',
            name='week_day',
        ),
        migrations.AddField(
            model_name='classagenda',
            name='class_cathegory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='taekonline.ClassCathegory'),
        ),
        migrations.AddField(
            model_name='classagenda',
            name='friday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='classagenda',
            name='monday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='classagenda',
            name='saturday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='classagenda',
            name='sunday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='classagenda',
            name='thursday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='classagenda',
            name='tuesday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='classagenda',
            name='wednesday',
            field=models.BooleanField(default=False),
        ),
    ]