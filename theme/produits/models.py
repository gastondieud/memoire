from django.db import models

# Create your models here.
class categories (models.Model):
    nom = models.CharField(max_length=200)
    def __str__(self):
        return self.nom

class types (models.Model):
    nom = models.CharField(max_length=200)
    def __str__(self):
        return self.nom

class dimensions (models.Model):
    nom = models.CharField(max_length=200)
    def __str__(self):
        return self.nom


class matelas (models.Model):
    categorie = models.ForeignKey(categories,on_delete=models.CASCADE)
    prix = models.FloatField(default=0)
    type = models.ForeignKey(types,on_delete=models.CASCADE)
    dimension = models.ForeignKey(dimensions,on_delete=models.CASCADE)
    def __str__(self):
            return f" {self.categorie} de { self.type}"

