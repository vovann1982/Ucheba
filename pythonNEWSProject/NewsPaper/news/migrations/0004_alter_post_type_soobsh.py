# Generated by Django 4.0.4 on 2022-04-22 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_post_zagolovok'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type_soobsh',
            field=models.CharField(choices=[('NW', 'Новость'), ('AR', 'Статья')], default='NW', max_length=2),
        ),
    ]