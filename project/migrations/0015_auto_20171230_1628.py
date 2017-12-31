# Generated by Django 2.0 on 2017-12-30 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_group_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='deadline',
            field=models.CharField(max_length=20, verbose_name='Срок сдачи'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.CharField(max_length=64, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='kurator',
            field=models.CharField(max_length=64, verbose_name='Куратор'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Название'),
        ),
    ]
