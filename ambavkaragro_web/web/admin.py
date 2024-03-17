from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Customer)
admin.site.register(Slider)
admin.site.register(Brands)
admin.site.register(Testimonial)