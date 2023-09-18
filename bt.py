class Node:

    def __init__(self, value):
          
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        res = f'значение нашего узла: {self.value}'
        if self.left:
            res += f' значение левого: {self.left.value}'
        if self.right:
            res += f' значение правого: {self.right.value}'
        return res


class BinaryTree:

    def __init__(self, root_value):
        self.root = Node(root_value)

    def add(self, value):
        res = self.search(self.root, value)

        if res[0] is None:
            new_node = Node(value)
            if value > res[1].value:
                res[1].right = new_node
            else:
                res[1].left = new_node
        else:
            print("Хорош")

    def search(self, node, value, parent=None):
        if node == None or value == node.value:
            return node, parent
        if value > node.value:
            return self.search(node.right, value, node)
        if value < node.value:
            return self.search(node.left, value, node)
    
    def count_elements(self, node):
        if node is None:
            return 0
        else:
            
            left_count = self.count_elements(node.left)
            right_count = self.count_elements(node.right)
            
            return 1 + left_count + right_count

    def get_element_count(self):
        
        return self.count_elements(self.root)

    def delete(self, value):
        self.root, _ = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            
            return node, None

        if value < node.value:
            
            node.left, _ = self._delete_recursive(node.left, value)
        elif value > node.value:
            
            node.right, _ = self._delete_recursive(node.right, value)
        else:
            
            if node.left is None:
                
                return node.right, node
            elif node.right is None:
                
                return node.left, node
            else:
                
                successor = self._find_min(node.right)
                node.value = successor.value
                node.right, _ = self._delete_recursive(node.right, successor.value)

        return node, None

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    
    def display_tree(self):
        tree_lines, *_ = self._display_vertical(self.root)
        for line in tree_lines:
            print(line)

    def _display_vertical(self, node):

        if node is None:
            return [], 0, 0, 0, 0

        left_tree, left_start, left_end, left_width, left_height = self._display_vertical(node.left)
        right_tree, right_start, right_end, right_width, right_height = self._display_vertical(node.right)

        middle = str(node.value)
        middle_width = len(middle)
        middle_height = 1

        root_start = max(left_end + 1, (left_start + right_end + 2 - middle_width) // 2)
        root_end = root_start + middle_width
        root_width = root_end - root_start
        root_height = left_height + middle_height + right_height

        width = max(left_start + right_width + 1, root_end)
        while len(left_tree) < len(right_tree):
            left_tree.append(' ' * width)
        while len(right_tree) < len(left_tree):
            right_tree.append(' ' * width)

        middle_line = ' ' * (left_end + 1) + middle + ' ' * (right_end - root_width + 1)

        if middle_width % 2 == 1 and root_width % 2 == 0:
            middle_line = middle_line[:-1] + ' ' + middle_line[-1]

        lines = []
        height = max(left_height, middle_height, right_height)

    # Adjust the formatting to align the tree to the right by adding spaces before the lines
        root_line = ' ' * (width - root_end) + middle_line

        if left_height > 0:
            for i in range(left_height):
                left = left_tree[i].splitlines()
                right = right_tree[i].splitlines() if i < right_height else [''] * right_height
                lines.append(left[0] + root_line + right[0])

        lines.append(root_line)

        for i in range(1, height):
            left = left_tree[i].splitlines() if i < left_height else [''] * left_height
            right = right_tree[i].splitlines() if i < right_height else [''] * right_height
            lines.append(left[0] + ' ' * width + right[0])

        return lines, root_start, root_end, width, height




bt = BinaryTree(5)
bt.add(10)
bt.add(15)
bt.add(3)
bt.add(4)

print(bt.root)
print(bt.root.left)
print(bt.root.right)
print("Количество элементов в бинарном дереве:", bt.get_element_count())



print("Дерево:")
bt.display_tree()

bt.delete(10)
element_count = bt.get_element_count()
print("Количество элементов после удаления:", element_count)