from django.shortcuts import render
from .models import Student

# Create your views here.
def index(request):
    return render (request, "index.html")

def administration(request):
    return render (request, "form.html")

def register(request):
    if request.method == 'POST':
        # Get all form fields
        name = request.POST.get('name')
        email = request.POST.get('email')
        admission_number = request.POST.get('admission_number')
        branch = request.POST.get('branch')
        year = request.POST.get('year')
        contact_number = request.POST.get('contact_number')
        component_name = request.POST.get('component_name')
        componentissue_date = request.POST.get('componentissue_date')
        componentdue_date = request.POST.get('componentdue_date')
        faculty_referred = request.POST.get('faculty_referred')

        # Save to database
        Student.objects.create(
            name=name,
            email=email,
            admission_number=admission_number,
            branch=branch,
            year=year,
            contact_number=contact_number,
            component_name=component_name,
            componentissue_date=componentissue_date,
            componentdue_date=componentdue_date,
            faculty_referred=faculty_referred
        )
        return render(request, "furm.html", {'success': True})

    return render(request, "furm.html")
