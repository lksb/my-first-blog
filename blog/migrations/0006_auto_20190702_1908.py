# Generated by Django 2.0.13 on 2019-07-02 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190702_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='eventdate',
            field=models.DateField(default='2000.01.01', verbose_name='Eventdate (DD.MM.YYYY)'),
        ),
    ]
