# Generated by Django 3.1.3 on 2021-01-20 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_post_destacado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='body',
            new_name='comentario',
        ),
        migrations.RenameField(
            model_name='comentario',
            old_name='name',
            new_name='nombre',
        ),
    ]
