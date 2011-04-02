from django.contrib import admin
from earthquake import models

class RoofTypeAdmin(admin.ModelAdmin):
    list_display = 'name', 'description'

class PrimaryAdmin(admin.ModelAdmin):
    list_display = 'name', 'description'

class SecondaryAdmin(admin.ModelAdmin):
    list_display = 'name', 'description'

class HeightTypeAdmin(admin.ModelAdmin):
    list_display = 'name', 'description'

class BuildingTypeAdmin(admin.ModelAdmin):
    list_display = (
                   'id',
                   'primary_structural_system', 
                   'secondary_structural_system',
                   'roof_type',
                   'height_type',
                   )
    list_filter = (
                   'primary_structural_system',
                   'secondary_structural_system',
                   'roof_type',
                   'height_type',
                  )

class CurveAdmin(admin.ModelAdmin):
    list_display = (
                   'building_type',
                   'points',
                   'vulnerability_function',
                   )
    list_filter = ('vulnerability_function',)

class CurveInline(admin.TabularInline):
    model = models.Curve


class VulnerabilityAdmin(admin.ModelAdmin):
    list_display = (
                   'name',
                   'confidence',
                   )
    inlines = [
            CurveInline,
        ]


admin.site.register(models.RoofType, RoofTypeAdmin)
admin.site.register(models.PrimaryStructuralSystem, PrimaryAdmin)
admin.site.register(models.SecondaryStructuralSystem, SecondaryAdmin)
admin.site.register(models.BuildingType, BuildingTypeAdmin)
admin.site.register(models.HeightType, HeightTypeAdmin)
admin.site.register(models.VulnerabilityFunction, VulnerabilityAdmin)
admin.site.register(models.Curve, CurveAdmin)
