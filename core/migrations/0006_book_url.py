# Generated by Django 2.2.2 on 2019-06-27 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_books_csv'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]