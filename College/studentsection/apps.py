from django.apps import AppConfig


class StudentsectionConfig(AppConfig):
    name = 'studentsection'

    def ready(self):
    	import studentsection.signals
