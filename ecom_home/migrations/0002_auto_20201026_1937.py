# Generated by Django 2.2.14 on 2020-10-26 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Category',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
