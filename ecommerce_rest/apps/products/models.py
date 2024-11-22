from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords


class MeasureUnit(BaseModel):
    """Model definition for MeasureUnit."""

    # TODO: Define fields here
    description = models.CharField('Descripción', max_length=50,blank=False,null=False, unique=True)
    historical= HistoricalRecords()

    #property sirve para que la funcion se llame sola 
    # primero corremos history user que guarda que usuario altero este objeto(measureunit)
    @property
    def _history_user(self):
        return self.changed_by
    #esta funcion le otorga una valor a este changed_by con el valor que cambio 
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by=value

    class Meta:
        """Meta definition for MeasureUnit."""

        verbose_name =  'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medida'

    def __str__(self):
        """Unicode representation of MeasureUnit."""
        return self.description
    
class CategoryProduct(BaseModel):
    """Model definition for CategoryProduct."""

    # TODO: Define fields here
    description = models.CharField('Descripción', max_length=50,unique=True,null=False,blank=False)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de Medida')
    historical= HistoricalRecords()

    #property sirve para que la funcion se llame sola 
    # primero corremos history user que guarda que usuario altero este objeto(measureunit)
    @property
    def _history_user(self):
        return self.changed_by
    #esta funcion le otorga una valor a este changed_by con el valor que cambio 
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by=value

    class Meta:
        """Meta definition for CategoryProduct."""

        verbose_name = 'Categoria de Producto'
        verbose_name_plural = 'Categorias de Producto'

    def __str__(self):
        """Unicode representation of CategoryProduct."""
        return self.description

class Indicator(BaseModel):
    """Model definition for Indicador."""

    # TODO: Define fields here
    descount_value = models.PositiveIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Indicador de Oferta')
    historical= HistoricalRecords()

    #property sirve para que la funcion se llame sola 
    # primero corremos history user que guarda que usuario altero este objeto(measureunit)
    @property
    def _history_user(self):
        return self.changed_by
    #esta funcion le otorga una valor a este changed_by con el valor que cambio 
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by=value
    

    class Meta:
        """Meta definition for Indicador."""

        verbose_name = 'Indicador de Oferta'
        verbose_name_plural = 'Indicadores de Ofertas'

    def __str__(self):
        """Unicode representation of Indicador."""
        return f'Oferta de la categoria {self.category_product} : {self.descount_value}%'

class Product(BaseModel):
    """Model definition for Product."""

    # TODO: Define fields here
    name = models.CharField('Nombre de Producto', max_length=150,unique=True,blank=False,null=False)
    description = models.TextField('Descripcion de Producto',blank=False,null=False)
    image = models.ImageField('Imagen del Producto', upload_to='products/',blank=True,null=True)
    historical= HistoricalRecords()

    #property sirve para que la funcion se llame sola 
    # primero corremos history user que guarda que usuario altero este objeto(measureunit)
    @property
    def _history_user(self):
        return self.changed_by
    #esta funcion le otorga una valor a este changed_by con el valor que cambio 
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by=value

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name


