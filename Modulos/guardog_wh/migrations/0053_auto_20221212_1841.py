# Generated by Django 3.1.7 on 2022-12-12 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guardog_wh', '0052_weightsheet_destino_final'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordercontractor',
            name='Qty_PS',
            field=models.IntegerField(default=500, verbose_name='Qty PS to use on this Order'),
        ),
        migrations.AddField(
            model_name='product',
            name='contractor',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'Not')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='product',
            name='dunams',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'Not')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='product',
            name='menards',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'Not')], default='N', max_length=1),
        ),
    ]
