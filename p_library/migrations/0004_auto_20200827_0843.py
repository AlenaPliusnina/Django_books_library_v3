# Generated by Django 2.2.6 on 2020-08-27 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_auto_20200827_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='copy_count',
            field=models.SmallIntegerField(default=1),
        ),
    ]
