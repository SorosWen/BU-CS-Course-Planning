from ast import increment_lineno


class Class:
    def __init__(self, course_id, course_name):
        self.name = course_name
        self.id = course_id
        self.node = Or_Node()

class And_Node():
    def __init__(self):
        self.prereq = []
    
    def add_req(self, name, obj):
        self.prereq.append(name)
    
    def __str__(self):
        text = ''
        for ele in self.prereq:
            text = text + ' and ' + ele
        text = '{' + text + ';}'
        return text

    def is_satisfied(self, completed_courses):
        if len(self.prereq) == 0:
            return True
        for criteria in self.prereq:
            if type(criteria) == 'And_Node' or type(criteria) == 'Or_Node':
                if not criteria.is_satisfied():
                    return False 
            elif criteria not in completed_courses: 
                return False
        return True


class Or_Node():
    def __init__(self):
        self.prereq = []
    
    def add_req(self, name, obj):
        self.prereq.append(name)
    
    def __str__(self):
        text = ''
        for ele in self.prereq:
            text = text + ' or ' + ele
        text = '(' + text + ';)'
        return text

    def is_satisfied(self, completed_courses):
        if len(self.prereq) == 0:
            return True
        for criteria in self.prereq:
            if type(criteria) == 'And_Node' or type(criteria) == 'Or_Node':
                if criteria.is_satisfied():
                    return True 
            elif criteria in completed_courses: 
                return True
        return False