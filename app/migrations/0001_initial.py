# Generated by Django 3.1.7 on 2021-05-18 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fertilizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productImage', models.ImageField(default='NoPic', upload_to='products/')),
                ('Ferlilizername', models.CharField(max_length=100, verbose_name='Ferlilizer Name')),
                ('cropname', models.CharField(max_length=100, verbose_name='Crop-Name')),
                ('soilname', models.CharField(max_length=100, verbose_name='Soil-Name')),
                ('Price', models.CharField(max_length=100, verbose_name='Expected Price')),
                ('Options', models.CharField(max_length=100, verbose_name='Buying Options')),
            ],
            options={
                'db_table': 'Fertilizer_table',
            },
        ),
    ]
