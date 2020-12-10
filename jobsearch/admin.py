from django.contrib import admin
from .models import Customer, TripCategory, Destination
from .models import Contact_Information, Employee, State
from .models import Listing_Status, Applicant, Company, Skills, Job_Listing, Job_Offer

# Register your models here.
admin.site.register(Customer)
admin.site.register(TripCategory)
admin.site.register(Destination)  
#
admin.site.register(Contact_Information)
admin.site.register(Employee)
admin.site.register(State)  
admin.site.register(Listing_Status)
admin.site.register(Applicant)
admin.site.register(Company)
admin.site.register(Skills)
admin.site.register(Job_Listing)
admin.site.register(Job_Offer)
