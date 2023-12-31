from django.shortcuts import render
from django.core.paginator import Paginator
from .models import StaffTable, DivisionTable, InitiativeTable, RoleTable, CapabilityTable

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def staff_view(request):
    all_staff = StaffTable.objects.all()
    p = Paginator(all_staff, 3)  # Paginate results, showing 5 per page
    page = request.GET.get('page')
    staff_list = p.get_page(page)
    return render(request, 'staff.html', {'staff': staff_list})  # Context variable renamed

def division_view(request):
    all_divisions = DivisionTable.objects.all()
    p = Paginator(all_divisions, 3)
    page = request.GET.get('page')
    division_list = p.get_page(page)
    return render(request, 'division.html', {'division': division_list})  # Context variable renamed

def initiative_view(request):
    all_initiatives = InitiativeTable.objects.all()
    p = Paginator(all_initiatives, 3)
    page = request.GET.get('page')
    initiative_list = p.get_page(page)
    return render(request, 'initiative.html', {'initiative': initiative_list})  # Context variable renamed

def role_view(request):
    all_roles = RoleTable.objects.all()
    p = Paginator(all_roles, 3)
    page = request.GET.get('page')
    role_list = p.get_page(page)
    return render(request, 'role.html', {'role': role_list})  # Context variable renamed

def capability_view(request):
    all_capabilities = CapabilityTable.objects.all()
    p = Paginator(all_capabilities, 3)
    page = request.GET.get('page')
    capability_list = p.get_page(page)
    return render(request, 'capabilities.html', {'capability': capability_list})  # Context variable renamed