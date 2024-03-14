from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from .ai_model import describe_image  # Import describe_image function from ai_model

def home(request):
    if request.method == 'POST' and request.FILES['image']:
        # Handle image upload
        uploaded_image = request.FILES['image']
        fs = FileSystemStorage()
        image_path = os.path.join(settings.MEDIA_ROOT, uploaded_image.name)
        fs.save(image_path, uploaded_image)
        
        # Process image with AI model
        results = describe_image(image_path)
        
        # Render template with result
        return render(request, 'result.html', {'results': results})  # Changed 'result' to 'results'
    
    return render(request, 'price_comparison_app/home.html')
