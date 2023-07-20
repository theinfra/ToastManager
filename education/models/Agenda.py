from django.db import models
from datetime import datetime
from django.conf import settings

# Dated Agenda instances
class Agenda(models.Model):
	toastmaster = models.ForeignKey('core.Member', on_delete=models.RESTRICT, related_name="toastmaster", related_query_name="agenda_toastmaster")
	topic = models.CharField(max_length=20)
	date = models.DateField(db_index=True)
	time = models.TimeField(default=settings.DEFAULT_AGENDA_TIME)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	evaluator_general = models.ForeignKey('core.Member', on_delete=models.RESTRICT, related_name="evgeneral", related_query_name="agenda_evgeneral", verbose_name="General")
	evaluator_crutch = models.ForeignKey('core.Member', on_delete=models.RESTRICT, related_name="evcrutch", related_query_name="agenda_evcrutch", verbose_name="Crutches")
	evaluator_time = models.ForeignKey('core.Member', on_delete=models.RESTRICT, related_name="evtime", related_query_name="agenda_evtime", verbose_name="Timekeeper")
	evaluator_grammar = models.ForeignKey('core.Member', on_delete=models.RESTRICT, related_name="evgrammar", related_query_name="agenda_evgrammar", verbose_name="Grammar")
	evaluator_pronunciation = models.ForeignKey('core.Member', on_delete=models.RESTRICT, null=True, related_name="evpronunciation", related_query_name="agenda_evpronunciation", verbose_name="Pronunciation")

	word_of_the_week = models.CharField(max_length=400)
	wow_definition = models.TextField('Definition')
	wow_example = models.TextField('Example')

	def __str__(self):
		return f"Agenda {self.date} - '{self.topic}'"