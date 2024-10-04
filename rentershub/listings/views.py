from django.views.generic import CreateView, TemplateView, ListView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import PropertyPostForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


# A mixin to save multiple images
class SaveImagesMixin:
    def save_images(self, property, images):
        for image in images:
            PropertyImages.objects.create(property=property, image=image)

# A view for creating a new property post
class PropertyPostView(SaveImagesMixin, LoginRequiredMixin, CreateView):
    model = PropertyPost
    form_class = PropertyPostForm
    template_name = 'listings/templates/uploads.html'
    success_url = reverse_lazy('view_properties')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user 
        property = form.save()
        for image in self.request.FILES:
            self.save_images(property, self.request.FILES.getlist('images')) # Save object images to the property images model 
        return super().form_valid(form)

# A view for viewing all property posts       
class PropertyListView(ListView):
    model = PropertyPost
    template_name = 'listings/templates/listings.html'
    context_object_name = 'listing'
    ordering = ['-date_posted'] 

# A view for deleting a property post
class PropertyDeleteView(DeleteView):
    model = PropertyPost
    template_name = 'listings/templates/property_confirm_delete.html' 
    success_url = reverse_lazy('view_properties')

# A view for updating/editing a property post
class PropertyEditView(SaveImagesMixin, UpdateView):
    model = PropertyPost
    form_class = PropertyPostForm
    template_name = 'listings/templates/property_update_form.html'
    success_url = reverse_lazy('view_properties')

    
    def get_context_data(self, **kwargs): # Include existing images in the context
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.propertyimages_set.all()  
        return context
    
    def form_valid(self, form):
        property = form.save()
        images_to_delete = self.request.POST.getlist('delete_images')
        if images_to_delete:
            for image_id in images_to_delete:
                image = PropertyImages.objects.get(id=image_id)
                image.delete()

        if 'images' in self.request.FILES: # Check if new images were uploaded by the user and save them
            self.save_images(property, self.request.FILES.getlist('images'))
        return super().form_valid(form)
    
# A view for viewing property details
class PropertyDetailView(DetailView):
    model = PropertyPost
    template_name = 'listings/templates/property_detail.html'
    context_object_name = 'property'