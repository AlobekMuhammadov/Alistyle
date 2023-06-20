# Generated by Django 4.2 on 2023-06-13 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0005_mahsulot_mavjud_mahsulot_yetkazish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mahsulot',
            name='rasm',
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.FileField(upload_to='mahsulotlar')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mahsulot')),
            ],
        ),
    ]