from django.contrib import admin
from .models import Car , DataStored ,Voter,N_ID,nationality,User,Profile,Log,persons
# Register your models here.

admin.site.register(Car)
admin.site.register(DataStored)
admin.site.register(Voter)
admin.site.register(N_ID)
admin.site.register(nationality)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Log)
admin.site.register(persons)