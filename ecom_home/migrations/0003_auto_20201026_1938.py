# Generated by Django 2.2.14 on 2020-10-26 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_home', '0002_auto_20201026_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='item_by_seller',
            name='Category',
        ),
        migrations.DeleteModel(
            name='CATEGORY',
        ),
    ]
