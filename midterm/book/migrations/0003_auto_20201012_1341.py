# Generated by Django 3.1.1 on 2020-10-12 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20201012_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pubdate',
            field=models.DateField(verbose_name='PUBDATE'),
        ),
    ]
