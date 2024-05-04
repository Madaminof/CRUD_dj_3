from django.db import models

# Create your models here.


class Serial_Name(models.Model):
    name=models.CharField(max_length=20)


    class Meta:
        db_table='serial'

    def __str__(self) -> str:
        return self.name





class Get_Actior(models.Model):
    serial=models.ForeignKey(to='Serial_Name',on_delete=models.CASCADE)
    actior_name=models.CharField(max_length=20)
    yera=models.IntegerField()
    gender=models.CharField(10)
    image=models.ImageField(upload_to='rasm/',blank=True,null=True)


    class Meta:
        db_table='aktior'

    def __str__(self) -> str:
        return f"{self.serial.name}  {self.actior_name}"
    
        