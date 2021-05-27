from django.contrib import admin
from . models import Contact
# Register your models here.
admin.site.site_header = "My Portfolio"
admin.site.index_title = "Welcome to Prince Bhut Portfolio"
admin.site.site_title = "My Portfolio"

admin.site.register(Contact)