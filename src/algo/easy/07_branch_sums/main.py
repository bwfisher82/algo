import src.algo.binary_tree as binary_tree


def find_branch_sums(tree: binary_tree.Node) -> list[int]:
    pass


if __name__ == "__main__":
    root = binary_tree.Node(1)
    binary_tree.binary_insert(root, binary_tree.Node(2))
    binary_tree.binary_insert(root, binary_tree.Node(3))
    binary_tree.binary_insert(root, binary_tree.Node(4))
    binary_tree.binary_insert(root, binary_tree.Node(5))
    binary_tree.binary_insert(root, binary_tree.Node(6))
    binary_tree.binary_insert(root, binary_tree.Node(7))
    binary_tree.binary_insert(root, binary_tree.Node(8))
    binary_tree.binary_insert(root, binary_tree.Node(9))
    binary_tree.binary_insert(root, binary_tree.Node(10))
    print(find_branch_sums(root)) # [15, 16, 18, 10, 11]
