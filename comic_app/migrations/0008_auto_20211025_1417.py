# Generated by Django 2.2.24 on 2021-10-25 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comic_app', '0007_auto_20211021_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='book_title',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='evaluation', to='comic_app.Title', verbose_name='タイトル'),
        ),
    ]
