# Generated by Django 4.1.6 on 2023-03-30 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_user_first_name_alter_user_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='link',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True),
        ),
    ]
