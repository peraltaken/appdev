from django.db import models

# Create your models here.
class BaseTable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class DivisionTable(BaseTable):
    division_image = models.ImageField(upload_to='division_images/', null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class RoleTable(BaseTable):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class CapabilityTable(BaseTable):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class StaffTable(BaseTable):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    hire_date = models.DateTimeField()
    division = models.ForeignKey(DivisionTable, on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(RoleTable, on_delete=models.SET_NULL, null=True)
    capabilities = models.ManyToManyField(CapabilityTable)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class InitiativeTable(BaseTable):
    initiative_image = models.ImageField(upload_to='initiative_images/', null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    staff = models.ManyToManyField(StaffTable)

    def __str__(self):
        return self.name