# Generated by Django 4.2 on 2023-06-20 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_account_delete_foydalanuvchi'),
        ('buyurtma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manzil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('davlat', models.CharField(choices=[('Uzbekistan', 'Uzbekistan'), ('Russia', 'Russia'), ('Armenia', 'Armenia'), ('Tajikistan', 'Tajikistan'), ('Kazakhstan', 'Kazakhstan'), ('Kyrgzstan', 'Kyrgzstan'), ('Azerbayjan', 'Azerbayjan'), ('Moldova', 'Moldova'), ('Latviya', 'Latviya'), ('Turkmenistan', 'Turkmenistan')], max_length=50)),
                ('shahar', models.CharField(max_length=70)),
                ('manzil', models.CharField(max_length=70)),
                ('zipcode', models.CharField(max_length=6)),
                ('asosiy', models.BooleanField(default=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.account')),
            ],
        ),
        migrations.CreateModel(
            name='Buyurtma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.DateField(auto_now_add=True)),
                ('holat', models.CharField(max_length=50)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.account')),
                ('manzil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyurtma.manzil')),
                ('savat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyurtma.savat')),
            ],
        ),
    ]