# Generated by Django 3.0.3 on 2020-05-31 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'Total',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='institution',
            fields=[
                ('institution_number', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('howtogo', models.CharField(max_length=20)),
                ('quiz1', models.CharField(max_length=50)),
                ('quiz2', models.CharField(max_length=50)),
                ('quiz3', models.CharField(max_length=50)),
                ('latitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['institution_number'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompleteState', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stampStatus', models.BooleanField(default=False)),
                ('create_Stamp_date', models.DateField(null=True)),
                ('create_Stamp_time', models.TimeField(null=True)),
                ('quiz1_answer', models.CharField(default=' ', max_length=50)),
                ('quiz2_answer', models.CharField(default=' ', max_length=50)),
                ('quiz3_answer', models.CharField(default=' ', max_length=50)),
                ('modify_date', models.DateField(auto_now=True)),
                ('Watch_Student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Museum.Student')),
                ('Watch_institution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Museum.institution')),
            ],
            options={
                'ordering': ['modify_date'],
            },
        ),
        migrations.CreateModel(
            name='Comunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Museum.Student')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
