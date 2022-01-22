# Generated by Django 4.0.1 on 2022-01-22 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="prescription", name="laboratoryTestId",),
        migrations.CreateModel(
            name="LabTestPrescriptionMap",
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
                (
                    "laboratoryTestId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="doctor.laboratorytest",
                    ),
                ),
                (
                    "prescriptionId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="doctor.prescription",
                    ),
                ),
            ],
        ),
    ]
