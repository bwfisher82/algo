from typing import Any


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


def generate_test_bst(data: dict[str, Any]) -> Node:
    tree: dict[str, list|str] = data["tree"]
    nodes: list[dict] = tree["nodes"]
    root_id: str = data["tree"]["root"]
    bst_root = None
    for node in nodes:
        if node["id"] == root_id:
            bst_root = Node(node["value"])
    if bst_root is not None:
        for node in nodes:
            if node["id"] != root_id:
                binary_insert(bst_root, Node(node["value"]))
    target: int = data["target"]
    return bst_root
