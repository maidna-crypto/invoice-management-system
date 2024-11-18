from rest_framework import serializers
from .models import InvoiceModel, InvoiceDetailModel

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetailModel
        fields = ['id', 'description', 'quantity', 'price', 'line_total']
        read_only_fields = ['line_total']  

    def validate(self, data):
        """Validate invoice detail data"""
        if data['quantity'] <= 0:
            raise serializers.ValidationError({
                "quantity": "Quantity must be greater than 0"
            })
        if data['price'] <= 0:
            raise serializers.ValidationError({
                "price": "Price must be greater than 0"
            })
        
        data['line_total'] = data['quantity'] * data['price']
        return data


class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True, source='invoice_detail')

    class Meta:
        model = InvoiceModel
        fields = ['id', 'invoice_number', 'customer_name', 'date', 'details']

    def validate_invoice_number(self, value):
        """Validate invoice number uniqueness"""
        instance = getattr(self, 'instance', None)
        if InvoiceModel.objects.filter(invoice_number=value).exclude(id=instance.id if instance else None).exists():
            raise serializers.ValidationError("Invoice number must be unique")
        return value

    def create(self, validated_data):
        details_data = validated_data.pop('invoice_detail')
        invoice = InvoiceModel.objects.create(**validated_data)
        
        for detail_data in details_data:
            InvoiceDetailModel.objects.create(invoice=invoice, **detail_data)
        
        return invoice

    def update(self, instance, validated_data):
        details_data = validated_data.pop('invoice_detail')
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Delete existing details
        instance.invoice_detail.all().delete()
        
        # Create new details
        for detail_data in details_data:
            InvoiceDetailModel.objects.create(invoice=instance, **detail_data)
        
        return instance