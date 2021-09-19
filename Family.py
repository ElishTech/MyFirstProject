class Father:
    def __init__(self):
        father_name=""
        father_age=None
    def set_father_name(self, name):
        self.father_name=name
    def set_father_age(self, age):
        self.father_age=age
    def get_father_name(self):
        return self.father_name
    def get_father_age(self):
        return  self.father_age

class Mother:

    def __init__(self):
        mother_age=None
        mother_name=""
    def set_mother_name(self, name):
        self.mother_name=name
    def set_mother_age(self, age):
        self.mother_age=age
    def get_mother_name(self):
        return  self.mother_name
    def get_mother_age(self):
        return  self.mother_age

class Child:
    def __init__(self):
        super(Father, self).__init__()
        super(Mother, self).__init__()
        child_name=""
        child_age=None
        father=Father
        mother=Mother
    def set_child_name(self, name):
        self.child_name=name
    def set_child_age(self, age):
        self.child_age=age
    def get_child_name(self):
        return  self.child_name
    def get_child_age(self):
        return self.child_age
    def set_father(self, father_name, father_age):
        self.father.set_father_name(father_name)
        self.father.set_father_age(father_age)
    def set_mother(self, mother_name, mother_age):
        self.mother.set_mother_name(mother_name)
        self.mother.set_mother_age(mother_age)
    def set_parents(self, father_details, mother_details):
        self.set_father(father_details["name"],father_details["age"])
        self.set_mother(mother_details["name"],mother_details["age"])

class Family:
   def  __init__(self, parents, children, last_name=''):
       self.parents=parents
       self.children=list(children.iteדms())
       self.last_name=last_name

   def add_child(self, child_name, child_age):
       self.children.append((child_name,child_age))
   def get_children(self):
       return  self.children
   def get_child(self,i):
       if i<=len(self.children):
         return self.children[i-1]
   def get_parents_names(self):
       return self.parents['father']['name'],self.parents['mother']['name']

