# Generated by Django 3.1.3 on 2021-01-20 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20210120_1224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='comment',
            new_name='body',
        ),
    ]
