# Generated by Django 2.1 on 2019-04-23 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.BigIntegerField(default='01000000000', null=True)),
                ('picture', models.ImageField(default='avatars/avatar.png', null=True, upload_to='avatars/')),
                ('birthday', models.DateField(default=django.utils.timezone.now, null=True)),
                ('facebook', models.URLField(default='www.facebook.com', null=True)),
                ('country', models.CharField(default='Egypt', max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
