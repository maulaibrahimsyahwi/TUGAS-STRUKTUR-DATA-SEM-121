class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_value):
        self.children = [child for child in self.children if child.value != child_value]

    def display(self, level=0):
        print(" " * (level * 4) + f"- {self.value}")
        for child in self.children:
            child.display(level + 1)

class InteractiveTree:
    def __init__(self):
        self.root = None

    def set_root(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            print("Root already exists. Use the existing root.")

    def find_node(self, current_node, value):
        if current_node is None:
            return None
        if current_node.value == value:
            return current_node
        for child in current_node.children:
            found = self.find_node(child, value)
            if found:
                return found
        return None

    def add_node(self, parent_value, child_value):
        parent_node = self.find_node(self.root, parent_value)
        if parent_node:
            new_child = TreeNode(child_value)
            parent_node.add_child(new_child)
        else:
            print(f"Parent node '{parent_value}' not found.")

    def remove_node(self, value):
        if self.root and self.root.value == value:
            print("Cannot remove the root node.")
            return
        parent_node = self.find_parent(self.root, value)
        if parent_node:
            parent_node.remove_child(value)
        else:
            print(f"Node '{value}' not found.")

    def find_parent(self, current_node, child_value):
        if current_node is None:
            return None
        for child in current_node.children:
            if child.value == child_value:
                return current_node
            found = self.find_parent(child, child_value)
            if found:
                return found
        return None

    def display_tree(self):
        if self.root:
            self.root.display()
        else:
            print("Tree is empty.")

# Interaktif Menu
def menu():
    tree = InteractiveTree()

    while True:
        print("\nTree Operations:")
        print("1. Set Root Node")
        print("2. Add Node")
        print("3. Remove Node")
        print("4. Display Tree")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            value = input("Enter root value: ")
            tree.set_root(value)
        elif choice == '2':
            parent_value = input("Enter parent value: ")
            child_value = input("Enter child value: ")
            tree.add_node(parent_value, child_value)
        elif choice == '3':
            value = input("Enter value to remove: ")
            tree.remove_node(value)
        elif choice == '4':
            tree.display_tree()
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
