# Generated by Django 3.2.16 on 2023-08-23 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_uploadedimage_stage2'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('video_url', models.URLField()),
                ('transcript_score', models.FloatField(blank=True, null=True)),
                ('comments_score', models.FloatField(blank=True, null=True)),
                ('description_score', models.FloatField(blank=True, null=True)),
                ('about_score', models.FloatField(blank=True, null=True)),
                ('overall_score', models.FloatField(blank=True, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='UploadedImage',
        ),
    ]