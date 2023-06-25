# Generated by Django 4.1.6 on 2023-06-25 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department_app', '0001_initial'),
        ('employee_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='works_for',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to='department_app.department'),
        ),
    ]
