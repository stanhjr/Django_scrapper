# Generated by Django 4.1.1 on 2022-09-06 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_olxmodel_tittle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_category',
            field=models.CharField(choices=[('100', '100 items'), ('200', '200 items'), ('300', '300 items')], max_length=3),
        ),
    ]