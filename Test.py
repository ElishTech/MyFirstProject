from Family import Family

def exe():
    father_name=input("Enter father name: ")
    mother_name=input("Enter mother name: ")
    father_age=int(input("Enter father age: "))
    mother_age=int(input("Enter mather age: "))
    father_details={'name':father_name,'age':father_age}
    mother_details={'name':mother_name,'age':mother_age}
    parents={'father':father_details,'mother':mother_details}
    last_name=input("Enter last name: ")
    num_of_children=int(input("Enter num of children: "))
    children={}
    for i in range(num_of_children):
        child_name=input("Enter child name: ")
        child_age=int(input("Enter age name: "))
        children[child_name]=child_age

    family1=Family(parents,children=children,last_name=last_name)
    print(f"The {family1.last_name}'s children: ", family1.get_children())
    family1.add_child('Beny',0)
    print(f"The {family1.last_name}'s children after adding child: ",family1.get_children())
    print("The parents: ",family1.get_parents_names())

if __name__ == '__main__':
    exe()
    #first execute example:Enter father name: dan
    # Enter mother name: Sara
    # Enter father age: 38
    # Enter mather age: 36
    # Enter last name: levi
    # Enter num of children: 2
    # Enter child name: Chani
    # Enter age name: 13
    # Enter child name: Eli
    # Enter age name: 7
    # The levi's children:  [('Chani', 13), ('Eli', 7)]
    # The levi's children after adding child:  [('Chani', 13), ('Eli', 7), ('Beny', 0)]
    # The parents:  ('dan', 'Sara')