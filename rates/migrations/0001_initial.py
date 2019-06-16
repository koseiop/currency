# Generated by Django 2.2.2 on 2019-06-16 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseCurrency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=3)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=3)),
                ('base', models.CharField(max_length=3)),
                ('rate_to_gbp', models.DecimalField(decimal_places=5, max_digits=15)),
                ('date', models.DateField()),
            ],
        ),
    ]