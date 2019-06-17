# Generated by Django 2.2.2 on 2019-06-17 14:30

import blog.models
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
            name='ACER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(db_index=True, upload_to=blog.models.media)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('title', models.CharField(db_index=True, max_length=30)),
                ('touch', models.CharField(blank=True, db_index=True, max_length=30)),
                ('weight', models.CharField(db_index=True, max_length=30)),
                ('memory', models.CharField(db_index=True, max_length=30)),
                ('onnect', models.CharField(db_index=True, max_length=30)),
                ('thickness', models.CharField(db_index=True, max_length=30)),
                ('ssd', models.CharField(db_index=True, max_length=30)),
                ('decimal', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Apple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(db_index=True, upload_to=blog.models.media)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('title', models.CharField(db_index=True, max_length=30)),
                ('connect', models.CharField(db_index=True, max_length=30)),
                ('memory', models.CharField(db_index=True, max_length=30)),
                ('camera', models.CharField(db_index=True, max_length=30)),
                ('decimal', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='ASUS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(db_index=True, upload_to=blog.models.media)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('title', models.CharField(db_index=True, max_length=30)),
                ('touch', models.CharField(blank=True, db_index=True, max_length=30)),
                ('weight', models.CharField(db_index=True, max_length=30)),
                ('memory', models.CharField(db_index=True, max_length=30)),
                ('onnect', models.CharField(db_index=True, max_length=30)),
                ('thickness', models.CharField(blank=True, db_index=True, max_length=30)),
                ('ssd', models.CharField(db_index=True, max_length=30)),
                ('decimal', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(db_index=True, upload_to=blog.models.media)),
            ],
        ),
        migrations.CreateModel(
            name='Category_a_laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('catalog', models.ManyToManyField(blank=True, related_name='a_laptop_catalog', to='blog.Catalog')),
                ('catalogs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Catalog')),
            ],
        ),
        migrations.CreateModel(
            name='Category_Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('catalog', models.ManyToManyField(blank=True, related_name='phone_catalog', to='blog.Catalog')),
                ('catalogs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Catalog')),
            ],
        ),
        migrations.CreateModel(
            name='Category_TV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('catalog', models.ManyToManyField(blank=True, related_name='tv_catalog', to='blog.Catalog')),
                ('catalogs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Catalog')),
            ],
        ),
        migrations.CreateModel(
            name='LG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(db_index=True, upload_to=blog.models.media)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('title', models.CharField(db_index=True, max_length=30)),
                ('screen', models.CharField(db_index=True, max_length=30)),
                ('connect', models.CharField(db_index=True, max_length=30)),
                ('size', models.CharField(db_index=True, max_length=30)),
                ('decimal', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('catalog', models.ManyToManyField(blank=True, related_name='lg_tv_catalog', to='blog.Catalog')),
                ('catalogs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Catalog')),
                ('category_tv', models.ManyToManyField(blank=True, related_name='lg_tv', to='blog.Category_TV')),
                ('lgs_tv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category_TV')),
            ],
        ),
        migrations.CreateModel(
            name='Mac_OS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(db_index=True, upload_to=blog.models.media)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('title', models.CharField(db_index=True, max_length=30)),
                ('touch', models.CharField(blank=True, db_index=True, max_length=30)),
                ('weight', models.CharField(db_index=True, max_length=30)),
                ('memory', models.CharField(db_index=True, max_length=30)),
                ('onnect', models.CharField(db_index=True, max_length=30)),
                ('thickness', models.CharField(db_index=True, max_length=30)),
                ('ssd', models.CharField(db_index=True, max_length=30)),
                ('decimal', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('catalog', models.ManyToManyField(blank=True, related_name='mac_os_a_laptop_catalog', to='blog.Catalog')),
                ('catalogs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Catalog')),
                ('category_a_laptop', models.ManyToManyField(blank=True, related_name='mac_os_a_laptop', to='blog.Category_a_laptop')),
                ('mac_a_laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category_a_laptop')),
            ],
        ),
        migrations.CreateModel(
            name='Xiaomi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(db_index=True, upload_to=blog.models.media)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('title', models.CharField(db_index=True, max_length=30)),
                ('onnect', models.CharField(db_index=True, max_length=30)),
                ('memory', models.CharField(db_index=True, max_length=30)),
                ('camera', models.CharField(db_index=True, max_length=30)),
                ('decimal', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('catalog', models.ManyToManyField(blank=True, related_name='xiaomi_phone_catalog', to='blog.Catalog')),
                ('catalogs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Catalog')),
                ('category_phone', models.ManyToManyField(blank=True, related_name='xiaomi_phone', to='blog.Category_Phone')),
                ('xiaomi_phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category_Phone')),
            ],
        ),
        migrations.CreateModel(
            name='Sony',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(db_index=True, upload_to=blog.models.media)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('title', models.CharField(db_index=True, max_length=30)),
                ('screen', models.CharField(db_index=True, max_length=30)),
                ('connect', models.CharField(db_index=True, max_length=30)),
                ('size', models.CharField(db_index=True, max_length=30)),
                ('decimal', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('catalog', models.ManyToManyField(blank=True, related_name='sony_tv_catalog', to='blog.Catalog')),
                ('catalogs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Catalog')),
                ('category_tv', models.ManyToManyField(blank=True, related_name='sony_tv', to='blog.Category_TV')),
                ('sonys_tv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category_TV')),
            ],
        ),
        migrations.CreateModel(
            name='Samsung_TV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(db_index=True, upload_to=blog.models.media)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('title', models.CharField(db_index=True, max_length=30)),
                ('screen', models.CharField(db_index=True, max_length=30)),
                ('connect', models.CharField(db_index=True, max_length=30)),
                ('size', models.CharField(db_index=True, max_length=30)),
                ('decimal', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('catalog', models.ManyToManyField(blank=True, related_name='samsung_tv_tv_catalog', to='blog.Catalog')),
                ('catalogs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Catalog')),
                ('category_tv', models.ManyToManyField(blank=True, related_name='samsung_tv_tv', to='blog.Category_TV')),
                ('samsungs_tv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category_TV')),
            ],
        ),
        migrations.CreateModel(
            name='Samsung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(db_index=True, upload_to=blog.models.media)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('title', models.CharField(db_index=True, max_length=30)),
                ('camera', models.CharField(db_index=True, max_length=30)),
                ('memory', models.CharField(db_index=True, max_length=30)),
                ('connect', models.CharField(db_index=True, max_length=30)),
                ('decimal', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('catalog', models.ManyToManyField(blank=True, related_name='samsung_phone_catalog', to='blog.Catalog')),
                ('catalogs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Catalog')),
                ('category_phone', models.ManyToManyField(blank=True, related_name='samsung_phone', to='blog.Category_Phone')),
                ('samsung_phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category_Phone')),
            ],
        ),
        migrations.CreateModel(
            name='Panasonic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(db_index=True, upload_to=blog.models.media)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('title', models.CharField(db_index=True, max_length=30)),
                ('screen', models.CharField(db_index=True, max_length=30)),
                ('connect', models.CharField(db_index=True, max_length=30)),
                ('size', models.CharField(db_index=True, max_length=30)),
                ('decimal', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('catalog', models.ManyToManyField(blank=True, related_name='panasonic_tv_catalog', to='blog.Catalog')),
                ('catalogs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Catalog')),
                ('category_tv', models.ManyToManyField(blank=True, related_name='panasonic_tv', to='blog.Category_TV')),
                ('panasonic_tv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category_TV')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('integer', models.IntegerField(default=1)),
                ('acer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.ACER')),
                ('apple', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Apple')),
                ('asus', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.ASUS')),
                ('lg', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.LG')),
                ('mac_os', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Mac_OS')),
                ('panasonic', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Panasonic')),
                ('samsung', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Samsung')),
                ('sony', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Sony')),
                ('xiaomi', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Xiaomi')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(to='blog.OrderItem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='asus',
            name='asus_a_laptop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category_a_laptop'),
        ),
        migrations.AddField(
            model_name='asus',
            name='catalog',
            field=models.ManyToManyField(blank=True, related_name='asus_a_laptop_catalog', to='blog.Catalog'),
        ),
        migrations.AddField(
            model_name='asus',
            name='catalogs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Catalog'),
        ),
        migrations.AddField(
            model_name='asus',
            name='category_a_laptop',
            field=models.ManyToManyField(blank=True, related_name='asus_a_laptop', to='blog.Category_a_laptop'),
        ),
        migrations.AddField(
            model_name='apple',
            name='apple_phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category_Phone'),
        ),
        migrations.AddField(
            model_name='apple',
            name='catalog',
            field=models.ManyToManyField(blank=True, related_name='apple_phone_catalog', to='blog.Catalog'),
        ),
        migrations.AddField(
            model_name='apple',
            name='catalogs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Catalog'),
        ),
        migrations.AddField(
            model_name='apple',
            name='category_phone',
            field=models.ManyToManyField(blank=True, related_name='apple_phone', to='blog.Category_Phone'),
        ),
        migrations.AddField(
            model_name='acer',
            name='acer_a_laptop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category_a_laptop'),
        ),
        migrations.AddField(
            model_name='acer',
            name='catalog',
            field=models.ManyToManyField(blank=True, related_name='acer_a_laptop_catalog', to='blog.Catalog'),
        ),
        migrations.AddField(
            model_name='acer',
            name='catalogs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Catalog'),
        ),
        migrations.AddField(
            model_name='acer',
            name='category_a_laptop',
            field=models.ManyToManyField(blank=True, related_name='acer_a_laptop', to='blog.Category_a_laptop'),
        ),
    ]
