class Clinic(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'role': 'CLINIC'})  
    license_key = models.CharField(max_length=50, unique=True)  
    location = models.CharField(max_length=100)  # Or use GeoDjango PointField for GPS  
    gps_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)  
    gps_lon = models.DecimalField(max_digits=9, decimal_places=6, null=True)  

    def get_current_stock(self):  
        return self.inventory_set.filter(quantity__gt=0)  

    def __str__(self):  
        return f"{self.user.username} Clinic"  

class Medicine(models.Model):  
    name = models.CharField(max_length=100)  
    expiry_date = models.DateField()  
    temperature_required = models.BooleanField(default=False)  # For vaccines  

    def __str__(self):  
        return self.name  

class Inventory(models.Model):  
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)  
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)  
    quantity = models.PositiveIntegerField(default=0)  
    threshold_alert = models.PositiveIntegerField(default=10)  # Low-stock threshold  

    def is_low_stock(self):  
        return self.quantity <= self.threshold_alert  

    def __str__(self):  
        return f"{self.medicine.name} at {self.clinic.user.username}"  