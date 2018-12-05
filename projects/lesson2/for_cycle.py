classes_grades = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, 
                  {'school_class': '4b', 'scores': [3,5,4,5,3]},
                  {'school_class': '3a', 'scores': [3,5,5,5,4]},
                  {'school_class': '6a', 'scores': [3,2,4,4,2]},
                  {'school_class': '5a', 'scores': [3,2,3,4,2]}]
school_grades = []
grade_count = 0

for class_and_scores in classes_grades:
	grade_count += len(class_and_scores['scores'])
	school_grades.extend(class_and_scores['scores'])
	print('Средняя оценка в классе {}: {}'.format(class_and_scores['school_class'], sum(class_and_scores['scores'])/len(class_and_scores['scores'])))

print('Средняя оценка в школе: {}'.format(sum(school_grades)/grade_count))

