# Generated by Django 2.2.13 on 2022-08-21 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xicor', '0003_gokumstmodel_frnd_vegeta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gokumstmodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='xicormstmodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]