# Generated by Django 4.1.6 on 2023-06-25 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0002_employee_works_for'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dependent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('sex', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=12, null=True)),
                ('birth_date', models.DateField()),
                ('relaationship', models.CharField(max_length=50)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dependents', to='employee_app.employee')),
            ],
        ),
    ]