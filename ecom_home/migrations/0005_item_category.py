# Generated by Django 2.2.14 on 2020-10-26 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_home', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom_home.CATEGORY'),
        ),
    ]
