from django.contrib.auth.models import Permission, User
from django.db import models

from django.core.urlresolvers import reverse


class Cars(models.Model):
    """ Table - car details """

    DOOR_NUMBER_CHOICES = (
        (3, '3 drzwiowy'),
        (4, '4 drzwiowy'),
        (5, '5 drzwiowy'),
        (6, '6 drzwiowy')
    )

    FUEL_TYPES_CHOICES = (
        (1, 'Benzyna'),
        (2, 'Benzyna + LPG'),
        (3, 'Benzyna + CNG'),
        (4, 'Diesel'),
        (5, 'Elektryczny'),
        (6, 'Etanol'),
        (7, 'Hybryda'),
        (8, 'Wodór')
    )

    car_id = models.AutoField(primary_key=True)
    brand_id = models.ForeignKey('Brands')
    capacity_id = models.ForeignKey('Capacities')
    color_id = models.ForeignKey('Colors')
    fuel_type = models.CharField(max_length=1, choices=FUEL_TYPES_CHOICES, default=1, blank=False)
    car_vin = models.CharField(max_length=17, unique=True, blank=False)
    car_registration = models.CharField(max_length=7, unique=True, blank=False)
    door_number = models.CharField(max_length=1, choices=DOOR_NUMBER_CHOICES, default=3, blank=False)
    car_production = models.DateField(blank=False)
    car_next_inspection = models.DateField(blank=False)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)


class Capacities(models.Model):
    """ Dictionary table - car engine capacities """
    capacity_id = models.AutoField(primary_key=True)
    capacity_value = models.PositiveIntegerField(unique=True, blank=False)
    capacity_short = models.FloatField()

    def __str__(self):
        return self.capacity_value

  #  def get_absolute_url(self):
   #     return reverse('cars:capacity-detail', kwargs={'pk': self})


class Colors(models.Model):
    """ Dictionary table - car colors """
    color_id = models.AutoField(primary_key=True)
    color_name = models.CharField(max_length=32, unique=True, blank=False)
    color_code = models.CharField(max_length=8, unique=True, blank=False)


class Services(models.Model):
    """ Dictionary table services """
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=164, unique=True, blank=False)


class Producers(models.Model):
    """ Dictionary table - car producers """
    producer_id = models.AutoField(primary_key=True)
    producer_name = models.CharField(max_length=32, unique=True, blank=False)


class Brands(models.Model):
    """ Dictionary table - car brands """
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=45, unique=True, blank=False)
    producer_id = models.ForeignKey('Producers', on_delete=models.CASCADE)


class CarServices(models.Model):
    """ Table - car services history """
    car_service_id = models.AutoField(primary_key=True)
    service_id = models.ForeignKey('Services', on_delete=models.CASCADE)
    car_id = models.ForeignKey('Cars', on_delete=models.CASCADE)
    invoice_id = models.PositiveIntegerField(blank=False)
    car_millage = models.PositiveIntegerField(blank=False)
    service_description = models.TextField(default='')
    service_cost = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    service_date = models.DateField(blank=False)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)


class Insurances(models.Model):
    """ Table - car insurance history """
    insurance_id = models.AutoField(primary_key=True)
    car_id = models.ForeignKey('Cars', on_delete=models.CASCADE)
    insurance_number = models.CharField(max_length=32, blank=False)
    insurante_start_date = models.DateField(blank=False)
    insurante_stop_date = models.DateField(blank=False)
    insurante_cost = models.DecimalField(max_digits=5, decimal_places=2, blank=False)


class CarRefuelings(models.Model):
    """ Table - car refueling history """
    refueling_id = models.AutoField(primary_key=True)
    car_id = models.ForeignKey('Cars', on_delete=models.CASCADE)
    invoice_id = models.PositiveIntegerField(blank=False)
    car_millage = models.PositiveIntegerField(blank=False)
    fuel_amount = models.DecimalField(max_digits=4, decimal_places=2, blank=False)
    fuel_cost = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    created_at = models.DateTimeField(auto_created=True)


class CarCars(models.Model):
    """ Table - car cards history """
    car_card_id = models.AutoField(primary_key=True)
    car_id = models.ForeignKey('Cars', on_delete=models.CASCADE),
    start_address = models.CharField(max_length=255, blank=False)
    destination_address = models.CharField(max_length=255, blank=False)
    distance = models.PositiveIntegerField()
    date_start = models.DateField()
    date_stop = models.DateField()
    created_at = models.DateTimeField(auto_created=True)
