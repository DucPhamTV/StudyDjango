from django.contrib import admin
from .models.agent import Agent
from .models.asset import Asset, Category, District, Address, Province
from .models.personal_info import PersonalInfo, Phone, Email
# Register your models here.

admin.site.register(Agent)
admin.site.register(Asset)
admin.site.register(Address)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Category)
admin.site.register(PersonalInfo)
admin.site.register(Phone)
admin.site.register(Email)
