# Generated by Django 5.0.3 on 2024-03-19 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0002_alter_comment_name_alter_comment_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='descr',
            field=models.TextField(default=None),
        ),
    ]
