# classes and objects are the concepts of object orietned programming language
# properties of any class are the components that are occupied by any class such as , name occupation of of a person.PermissionError
# methods is called as the activiity performed by a class, both of property and method comprises of a class entity such as human.

class college:
    def __init__(self, name, city):    # self is just a synitax which defines a class itsefl
        self.name = "Samrat Ashok Technological Institutee"
        self.city = "Vidisha"  # these names and city are all properties.

    def do_work(self):
        if self.city == "Vidisha":
            print(self.name, "Plays tennis")
        elif self.city == "jbp":
            print(self.name, " does'nt exiist")


    def speaks(self):
           print(self.name, "has the best education")


Sakshi= college("Sakshi tiwari", "Jabalpur")    
Sakshi.do_work()      
Sakshi.speaks()          

