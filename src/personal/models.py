from django.db import models


# PRIORITY=[
# 	{"L","LOW"},
# 	{"M","MEDIEM"},
# 	{"H","HIGH"}
# ]

# class Question(models.Model):
# 	title					=models.CharField(max_length=61)
# 	question				=models.TextField(max_length=401)
# 	priority					=models.CharField(max_length=61,choices=PRIORITY)

# 	def _str_(self):
# 		return self.title


# 	class Meta:
# 		verbose_name="The Question"
# 		verbose_name_plural="People Question"
			
			