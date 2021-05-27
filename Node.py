class Node:
    def __init__(self, course_id, course_name):
        self.name = course_name
        self.id = course_id
        self.prereq = []

    def add_andprereq(self, course_id):
        self.prereq.append(course_id)
    
    def add_orprereq(self, course_id_list):
        self.prereq.append(course_id_list)