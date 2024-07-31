from django.contrib import admin
from .models import Contact_us
#from .models import Tag
#from .forms import StockForm

# Register your models here.


#class ContactAdmin(admin.ModelAdmin):
#   list_display = ['name']
 #  form = StockForm


admin.site.register(Contact_us)

#admin.site.register(Tag)


