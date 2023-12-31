# Generated by Django 3.0.14 on 2023-07-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('intro', models.CharField(max_length=2000)),
                ('sub_heading01', models.CharField(max_length=500)),
                ('content01', models.CharField(max_length=5000)),
                ('sub_heading02', models.CharField(default='', max_length=500)),
                ('content02', models.CharField(default='', max_length=5000)),
                ('publish_date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(default='', upload_to='blog/images')),
            ],
        ),
    ]
