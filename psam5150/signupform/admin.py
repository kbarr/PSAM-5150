# -*- coding: UTF-8 -*-
from django.contrib import admin
from signupform.models import HelloWorld, Signup, City, Country, House, Mayor

class HelloWorldAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('created_on', 'name', 'location', )


class SignupAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('name', 'address', 'city', 'state', 'zipcode', 'phone_number', 'email', 'subject','inquiry',)
    list_filter = ('is_accepted',)
    list_display_links = ('email',)
    search_fields = ['name', 'address','city', 'state', 'zipcode', 'phone_number', 'email', 'subject','inquiry',]

admin.site.register(HelloWorld, HelloWorldAdmin)
admin.site.register(Signup, SignupAdmin)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(House)
admin.site.register(Mayor)