from django.db import models

# Create your models here.
class Bordereaux(models.Model):
	pay_ctr = models.CharField(max_length=20)
	n_brd = models.CharField(unique=True, max_length=200)
	dt_clo = models.DateField()
	n_ord = models.IntegerField()
	m_brd = models.DecimalField(decimal_places=2, max_digits=8)
	dt_depot = models.DateField(null=True, blank=True)
	dt_jrl = models.DateField(null=True, blank=True)
	n_ord_jrl = models.IntegerField( null=True, blank=True, default=0)
	m_jrl = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True, default=0)
	dt_pay = models.DateField( null=True, blank=True)
	defr = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True, default=0)
	def_o = models.IntegerField(default=0)
	payement = models.BooleanField(default=False)