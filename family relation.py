
class Member(object):
    def __init__(self, founder):
        """ 
        founder: string
        Initializes a member. 
        Name is the string,
        parent is None, and no children
        """        
        self.name = founder
        self.parent = None         
        self.children = []    

    def __str__(self):
        return self.name    

    def add_parent(self, mother):
        """
        mother: Member
        Sets the parent of this node to the `mother` node
        """
        self.parent = mother   

    def get_parent(self):
        """
        Returns the parent Member
        """
        return self.parent 

    def is_parent(self, mother):
        """
        mother: Member
        Returns: Boolean
        """
        return self.parent == mother  

    def add_child(self, child):
        """
        child: Member
        Adds another child Member node to this Member
        """
        self.children.append(child)   

    def is_child(self, child):
        """
        child: Member
        Returns: Boolean
        """
        return child in self.children 


class Family(object):
    def __init__(self, founder):
        """ 
        Initialize with string of name of oldest ancestor
        Keyword arguments:
        founder -- string of name of oldest ancestor
        """

        self.names_to_nodes = {}
        self.root = Member(founder)    
        self.names_to_nodes[founder] = self.root   

    def set_children(self, mother, list_of_children):
        """
        Set all children of the mother. 
        Keyword arguments: 
        mother -- mother's name as a string
        list_of_children -- children names as strings
        """
        
        mom_node = self.names_to_nodes[mother]   
        
        for c in list_of_children:           
               
            c_member = Member(c)               
            
            self.names_to_nodes[c] = c_member    
            
            c_member.add_parent(mom_node)        
    
            mom_node.add_child(c_member)         
    
    def is_parent(self, mother, kid):
        """
        Returns True or False whether mother is parent of kid. 
        Keyword arguments: 
        mother -- string of mother's name
        kid -- string of kid's name
        """
        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return child_node.is_parent(mom_node)   

    def is_child(self, kid, mother):
        """
        Returns True or False whether kid is child of mother. 
        Keyword arguments: 
        kid -- string of kid's name
        mother -- string of mother's name
        """        
        mom_node = self.names_to_nodes[mother]   
        child_node = self.names_to_nodes[kid]
        return mom_node.is_child(child_node)

    def cousin(self, a, b):
        """
        Returns a tuple of (the cousin type, degree removed) 
        cousin type is an integer that is -1 if a and b
        are the same node or if one is the direct descendent 
        of the other.  Otherwise, cousin type is 0 or greater,
        representing the shorter distance to their common 
        ancestor as described in the exercises above.
        degree removed is the distance to the common ancestor
        Keyword arguments: 
        a -- string that is the name of a
        b -- string that is the name of b
        """
        
        
        a_node = self.names_to_nodes[a]
        b_node = self.names_to_nodes[b]

        def create_branch(node):
            branch = [node]
            parent = node.get_parent()

            while parent:
                branch.append(parent)
                parent = parent.get_parent()
            return branch

        if a_node.name == b_node.name:
            return (-1, 0)
        elif a_node.is_child(b_node) or b_node.is_child(a_node):
            return (-1, 0)

        a_branch = create_branch(a_node)
        b_branch = create_branch(b_node)

        b_parent_index = 0
        for a_parent_index, node in enumerate(a_branch):
            try:
                b_parent_index = b_branch.index(node)
                break
            except ValueError:
                pass

        cousin_type = max(a_parent_index, b_parent_index)
        degree_removed = abs(a_parent_index - b_parent_index)
        return (cousin_type, degree_removed)

if __name__ == '__main__':
    
    f = Family("a")
    f.set_children("a", ["b", "c"])
    f.set_children("b", ["d", "e"])
    f.set_children("c", ["f", "g"])

    f.set_children("d", ["h", "i"])
    f.set_children("e", ["j", "k"])
    f.set_children("f", ["l", "m"])
    f.set_children("g", ["n", "o", "p", "q"])

    words = ["zeroth", "first", "second", "third", "fourth", "fifth", "non"]

    ## These are your test cases. 

    ## The first test case should print out:
    ## 'b' is a zeroth cousin 0 removed from 'c'
    t, r = f.cousin("b", "c")
    print "'b' is a", words[t],"cousin", r, "removed from 'c'"

    ## For the remaining test cases, use the graph to figure out what should 
    ## be printed, and make sure that your code prints out the appropriate values.

    t, r = f.cousin("d", "f")
    print "'d' is a", words[t],"cousin", r, "removed from 'f'"

    t, r = f.cousin("i", "n")
    print "'i' is a", words[t],"cousin", r, "removed from 'n'"

    t, r = f.cousin("q", "e")
    print "'q' is a", words[t], "cousin", r, "removed from 'e'"

    t, r = f.cousin("h", "c")
    print "'h' is a", words[t], "cousin", r, "removed from 'c'"

    t, r = f.cousin("h", "a")
    print "'h' is a", words[t], "cousin", r, "removed from 'a'"

    t, r = f.cousin("h", "h")
    print "'h' is a", words[t], "cousin", r, "removed from 'h'"

    t, r = f.cousin("a", "a")
    print "'a' is a", words[t], "cousin", r, "removed from 'a'"