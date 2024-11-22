from django.db import models

class BaseModel(models.Model):
    """Model definition fos BaseModel."""

    # TODO: Define fields here
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('Estado',default=True)
    created_date = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Fecha de Modificación', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Fecha de Eliminación', auto_now=True, auto_now_add=False)


    class Meta:
        """Meta definition fos BaseModel."""
        #al colocar esto, decimos que es abstracto, osea que no crea una base de datos para este modelo, solo sirve como plantilla
        # por ende no es obligatorio poner el __str__
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural ='Modelos Base'

