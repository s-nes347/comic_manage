# Generated by Django 2.2.24 on 2021-10-25 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comic_app', '0009_auto_20211025_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='total_score',
            field=models.IntegerField(blank=True, null=True, verbose_name='合計'),
        ),
    ]
