from django.contrib import admin
from .models import BaseTable, DivisionTable, RoleTable, CapabilityTable, StaffTable, InitiativeTable

# Register your models here.
admin.site.register(DivisionTable)
admin.site.register(RoleTable)
admin.site.register(CapabilityTable)
admin.site.register(StaffTable)
admin.site.register(InitiativeTable)