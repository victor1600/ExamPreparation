from django.db import models


# Create your models here.
class CommonFields(models.Model):
    nombre = models.CharField(max_length=200)
    status = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        abstract = True


class Facultad(CommonFields):
    pass


class Escuela(CommonFields):
    facultad = models.ForeignKey(Facultad, on_delete=models.PROTECT)


class Ciclo(CommonFields):
    pass


class Materia(CommonFields):
    escuela = models.ForeignKey(Escuela, on_delete=models.PROTECT)
    ciclo = models.ForeignKey(Ciclo, on_delete=models.PROTECT)
