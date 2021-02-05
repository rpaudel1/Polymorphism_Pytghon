# This program import the insect_class_polymorphism module here
# The isinstance() function is incorporated here
import insect_class_polymorphism as ic

def find_member(member):
  if isinstance(member, ic.Insect): # isinstance method
    print(member)
  else:
    print(member,' isn\'t an instance of Insect')

def create_instance():
	wasp = ic.Insect('Yellow Jacket')
	find_member(wasp)
	mosquito = ic.Mosquito('Aedes')
	find_member(mosquito)
	bug = ic.Bug('Laby-bug')
	find_member(bug)
	find_member('Long Horn')
	find_member('Hornet') 
create_instance()

