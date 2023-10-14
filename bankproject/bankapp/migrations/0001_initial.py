# Generated by Django 4.2.4 on 2023-10-13 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('dob', models.DateField(blank=True, null=True)),
                ('mail_id', models.EmailField(blank=True, max_length=254)),
                ('account', models.CharField(choices=[('saving', 'Saving Account'), ('current', 'Current Account'), ('business', 'Business Account'), ('student', 'Student Account')], max_length=255)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.area')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.branch')),
                ('materials', models.ManyToManyField(blank=True, to='bankapp.material')),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.branch'),
        ),
    ]