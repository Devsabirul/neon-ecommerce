# Generated by Django 4.2.9 on 2024-01-10 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_products_sub_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='filtername',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
