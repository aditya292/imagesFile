# images/views.py

from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image
import base64

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            # Get the uploaded file
            image_file = request.FILES.get('image_file')
            if image_file:
                # Convert image to base64
                image_base64 = base64.b64encode(image_file.read()).decode('utf-8')
                # Save the form with base64 data
                image_instance = form.save(commit=False)
                image_instance.image_base64 = image_base64
                image_instance.save()
                return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'images/upload_image.html', {'form': form})

def image_list(request):
    images = Image.objects.all()
    return render(request, 'images/image_list.html', {'images': images})
