# Generated by Django 4.1.1 on 2022-09-06 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_olxmodel_tittle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='olxmodel',
            name='tittle',
            field=models.CharField(max_length=2000),
        ),
    ]