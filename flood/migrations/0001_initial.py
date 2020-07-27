# Generated by Django 3.0.7 on 2020-07-25 04:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('is_volunteer', models.BooleanField()),
                ('district', models.CharField(max_length=30, null=True)),
                ('areaofvol', models.CharField(max_length=40, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('is_staff', models.BooleanField(blank=True, default=False, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('heading', models.TextField(max_length=100)),
                ('content', models.TextField(max_length=350)),
                ('contactphn', models.CharField(max_length=10)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('creationtime', models.DateTimeField(auto_now_add=True)),
                ('isRequest', models.BooleanField(default=False)),
                ('isDonate', models.BooleanField(default=False)),
                ('isAnnouncement', models.BooleanField(default=False)),
                ('isFoodWater', models.BooleanField(default=False)),
                ('isToiletries', models.BooleanField(default=False)),
                ('isOther', models.BooleanField(default=False)),
                ('isRescue', models.BooleanField(default=False)),
                ('upvotes', models.ManyToManyField(blank=True, related_name='luserprofile', to=settings.AUTH_USER_MODEL)),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]