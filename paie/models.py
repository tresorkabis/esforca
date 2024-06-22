from django.db import models

# Create your models here.
class Section(models.Model):
    code = models.CharField(max_length=10)
    libelle = models.CharField(max_length=50)

    def __str__(self):
        return self.code

class Promotion(models.Model):
    code = models.CharField(max_length=10)
    libelle = models.CharField(max_length=50)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.code + " - " + self.section.code