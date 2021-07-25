# 05. Programmer

class Programmer:
	def __init__(self, name, language, skills):
		self.name = name
		self.language = language
		self.skills = skills
		
	def watch_course(self, course_name, language, gained_skills):
		if language == self.language:
			self.skills += gained_skills
			return f"{self.name} watched {course_name}"
		return f"{self.name} does not know {language}"
		
	def change_language(self, new_language, skills_needed):
		if skills_needed <= self.skills:
			if new_language != self.language:
				old_language = self.language
				self.language = new_language
				return f"{self.name} switched from {old_language} to {new_language}"
			return f"{self.name} already knows {new_language}"
		return f"{self.name} needs {skills_needed - self.skills} more skills"
		

# Test Code:
"""
programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
"""
			