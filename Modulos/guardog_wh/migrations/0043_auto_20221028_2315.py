# Generated by Django 3.1.7 on 2022-10-29 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guardog_wh', '0042_num_liquidacion_contractor'),
    ]

    operations = [
        migrations.CreateModel(
            name='PSpray_Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'P.Spray Type',
                'verbose_name_plural': 'P.Spray Type',
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='product',
            name='tipo_p_spray',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='guardog_wh.pspray_types'),
        ),
    ]
