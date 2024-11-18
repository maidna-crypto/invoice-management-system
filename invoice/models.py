from django.db import models


class InvoiceModel(models.Model):
    invoice_number = models.CharField(
        max_length=250, 
        unique=True,
    )
    customer_name = models.CharField(
        max_length=250, 
        null=True, 
        blank=True,
    )
    date = models.DateField(null=True, blank=True
    )
    
    class Meta:
        ordering = ['-date']
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'

    def __str__(self):
        return f"Invoice {self.invoice_number}"

class InvoiceDetailModel(models.Model):
    invoice = models.ForeignKey(
        InvoiceModel, 
        on_delete=models.CASCADE, 
        related_name='invoice_detail'
    )
    description = models.CharField(
        max_length=250, 
        null=True, 
        blank=True,
    )
    quantity = models.IntegerField(default=0
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )

    
    line_total = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
    )

    class Meta:
        verbose_name = 'Invoice Detail'
        verbose_name_plural = 'Invoice Details'

    def __str__(self):
        return f"Detail for Invoice {self.invoice.invoice_number}"