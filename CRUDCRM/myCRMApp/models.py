from django.db import models

class ShipRecords(models.Model):
    
    DateCreated = models.DateTimeField(auto_now_add=True)

    ShipName = models.CharField(max_length=200)

    ShipCurrentCaptain = models.CharField(max_length=100)

    ShipEmail = models.CharField(max_length=100)

    ShipMobile  = models.CharField(max_length=100)

    ShipOriginCountry = models.CharField(max_length=100)

    ShipOriginPort = models.CharField(max_length=200)

    ShipSize = models.CharField(max_length=100)

    ShipTotalIncident = models.IntegerField(blank=True, null=True)

    ShipLastServiceDate = models.DateField()

    ShipCarbonEmission = models.IntegerField(blank=True, null=True)

    def __str__(self):

        return self.ShipName + " " + self.ShipOriginPort

    

    


