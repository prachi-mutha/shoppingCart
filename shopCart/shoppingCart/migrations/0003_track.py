# Generated by Django 3.0.8 on 2020-09-07 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingCart', '0002_auto_20200907_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('ordered_id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=400)),
            ],
        ),
    ]
