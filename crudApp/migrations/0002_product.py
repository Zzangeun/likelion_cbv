# Generated by Django 2.2.4 on 2019-10-06 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='crudApp.Post')),
                ('price', models.IntegerField()),
            ],
            bases=('crudApp.post',),
        ),
    ]
