# Generated by Django 3.0.14 on 2023-06-26 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20230625_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('placed_order_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('Address01', models.CharField(default='', max_length=500)),
                ('Address02', models.CharField(default='', max_length=500)),
                ('city', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=15)),
                ('pin_code', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
    ]