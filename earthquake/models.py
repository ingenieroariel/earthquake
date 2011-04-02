from django.contrib.gis.db import models


class RoofType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)   

    def __unicode__(self):
        return self.name

class PrimaryStructuralSystem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class SecondaryStructuralSystem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

class HeightType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

class BuildingType(models.Model):
    primary_structural_system = models.ForeignKey(PrimaryStructuralSystem)
    secondary_structural_system = models.ForeignKey(SecondaryStructuralSystem, blank=True, null=True)
    roof_type = models.ForeignKey(RoofType, blank=True, null=True)
    height_type = models.ForeignKey(HeightType, blank=True, null=True)

    def __unicode__(self):
        return '%s - %s - %s' % (
                                self.primary_structural_system or '(*)',
                                self.secondary_structural_system or '(*)',
                                self.roof_type or '(*)'
                               )

CONFIDENCE_CHOICES = (('1','1'), ('2', '2'),('3', '3'),('4', '4'))

class VulnerabilityFunction(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    confidence = models.CharField(max_length=1, choices = CONFIDENCE_CHOICES, default ='1')

    def __unicode__(self):
        return self.name


class Curve(models.Model):
    building_type = models.ForeignKey(BuildingType)
    points = models.TextField(help_text=r"""For example: [[-MAXFLOAT, 0.0],
                                                     [0.0, 0.016],
                                                     [0.1, 0.169],
                                                     [0.3, 0.445],
                                                     [0.5, 0.472],
                                                     [1.0, 0.618],
                                                     [1.5, 0.629],
                                                     [2.0, 0.633],
                                                     [2.5, 0.694],
                                                     [MAXFLOAT, 69.4]]""")
    vulnerability_function = models.ForeignKey(VulnerabilityFunction)

    def __unicode__(self):
        return '%s in %s' (self.building_type, self.area)
