# Generated by Django 4.2.9 on 2024-03-25 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_subcategory_filtername_subsubcategory_filtername'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_img',
            field=models.ImageField(blank=True, null=True, upload_to='Category Image'),
        ),
    ]
