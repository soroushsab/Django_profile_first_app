# Generated by Django 4.1 on 2022-09-03 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Firstname', models.CharField(max_length=150)),
                ('Lastname', models.CharField(max_length=150)),
                ('Contactnumber', models.CharField(max_length=11)),
                ('Email', models.URLField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Firstname', models.CharField(max_length=150)),
                ('Lastname', models.CharField(max_length=150)),
                ('Contactnumber', models.CharField(max_length=11)),
                ('Email', models.URLField()),
                ('LinkedIn', models.URLField()),
                ('GitHub', models.URLField()),
                ('Profile_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Educations',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Level', models.CharField(max_length=255)),
                ('Education_description', models.TextField()),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Role', models.CharField(max_length=255)),
                ('Experience_description', models.TextField()),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
            ],
        ),
    ]