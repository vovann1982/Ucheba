# Generated by Django 4.0.4 on 2022-04-21 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_category_options_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='zagolovok',
            field=models.CharField(max_length=64),
        ),
    ]
