# Generated by Django 3.1 on 2020-09-03 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('master', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='article',
            old_name='created_At',
            new_name='created_at',
        ),
    ]