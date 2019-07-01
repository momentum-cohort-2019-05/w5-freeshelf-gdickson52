# Generated by Django 2.2.2 on 2019-06-28 20:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_csv'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['date_added']},
        ),
        migrations.AddField(
            model_name='book',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]