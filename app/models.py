from django.db import models

# Create your models here.
class Capital(models.Model):
   Capital_id=models.IntegerField(primary_key=True)
   Capitalname=models.CharField(max_length=100)
   def _str_(self) -> str:
       return self.Capitalname

class Country(models.Model):
    country_id=models.IntegerField(primary_key=True)
    countryname=models.CharField(max_length=100)
    capital_id=models.OneToOneField(Capital,on_delete=models.CASCADE)
    def _str_(self) -> str:
        return self.countryname
