# Generated by Django 3.1.7 on 2021-03-15 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_isdraft'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='isDraft',
            new_name='is_draft',
        ),
    ]
