from django.shortcuts import render
import pandas as pd
from .models import CAPEXModels

# views.py


def home(request):
    # Use separate lines for import statements
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file is not None:
            try:
                # Explicitly catch ParserError instead of any Exception
                # to avoid hiding other exceptions.
                df = pd.read_excel(file, sheet_name="CAPEX")
                context = {'User': request.user, 'df': df}
                return render(request, 'home.html', context)

            except pd.errors.ParserError as e:
                # Handle ParserError explicitly
                return render(request, 'error.html', {'error': str(e)})
    return render(request, 'home.html')


def index(request):
    books = CAPEXModels.objects.all()
    return render(request, 'index.html', {'books': books})


def about(request):
    return render(request, 'about.html')
