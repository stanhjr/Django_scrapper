# Generated by Django 4.1.1 on 2022-09-06 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OlxModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=2000)),
                ('name', models.CharField(max_length=2000)),
                ('src', models.CharField(max_length=2000)),
                ('price_grv', models.IntegerField()),
                ('price_dollar', models.IntegerField()),
            ],
            options={
                'ordering': ('price_grv',),
            },
        ),
    ]