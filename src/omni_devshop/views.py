from django.shortcuts import render

from omni_customers.models import Customer


def websites(request):

    customers = Customer.objects.order_by('name').prefetch_related('projects__websites__envs').all()

    return render(request, 'omni/devshop/websites.html', {
        'customers': customers,
        'can_edit': request.user.is_superuser,
    })
