# Generated by Django 2.2.7 on 2019-12-20 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20191220_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.FileField(blank=True, default='default', null=True, upload_to='', verbose_name='Add Photo for Article'),
        ),
    ]
