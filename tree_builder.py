class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''

    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        top_level = current_node is None

        if top_level:
            if self.root is None:
                print("There is no team lead yet. Add a team lead first.")
                return False
            if side not in ("left", "right"):
                print("Side must be either Left or Right.")
                return False
            current_node = self.root

        if current_node.name == manager_name:
            if getattr(current_node, side) is not None:
                print(f"{manager_name}'s {side.upper()} side is already taken by "
                      f"{getattr(current_node, side).name}.")
                return False
            setattr(current_node, side, EmployeeNode(employee_name))
            print(f"{employee_name} added to the {side.upper()} of {manager_name}")
            return True

        if current_node.left and self.insert(manager_name, employee_name, side, current_node.left):
            return True
        if current_node.right and self.insert(manager_name, employee_name, side, current_node.right):
            return True

        if top_level:
            print(f"Manager '{manager_name}' was not found in the tree.")
        return False

    def print_tree(self, node=None, level=0):
        if node is None:
            if level == 0:
                node = self.root
                if node is None:
                    print("The tree is empty.")
                    return
            else:
                return

        print("  " * level + "- " + node.name)
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


if __name__ == "__main__":
    company_directory_test = TeamTree()
    company_directory_test.root = EmployeeNode("Jordan")
    company_directory_test.insert("Jordan", "Taylor", "right")
    company_directory_test.insert("Jordan", "Riley", "left")
    company_directory_test.insert("Riley", "Dana", "right")
    company_directory_test.insert("Riley", "Morgan", "left")
    company_directory_test.insert("Riley", "Extra", "left")   
    company_directory_test.insert("Nobody", "Sam", "left")    
    company_directory_test.print_tree()


def company_directory():
    tree = TeamTree()

    while True:
        print("\n Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"{name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("Invalid option. Try again.")

# Recursive insertion works by treating every node as the root of its own
# smaller tree. My insert() method starts at the team lead and checks whether
# the current node's name matches the manager I'm looking for. If it does, I
# check that the requested side is empty and create a new EmployeeNode there.
# If it doesn't, the method calls itself on the left child and then the right
# child, so the search walks down the whole hierarchy. Each call only answers
# one small question: is this the manager, or should I keep looking below me?
#
# The hardest part was handling the different outcomes cleanly. Because
# insert() calls itself, an error message could print once for every branch
# searched. I fixed this by returning True or False so each call tells its
# parent whether the manager was found, and only the top-level call prints
# "manager not found" after the whole tree has been searched. I also had to
# validate the side and handle an empty tree before recursing. Small mistakes
# in print_tree() showed me how easily a misplaced stopping condition breaks
# recursion.
#
# Trees are preferable when data is naturally hierarchical or must be searched
# quickly. File systems, web pages, org charts, and decision paths all have
# parent-child relationships that a flat list or dictionary cannot express
# well. Balanced search trees also find items in roughly O(log n) time instead
# of scanning everything, which matters in databases and routing systems that
# keep growing.