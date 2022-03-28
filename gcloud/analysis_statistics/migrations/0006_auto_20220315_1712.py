# Generated by Django 2.2.26 on 2022-03-15 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analysis_statistics", "0005_auto_20220315_1126"),
    ]

    operations = [
        migrations.CreateModel(
            name="TemplateCustomVariableSummary",
            fields=[
                (
                    "variable_type",
                    models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name="变量类型"),
                ),
                ("task_template_refs", models.IntegerField(verbose_name="使用该变量的项目流程数量")),
                ("common_template_refs", models.IntegerField(verbose_name="使用该变量的公共流程数量")),
            ],
            options={
                "verbose_name": "流程模板变量统计数据总览",
                "verbose_name_plural": "流程模板变量统计数据总览",
            },
        ),
        migrations.AlterModelOptions(
            name="templatevariablestatistics",
            options={"verbose_name": "流程模板变量统计数据", "verbose_name_plural": "流程模板变量统计数据"},
        ),
    ]
