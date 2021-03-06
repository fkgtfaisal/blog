# Generated by Django 4.0.4 on 2022-04-28 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0007_auto_20200926_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='book',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
