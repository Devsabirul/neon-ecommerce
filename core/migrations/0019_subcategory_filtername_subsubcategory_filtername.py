# Generated by Django 4.2.9 on 2024-01-10 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_category_filtername'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='filtername',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='subsubcategory',
            name='filtername',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
