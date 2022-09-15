from django.contrib import admin
from legal.models.modelsApp.LegalBusinessMasterModel import LegalCustomerModel


# Register your models here.
admin.site.register(LegalCustomerModel)


@admin.register(LegalCustomerModel)

class LegalCustomerModelAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)