# Generated by Django 4.0.5 on 2022-08-02 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GroupApp', '0003_content_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheet',
            name='type',
            field=models.CharField(default=12, max_length=10),
            preserve_default=False,
        ),
    ]
