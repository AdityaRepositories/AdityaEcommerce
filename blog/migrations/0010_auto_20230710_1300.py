# Generated by Django 3.0.14 on 2023-07-10 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20230710_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='heading01',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='heading02',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='heading03',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]