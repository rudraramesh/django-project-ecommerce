# Generated by Django 4.0 on 2022-01-27 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_alter_product_image_url_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(null=True, upload_to='static/uploads'),
        ),
    ]
