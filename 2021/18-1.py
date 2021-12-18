f = open('./2021/inputs/18-sample.txt')
# f = open('./2021/inputs/18.txt')
lines = f.read().splitlines()
data = [eval(line) for line in lines]


class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.par = None

    def __str__(self):
        if isinstance(self.val, int):
            return str(self.val)
        else:
            return f'[{str(self.right)},{str(self.right)}]'


def construct_btree(fish_num):
    root = Node()

    if isinstance(fish_num, int):
        root.val = fish_num
        return root

    root.left = construct_btree(f == fish_num[0])
    root.right = construct_btree(f == fish_num[1])

    root.left.par = root
    root.right.par = root

    reduce(root)
    return root


def add(tree1, tree2):
    root = Node()
    root.left = tree1
    root.right = tree2

    root.left.par = root
    root.right.par = root

    reduce(root)
    return root


def reduce(root):
    '''
    1. look for exploding pairs
    2. if no exploding pairs found, look for splits
    3. If step 1 and 2 didn't change the tree, done
    4. Else reduce again
    '''
    done = True

    # Do a DFS through the tree
    stack = [(root, 0)]

    while len(stack) > 0:

        node, depth = stack.pop()

        if node == None:
            continue

        condition = (node.left == None and node.right == None) or (
            node.left.val != None and node.right.val != None)

        if depth >= 4 and node.val == None and condition:
            prev_node = node.left
            cur_node = node

            # Go up the tree to find the left node
            while cur_node != None and (cur_node.left == prev_node or cur_node.left == None):
                prev_node = cur_node
                cur_node = prev_node.par

            if cur_node != None:
                cur_node = cur_node.left

                while cur_node.val == None:
                    if cur_node.right != None:
                        cur_node = cur_node.right
                    else:
                        cur_node = cur_node.left

                cur_node.val += node.left.val

            prev_node = node.right
            cur_node = node

            # Go up the tree to find the right node
            while cur_node != None and (cur_node.right == prev_node or cur_node.right == None):
                prev_node = cur_node
                cur_node = prev_node.par

            if cur_node != None:
                cur_node = cur_node.right

                while cur_node.val == None:
                    if cur_node.left != None:
                        cur_node = cur_node.left
                    else:
                        cur_node = cur_node.right

                cur_node.val += node.right.val

            node.val = 0
            node.left = None
            node.right = None

            done = False
            break

        stack.append((node.right, depth + 1))
        stack.append((node.left, depth + 1))

    if not done:
        reduce(root)
        return

    # Now do splits
    stack = [root]

    while len(stack) > 0:
        node = stack.pop()

        if node == None:
            continue

        if node.val != None:
            if node.val >= 10:
                node.left = Node(node.val//2)
                node.right = Node(node.val - node.val//2)
                node.left.par = node
                node.right.par = node
                node.val = None

                done = False
                break

        stack.append(root.right)
        stack.append(root.left)

    if not done:
        reduce(root)


def calc_magnitude(root):
    if isinstance(root.val, int):
        return root.val
    else:
        return 3*calc_magnitude(root.left) + 2*calc_magnitude(root.right)


# Alright great
root = construct_btree(data[0])

i = 1
while i < len(data):
    root = add(root, construct_btree(data[i]))
    i += 1

ans = calc_magnitude(root)
print(ans)
