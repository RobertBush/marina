# Generated by Django 4.1 on 2022-08-16 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Boat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("manufacturer", models.CharField(max_length=200)),
                ("hull_number", models.CharField(max_length=200)),
                ("model_name", models.CharField(max_length=200)),
                ("model_year", models.IntegerField()),
                ("custom_description", models.TextField(blank=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name="Engine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("manufacturer", models.CharField(max_length=200)),
                ("serial_number", models.CharField(max_length=200)),
                ("model_name", models.CharField(max_length=200)),
                ("model_year", models.IntegerField()),
                ("custom_description", models.TextField(blank=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=12)),
                ("hours_of_operation", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="BoatEngine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_attached", models.DateField(blank=True, null=True)),
                ("date_removed", models.DateField(blank=True, null=True)),
                (
                    "boat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="power.boat"
                    ),
                ),
                (
                    "engine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="power.engine"
                    ),
                ),
            ],
            options={
                "unique_together": {("boat", "engine", "date_attached")},
            },
        ),
        migrations.AddField(
            model_name="boat",
            name="engines",
            field=models.ManyToManyField(
                blank=True,
                related_name="boats",
                through="power.BoatEngine",
                to="power.engine",
            ),
        ),
    ]
