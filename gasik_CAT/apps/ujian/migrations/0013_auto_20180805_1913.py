# Generated by Django 2.0.7 on 2018-08-05 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ujian', '0012_auto_20180804_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jawabansoal',
            name='teks_jawaban',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='soalujian',
            name='teks_soal',
            field=models.TextField(),
        ),
    ]