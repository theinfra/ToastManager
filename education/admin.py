from django.contrib import admin

from .models.Agenda import Agenda

class AgendaAdmin(admin.ModelAdmin):
	fieldsets = (
		(
			None,
			{
				'fields':['toastmaster', 'topic', 'date', 'time', 'created_at', 'updated_at']
			}
		),
		(
			'Evaluators',
			{
				'fields': ['evaluator_general', 'evaluator_crutch', 'evaluator_time', 'evaluator_grammar', 'evaluator_pronunciation',]
			}
		),
		(
			'Word of the Week',
			{
				'fields': ['word_of_the_week', 'wow_definition', 'wow_example',]
			}
		)
	)
	add_fieldsets = (
		(
			None,
			{
				'fields': ['toastmaster', 'date']
			}
		)
	)
	readonly_fields = ['created_at', 'updated_at']
	list_display = ['date', 'toastmaster', 'topic']

# Register your models here.
admin.site.register(Agenda, AgendaAdmin)