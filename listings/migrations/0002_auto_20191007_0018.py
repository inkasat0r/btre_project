# Generated by Django 2.2 on 2019-10-06 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='state',
            field=models.CharField(default='n/a', max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bathrooms',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]
