# Generated by Django 2.2.24 on 2022-01-04 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taskflow3", "0019_timeoutnodesrecord"),
    ]

    operations = [
        migrations.AddField(
            model_name="autoretrynodestrategy",
            name="interval",
            field=models.IntegerField(default=0, verbose_name="retry interval"),
        ),
    ]
