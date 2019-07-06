# Generated by Django 2.2.3 on 2019-07-06 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(blank=True, choices=[('General', 'General'), ('Advance', 'Advance'), ('Professional', 'Professional')], max_length=200, null=True),
        ),
    ]
