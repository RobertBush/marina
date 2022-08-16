from django.db import models


class Boat(models.Model):
    manufacturer = models.CharField(max_length=200)
    hull_number = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    model_year = models.IntegerField()
    custom_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    engines = models.ManyToManyField(
        "Engine", blank=True, through="BoatEngine", related_name="boats"
    )

    def __str__(self):
        return f"{self.model_year} {self.manufacturer} {self.model_name} - {self.price}"


class Engine(models.Model):
    manufacturer = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    model_year = models.IntegerField()
    custom_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    hours_of_operation = models.IntegerField()

    def __str__(self):
        return f"{self.model_year} {self.manufacturer} {self.model_name} - {self.price}"


class BoatEngine(models.Model):
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE)
    date_attached = models.DateField(blank=True, null=True)
    date_removed = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = (
            "boat",
            "engine",
            "date_attached",
        )

    def __str__(self):
        return f"{self.boat} with {self.engine}"
