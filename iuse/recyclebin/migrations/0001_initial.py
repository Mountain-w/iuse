# Generated by Django 3.1.3 on 2022-03-29 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Garbage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('source', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sources.source')),
            ],
        ),
    ]
