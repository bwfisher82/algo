# import algo.binary_tree as binary_tree


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


if __name__ == "__main__":
	import sys
	print(sys.path)
	sys.exit(0)
	root = binary_tree.Node(10)
	binary_tree.binary_insert(root, binary_tree.Node(5))
	binary_tree.binary_insert(root, binary_tree.Node(15))
	binary_tree.binary_insert(root, binary_tree.Node(2))
	binary_tree.binary_insert(root, binary_tree.Node(5))
	binary_tree.binary_insert(root, binary_tree.Node(13))
	binary_tree.binary_insert(root, binary_tree.Node(22))
	binary_tree.binary_insert(root, binary_tree.Node(1))
	binary_tree.binary_insert(root, binary_tree.Node(14))
	# print(find_closest_value_in_bst(root, 12))
	print(find_closest_value_in_bst(root, 12))