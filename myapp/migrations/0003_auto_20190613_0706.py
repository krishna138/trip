# Generated by Django 2.2.2 on 2019-06-13 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190612_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(default=None, help_text='Enter city name', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='loc',
            field=models.CharField(help_text='Enter Place name', max_length=50),
        ),
    ]
