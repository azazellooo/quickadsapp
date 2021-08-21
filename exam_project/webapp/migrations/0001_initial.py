# Generated by Django 3.2.6 on 2021-08-21 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='pictures')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(blank=True, max_length=3000, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('is_moderated', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advert', to='accounts.profile')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advert', to='webapp.category')),
            ],
        ),
    ]
