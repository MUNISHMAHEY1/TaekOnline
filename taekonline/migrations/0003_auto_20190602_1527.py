# Generated by Django 2.2.1 on 2019-06-02 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taekonline', '0002_auto_20190602_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address_complement',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
