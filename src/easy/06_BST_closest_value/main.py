def find_closest_value_in_bst(tree, target):
	return recurse(tree, target, tree.value)


def recurse(tree, target, closest):
	if tree is None:
		return closest
	if tree.value == target:
		return tree.value
	if abs(target - closest) > abs(tree.value - target):
		closest = tree.value
	if target < tree.value:
		return recurse(tree.left, target, closest)
	elif target > tree.value:
		return recurse(tree.right, target, closest)


class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


def binary_insert(root, node):
	if root is None:
		root = node
	else:
		if root.value < node.value:
			if root.right is None:
				root.right = node
			else:
				binary_insert(root.right, node)
		else:
			if root.left is None:
				root.left = node
			else:
				binary_insert(root.left, node)


if __name__ == "__main__":
	root = Node(10)
	binary_insert(root, Node(5))
	binary_insert(root, Node(15))
	binary_insert(root, Node(2))
	binary_insert(root, Node(5))
	binary_insert(root, Node(13))
	binary_insert(root, Node(22))
	binary_insert(root, Node(1))
	binary_insert(root, Node(14))
	# print(find_closest_value_in_bst(root, 12))
	print(find_closest_value_in_bst(root, 12))