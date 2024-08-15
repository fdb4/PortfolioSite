from django.contrib import admin
from .models import Aboutme,Education,Coreskills,Certifications,Workexperience
# Register your models here.
admin.site.register(Aboutme)
admin.site.register(Coreskills)
admin.site.register(Education)
admin.site.register(Certifications)
admin.site.register(Workexperience)
