from django.shortcuts import render, get_object_or_404, redirect
from .models import Lead

def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'lead_list.html', {'leads': leads})


def lead_detail(request, id):
    lead = get_object_or_404(Lead, id=id)
    return render(request, 'lead_detail.html', {'lead': lead})


def dashboard(request):
    total = Lead.objects.count()
    new = Lead.objects.filter(status='New').count()
    contacted = Lead.objects.filter(status='Contacted').count()

    context = {
        'total': total,
        'new': new,
        'contacted': contacted
    }

    return render(request, 'dashboard.html', context)