# Generated by Django 2.2.1 on 2019-06-13 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taekonline', '0006_rank_rankhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='order',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
