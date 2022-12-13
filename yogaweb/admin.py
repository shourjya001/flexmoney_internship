from django.contrib import admin
from .models import UserProfile,Newsletter,Contact,Instructor,Feestrack,Advertisements
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Newsletter)
admin.site.register(Contact)
admin.site.register(Feestrack)
admin.site.register(Advertisements)