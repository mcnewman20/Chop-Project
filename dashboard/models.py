from django.db import models


# Create your models here.
class Sample_Information(models.Model):
    aliquot_pk_serial = models.IntegerField(primary_key=True)
    received_on = models.DateField(auto_now=False, auto_now_add=False)
    collected_on = models.DateField(auto_now=False, auto_now_add=False)
    sample_type_code = models.CharField(max_length=50)
    secondary_sample_code = models.CharField(max_length=50)
    sample_type = models.CharField(max_length=50)
    full_sample_type_desc = models.CharField(max_length=50)
    origin_aliquot_desc = models.CharField(max_length=50)
    tissue_type = models.CharField(max_length=50)
    specimen_category = models.CharField(max_length=50)
    volume_received = models.IntegerField()
    volume_remaining = models.IntegerField()
    alq_status = models.CharField(max_length=50)
    available_flag = models.BooleanField()