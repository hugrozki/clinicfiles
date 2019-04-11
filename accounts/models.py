from django.db import models

BLOOD_TYPE_CHOICES = (
    ('O-', 'O-'),
    ('O+', 'O+'),
    ('A-', 'A-'),
    ('A+', 'A+'),
    ('B-', 'B-'),
    ('B+', 'B+'),
    ('AB-', 'AB-'),
    ('AB+', 'AB+'),
)

class Account(models.Model):
    name = models.CharField(verbose_name='Nombre de usuario', max_length=50)
    no_expediente = models.IntegerField(verbose_name='Número de expediente', unique=True)
    fecha_ultima_consulta = models.DateField(verbose_name='Fecha de última consulta')
    tipo_sangre = models.CharField(
        verbose_name='Tipo de sangre',
        max_length=3,
        choices=BLOOD_TYPE_CHOICES,
    )

    def __str__(self):
        return self.name

class Allergy(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=50)
    fecha_alta = models.DateField(verbose_name='Fecha de alta')
    medicamento = models.CharField(verbose_name='Medicamento', max_length=50)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='alergias')

    def __str__(self):
        return '{}, {}'.format(self.nombre, self.medicamento)