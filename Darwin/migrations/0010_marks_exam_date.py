# Generated by Django 2.0.6 on 2018-07-12 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Darwin', '0009_auto_20180712_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='exam_date',
            field=models.DateField(default='2000-01-1'),
        ),
    ]
