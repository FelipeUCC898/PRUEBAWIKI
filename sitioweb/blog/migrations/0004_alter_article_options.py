# Generated by Django 5.1.3 on 2024-11-22 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_date_alter_article_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date'], 'verbose_name': 'Articulo', 'verbose_name_plural': 'Articulos'},
        ),
    ]
