# Generated by Django 2.2.2 on 2019-06-20 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rates.BaseCurrency'),
        ),
    ]
