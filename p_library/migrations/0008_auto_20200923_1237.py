# Generated by Django 2.2.6 on 2020-09-23 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0007_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Book'),
        ),
    ]
