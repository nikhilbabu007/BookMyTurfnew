from django.contrib import admin

# Register your models here.
from.models import *
admin.site.register(user)
admin.site.register(turf)
admin.site.register(login)
admin.site.register(owner)
admin.site.register(contact_admin)
admin.site.register(Booking)
admin.site.register(Payment)


