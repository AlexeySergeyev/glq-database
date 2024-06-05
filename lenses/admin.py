from django.contrib import admin
import nested_admin
from lenses.models import GLObject
# Register your models here.

from .models import GLObject,GLComponent,Magnitude

class MagnitudeInline(nested_admin.NestedTabularInline):
	model = Magnitude
	# fieldsets = (
	# 	('Component Magnitude',{
	# 		'classes': ('collapse',),
	# 		'fields' : (('m_band','m_value'),'m_date')
	# 		}),
	# 	)
	extra = 0

class GlComponentInline(nested_admin.NestedTabularInline):
    # fieldsets = (
    # 	('Redshift',{
    # 		'fields': ['c_alpha','c_delta']
    # 	})
    # )
    model = GLComponent
    extra = 0
    inlines = [MagnitudeInline]

# class GlComponentAdmin(admin.ModelAdmin):
# 	fields = ['m_band']
# 	inlines = (GlMagInline,)


class GlObjectAdmin(nested_admin.NestedModelAdmin):
	"""
	Admin class for managing GLObject model in the Django admin interface.
	"""
	# fieldsets = (
	# (None, {
	#     'fields': ['gl_name']
	# }),
	# ('Redshifts', {
	#     'fields': ['l_redshift','q_redshift']
	#     }),
	# )
	list_display = ('gl_name', 'gl_ra', 'gl_dec')
	model = GLObject
	list_per_page = 20
	inlines = [GlComponentInline]
	ordering = ('gl_alpha',)

admin.site.register(GLObject, GlObjectAdmin)
