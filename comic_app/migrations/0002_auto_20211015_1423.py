# Generated by Django 2.2.24 on 2021-10-15 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comic_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='state',
            field=models.IntegerField(choices=[(1, '未完'), (2, '完結')], default=2, verbose_name='状態'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='title',
            name='watch_date',
            field=models.DateField(verbose_name='読んだ日'),
        ),
        migrations.AlterField(
            model_name='title',
            name='watch_number',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='最終巻数'),
        ),
    ]
