from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import math

# Create your models here.

class GLObject(models.Model):
    """
    Represents a GLObject in the database.

    Attributes:
        gl_name (str): The name of the GLObject.
        gl_alpha (Decimal): The alpha coordinate of the GLObject in degrees.
        gl_delta (Decimal): The delta coordinate of the GLObject in degrees.
        l_redshift (Decimal): The redshift of the GLObject for the lens.
        q_redshift (Decimal): The redshift of the GLObject for the quasar.
        ang_sep (Decimal): The angular separation between the lens and the quasar.
        time_delay (Decimal): The time delay between the lens and the quasar in days.
        gl_url (str): The URL associated with the GLObject.
        gl_image (ImageField): The image associated with the GLObject.

    Methods:
        c_count(): Returns the count of GLComponents that are quasars.
        max_sep(): Returns the maximum separation between quasars in the GLObject.
        gl_ra(): Returns the right ascension of the GLObject in HH:MM:SS format.
        gl_dec(): Returns the declination of the GLObject in DD:MM:SS format.
        max_mag(): Returns the maximum magnitude of the GLObject for the quasars.
        min_mag(): Returns the minimum magnitude of the GLObject for the quasars.
        gal_mag(): Returns the magnitude of the GLObject for non-quasars.
    """

    gl_name = models.CharField(max_length=30)
    gl_alpha = models.DecimalField(max_digits=8, decimal_places=5, default=0.0)
    gl_delta = models.DecimalField(max_digits=8, decimal_places=5, default=0.0)
    l_redshift = models.DecimalField(max_digits=5, decimal_places=3, default=0.0)
    q_redshift = models.DecimalField(max_digits=5, decimal_places=3, default=0.0)
    ang_sep = models.DecimalField(max_digits=5, decimal_places=3, default=0.0)
    time_delay = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    gl_url = models.URLField(max_length=200, blank=True)
    gl_image = models.ImageField(blank=True)

    def c_count(self):
        # Implementation omitted for brevity
        pass
    
    def max_sep(self):
        # Implementation omitted for brevity
        pass

    def gl_ra(self):
        # Implementation omitted for brevity
        pass

    def gl_dec(self):
        # Implementation omitted for brevity
        pass

    def max_mag(self):
        # Implementation omitted for brevity
        pass

    def min_mag(self):
        # Implementation omitted for brevity
        pass

    def gal_mag(self):
        # Implementation omitted for brevity
        pass

    def __str__(self):
        return self.gl_name

    class Meta:
        ordering = ["gl_alpha"]


class GLComponent(models.Model):
    """
    Represents a component of a GLObject in the database.

    Attributes:
        c_name (str): The name of the component.
        c_alpha (Decimal): The alpha coordinate in angular seconds.
        c_alpha_err (Decimal): The error in the alpha coordinate.
        c_delta (Decimal): The delta coordinate in angular seconds.
        c_delta_err (Decimal): The error in the delta coordinate.
        is_quasar (bool): Indicates whether the component is a quasar.
        globject (GLObject): The GLObject that the component belongs to.
    """

    c_name = models.CharField(max_length=3, default="A")
    c_alpha = models.DecimalField(max_digits=5, decimal_places=3, default=0.0)
    c_alpha_err = models.DecimalField(max_digits=4, decimal_places=3, default=0.0)
    c_delta = models.DecimalField(max_digits=5, decimal_places=3, default=0.0)
    c_delta_err = models.DecimalField(max_digits=4, decimal_places=3, default=0.0)
    is_quasar = models.BooleanField(default=True)
    globject = models.ForeignKey(GLObject, on_delete=models.CASCADE, null=True)

    def __str__(self):
        """
        Returns a string representation of the GLComponent.

        Returns:
            str: The name of the component.
        """
        return self.c_name

class Magnitude(models.Model):
    """
    Represents a magnitude measurement of a celestial object.
    
    Attributes:
        m_band (str): The band in which the magnitude is measured.
        m_value (Decimal): The value of the magnitude.
        m_value_err (Decimal): The error associated with the magnitude value.
        m_date (Date): The date of the observation.
        glcomponent (GLComponent): The GLComponent to which this magnitude measurement belongs.
    """
    m_band = models.CharField(max_length=10, default="r")
    m_value = models.DecimalField(max_digits=5, decimal_places=3, default=0.0)
    m_value_err = models.DecimalField(max_digits=4, decimal_places=3, default=0.0)
    m_date = models.DateField('observation date', blank=True, null=True)
    glcomponent = models.ForeignKey(GLComponent, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.m_band
