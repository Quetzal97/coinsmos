# Generated by Django 3.1.3 on 2021-01-18 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210117_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Borrador'), (1, 'Publicacion')], default=0),
        ),
    ]
