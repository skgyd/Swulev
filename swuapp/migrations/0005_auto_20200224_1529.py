# Generated by Django 3.0.3 on 2020-02-24 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swuapp', '0004_merge_20200224_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='swuapp.Student_User'),
        ),
    ]
