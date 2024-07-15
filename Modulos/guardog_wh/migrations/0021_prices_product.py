# Generated by Django 3.1.7 on 2022-09-29 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guardog_wh', '0020_auto_20220926_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prices_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.FloatField(default=0)),
                ('Product', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='guardog_wh.product')),
            ],
            options={
                'verbose_name': 'Price',
                'verbose_name_plural': 'Price',
            },
        ),
    ]
