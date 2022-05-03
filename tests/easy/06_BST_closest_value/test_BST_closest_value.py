from typing import Any

import algo.binary_tree as binary_tree

from main import find_closest_value_in_bst


class TestBSTClosestValue:
    @classmethod
    def _get_data_test_case_1(cls) -> (binary_tree.Node, int):
        data: dict[str, Any] = {
          "tree": {
            "nodes": [
              {"id": "10", "left": "5", "right": "15", "value": 10},
              {"id": "15", "left": "13", "right": "22", "value": 15},
              {"id": "22", "left": None, "right": None, "value": 22},
              {"id": "13", "left": None, "right": "14", "value": 13},
              {"id": "14", "left": None, "right": None, "value": 14},
              {"id": "5", "left": "2", "right": "5-2", "value": 5},
              {"id": "5-2", "left": None, "right": None, "value": 5},
              {"id": "2", "left": "1", "right": None, "value": 2},
              {"id": "1", "left": None, "right": None, "value": 1}
            ],
            "root": "10"
          },
          "target": 12
        }
        return binary_tree.generate_test_bst(data), data["target"]

    @classmethod
    def _get_data_test_case_2(cls) -> (binary_tree.Node, int):
        data = {
          "tree": {
            "nodes": [
              {"id": "100", "left": "5", "right": "502", "value": 100},
              {"id": "502", "left": "204", "right": "55000", "value": 502},
              {"id": "55000", "left": "1001", "right": None, "value": 55000},
              {"id": "1001", "left": None, "right": "4500", "value": 1001},
              {"id": "4500", "left": None, "right": None, "value": 4500},
              {"id": "204", "left": "203", "right": "205", "value": 204},
              {"id": "205", "left": None, "right": "207", "value": 205},
              {"id": "207", "left": "206", "right": "208", "value": 207},
              {"id": "208", "left": None, "right": None, "value": 208},
              {"id": "206", "left": None, "right": None, "value": 206},
              {"id": "203", "left": None, "right": None, "value": 203},
              {"id": "5", "left": "2", "right": "15", "value": 5},
              {"id": "15", "left": "5-2", "right": "22", "value": 15},
              {"id": "22", "left": None, "right": "57", "value": 22},
              {"id": "57", "left": None, "right": "60", "value": 57},
              {"id": "60", "left": None, "right": None, "value": 60},
              {"id": "5-2", "left": None, "right": None, "value": 5},
              {"id": "2", "left": "1", "right": "3", "value": 2},
              {"id": "3", "left": None, "right": None, "value": 3},
              {"id": "1", "left": "-51", "right": "1-2", "value": 1},
              {"id": "1-2", "left": None, "right": "1-3", "value": 1},
              {"id": "1-3", "left": None, "right": "1-4", "value": 1},
              {"id": "1-4", "left": None, "right": "1-5", "value": 1},
              {"id": "1-5", "left": None, "right": None, "value": 1},
              {"id": "-51", "left": "-403", "right": None, "value": -51},
              {"id": "-403", "left": None, "right": None, "value": -403}
            ],
            "root": "100"
          },
          "target": 100
        }
        return binary_tree.generate_test_bst(data), data["target"]

    @classmethod
    def _get_data_test_case_3(cls) -> (binary_tree.Node, int):
        data = {
          "tree": {
            "nodes": [
              {"id": "100", "left": "5", "right": "502", "value": 100},
              {"id": "502", "left": "204", "right": "55000", "value": 502},
              {"id": "55000", "left": "1001", "right": None, "value": 55000},
              {"id": "1001", "left": None, "right": "4500", "value": 1001},
              {"id": "4500", "left": None, "right": None, "value": 4500},
              {"id": "204", "left": "203", "right": "205", "value": 204},
              {"id": "205", "left": None, "right": "207", "value": 205},
              {"id": "207", "left": "206", "right": "208", "value": 207},
              {"id": "208", "left": None, "right": None, "value": 208},
              {"id": "206", "left": None, "right": None, "value": 206},
              {"id": "203", "left": None, "right": None, "value": 203},
              {"id": "5", "left": "2", "right": "15", "value": 5},
              {"id": "15", "left": "5-2", "right": "22", "value": 15},
              {"id": "22", "left": None, "right": "57", "value": 22},
              {"id": "57", "left": None, "right": "60", "value": 57},
              {"id": "60", "left": None, "right": None, "value": 60},
              {"id": "5-2", "left": None, "right": None, "value": 5},
              {"id": "2", "left": "1", "right": "3", "value": 2},
              {"id": "3", "left": None, "right": None, "value": 3},
              {"id": "1", "left": "-51", "right": "1-2", "value": 1},
              {"id": "1-2", "left": None, "right": "1-3", "value": 1},
              {"id": "1-3", "left": None, "right": "1-4", "value": 1},
              {"id": "1-4", "left": None, "right": "1-5", "value": 1},
              {"id": "1-5", "left": None, "right": None, "value": 1},
              {"id": "-51", "left": "-403", "right": None, "value": -51},
              {"id": "-403", "left": None, "right": None, "value": -403}
            ],
            "root": "100"
          },
          "target": 208
        }
        return binary_tree.generate_test_bst(data), data["target"]

    @classmethod
    def _get_data_test_case_4(cls) -> (binary_tree.Node, int):
        data = {
          "tree": {
            "nodes": [
              {"id": "100", "left": "5", "right": "502", "value": 100},
              {"id": "502", "left": "204", "right": "55000", "value": 502},
              {"id": "55000", "left": "1001", "right": None, "value": 55000},
              {"id": "1001", "left": None, "right": "4500", "value": 1001},
              {"id": "4500", "left": None, "right": None, "value": 4500},
              {"id": "204", "left": "203", "right": "205", "value": 204},
              {"id": "205", "left": None, "right": "207", "value": 205},
              {"id": "207", "left": "206", "right": "208", "value": 207},
              {"id": "208", "left": None, "right": None, "value": 208},
              {"id": "206", "left": None, "right": None, "value": 206},
              {"id": "203", "left": None, "right": None, "value": 203},
              {"id": "5", "left": "2", "right": "15", "value": 5},
              {"id": "15", "left": "5-2", "right": "22", "value": 15},
              {"id": "22", "left": None, "right": "57", "value": 22},
              {"id": "57", "left": None, "right": "60", "value": 57},
              {"id": "60", "left": None, "right": None, "value": 60},
              {"id": "5-2", "left": None, "right": None, "value": 5},
              {"id": "2", "left": "1", "right": "3", "value": 2},
              {"id": "3", "left": None, "right": None, "value": 3},
              {"id": "1", "left": "-51", "right": "1-2", "value": 1},
              {"id": "1-2", "left": None, "right": "1-3", "value": 1},
              {"id": "1-3", "left": None, "right": "1-4", "value": 1},
              {"id": "1-4", "left": None, "right": "1-5", "value": 1},
              {"id": "1-5", "left": None, "right": None, "value": 1},
              {"id": "-51", "left": "-403", "right": None, "value": -51},
              {"id": "-403", "left": None, "right": None, "value": -403}
            ],
            "root": "100"
          },
          "target": 4500
        }
        return binary_tree.generate_test_bst(data), data["target"]

    @classmethod
    def _get_data_test_case_5(cls) -> (binary_tree.Node, int):
        data = {
          "tree": {
            "nodes": [
              {"id": "100", "left": "5", "right": "502", "value": 100},
              {"id": "502", "left": "204", "right": "55000", "value": 502},
              {"id": "55000", "left": "1001", "right": None, "value": 55000},
              {"id": "1001", "left": None, "right": "4500", "value": 1001},
              {"id": "4500", "left": None, "right": None, "value": 4500},
              {"id": "204", "left": "203", "right": "205", "value": 204},
              {"id": "205", "left": None, "right": "207", "value": 205},
              {"id": "207", "left": "206", "right": "208", "value": 207},
              {"id": "208", "left": None, "right": None, "value": 208},
              {"id": "206", "left": None, "right": None, "value": 206},
              {"id": "203", "left": None, "right": None, "value": 203},
              {"id": "5", "left": "2", "right": "15", "value": 5},
              {"id": "15", "left": "5-2", "right": "22", "value": 15},
              {"id": "22", "left": None, "right": "57", "value": 22},
              {"id": "57", "left": None, "right": "60", "value": 57},
              {"id": "60", "left": None, "right": None, "value": 60},
              {"id": "5-2", "left": None, "right": None, "value": 5},
              {"id": "2", "left": "1", "right": "3", "value": 2},
              {"id": "3", "left": None, "right": None, "value": 3},
              {"id": "1", "left": "-51", "right": "1-2", "value": 1},
              {"id": "1-2", "left": None, "right": "1-3", "value": 1},
              {"id": "1-3", "left": None, "right": "1-4", "value": 1},
              {"id": "1-4", "left": None, "right": "1-5", "value": 1},
              {"id": "1-5", "left": None, "right": None, "value": 1},
              {"id": "-51", "left": "-403", "right": None, "value": -51},
              {"id": "-403", "left": None, "right": None, "value": -403}
            ],
            "root": "100"
          },
          "target": 4501
        }
        return binary_tree.generate_test_bst(data), data["target"]

    @classmethod
    def _get_data_test_case_6(cls) -> (binary_tree.Node, int):
        data = {
          "tree": {
            "nodes": [
              {"id": "100", "left": "5", "right": "502", "value": 100},
              {"id": "502", "left": "204", "right": "55000", "value": 502},
              {"id": "55000", "left": "1001", "right": None, "value": 55000},
              {"id": "1001", "left": None, "right": "4500", "value": 1001},
              {"id": "4500", "left": None, "right": None, "value": 4500},
              {"id": "204", "left": "203", "right": "205", "value": 204},
              {"id": "205", "left": None, "right": "207", "value": 205},
              {"id": "207", "left": "206", "right": "208", "value": 207},
              {"id": "208", "left": None, "right": None, "value": 208},
              {"id": "206", "left": None, "right": None, "value": 206},
              {"id": "203", "left": None, "right": None, "value": 203},
              {"id": "5", "left": "2", "right": "15", "value": 5},
              {"id": "15", "left": "5-2", "right": "22", "value": 15},
              {"id": "22", "left": None, "right": "57", "value": 22},
              {"id": "57", "left": None, "right": "60", "value": 57},
              {"id": "60", "left": None, "right": None, "value": 60},
              {"id": "5-2", "left": None, "right": None, "value": 5},
              {"id": "2", "left": "1", "right": "3", "value": 2},
              {"id": "3", "left": None, "right": None, "value": 3},
              {"id": "1", "left": "-51", "right": "1-2", "value": 1},
              {"id": "1-2", "left": None, "right": "1-3", "value": 1},
              {"id": "1-3", "left": None, "right": "1-4", "value": 1},
              {"id": "1-4", "left": None, "right": "1-5", "value": 1},
              {"id": "1-5", "left": None, "right": None, "value": 1},
              {"id": "-51", "left": "-403", "right": None, "value": -51},
              {"id": "-403", "left": None, "right": None, "value": -403}
            ],
            "root": "100"
          },
          "target": -70
        }
        return binary_tree.generate_test_bst(data), data["target"]

    @classmethod
    def _get_data_test_case_7(cls) -> (binary_tree.Node, int):
        data = {
          "tree": {
            "nodes": [
              {"id": "100", "left": "5", "right": "502", "value": 100},
              {"id": "502", "left": "204", "right": "55000", "value": 502},
              {"id": "55000", "left": "1001", "right": None, "value": 55000},
              {"id": "1001", "left": None, "right": "4500", "value": 1001},
              {"id": "4500", "left": None, "right": None, "value": 4500},
              {"id": "204", "left": "203", "right": "205", "value": 204},
              {"id": "205", "left": None, "right": "207", "value": 205},
              {"id": "207", "left": "206", "right": "208", "value": 207},
              {"id": "208", "left": None, "right": None, "value": 208},
              {"id": "206", "left": None, "right": None, "value": 206},
              {"id": "203", "left": None, "right": None, "value": 203},
              {"id": "5", "left": "2", "right": "15", "value": 5},
              {"id": "15", "left": "5-2", "right": "22", "value": 15},
              {"id": "22", "left": None, "right": "57", "value": 22},
              {"id": "57", "left": None, "right": "60", "value": 57},
              {"id": "60", "left": None, "right": None, "value": 60},
              {"id": "5-2", "left": None, "right": None, "value": 5},
              {"id": "2", "left": "1", "right": "3", "value": 2},
              {"id": "3", "left": None, "right": None, "value": 3},
              {"id": "1", "left": "-51", "right": "1-2", "value": 1},
              {"id": "1-2", "left": None, "right": "1-3", "value": 1},
              {"id": "1-3", "left": None, "right": "1-4", "value": 1},
              {"id": "1-4", "left": None, "right": "1-5", "value": 1},
              {"id": "1-5", "left": None, "right": None, "value": 1},
              {"id": "-51", "left": "-403", "right": None, "value": -51},
              {"id": "-403", "left": None, "right": None, "value": -403}
            ],
            "root": "100"
          },
          "target": 2000
        }
        return binary_tree.generate_test_bst(data), data["target"]

    @classmethod
    def _get_data_test_case_8(cls) -> (binary_tree.Node, int):
        data = {
          "tree": {
            "nodes": [
              {"id": "100", "left": "5", "right": "502", "value": 100},
              {"id": "502", "left": "204", "right": "55000", "value": 502},
              {"id": "55000", "left": "1001", "right": None, "value": 55000},
              {"id": "1001", "left": None, "right": "4500", "value": 1001},
              {"id": "4500", "left": None, "right": None, "value": 4500},
              {"id": "204", "left": "203", "right": "205", "value": 204},
              {"id": "205", "left": None, "right": "207", "value": 205},
              {"id": "207", "left": "206", "right": "208", "value": 207},
              {"id": "208", "left": None, "right": None, "value": 208},
              {"id": "206", "left": None, "right": None, "value": 206},
              {"id": "203", "left": None, "right": None, "value": 203},
              {"id": "5", "left": "2", "right": "15", "value": 5},
              {"id": "15", "left": "5-2", "right": "22", "value": 15},
              {"id": "22", "left": None, "right": "57", "value": 22},
              {"id": "57", "left": None, "right": "60", "value": 57},
              {"id": "60", "left": None, "right": None, "value": 60},
              {"id": "5-2", "left": None, "right": None, "value": 5},
              {"id": "2", "left": "1", "right": "3", "value": 2},
              {"id": "3", "left": None, "right": None, "value": 3},
              {"id": "1", "left": "-51", "right": "1-2", "value": 1},
              {"id": "1-2", "left": None, "right": "1-3", "value": 1},
              {"id": "1-3", "left": None, "right": "1-4", "value": 1},
              {"id": "1-4", "left": None, "right": "1-5", "value": 1},
              {"id": "1-5", "left": None, "right": None, "value": 1},
              {"id": "-51", "left": "-403", "right": None, "value": -51},
              {"id": "-403", "left": None, "right": None, "value": -403}
            ],
            "root": "100"
          },
          "target": 6
        }
        return binary_tree.generate_test_bst(data), data["target"]

    @classmethod
    def _get_data_test_case_9(cls) -> (binary_tree.Node, int):
        data = {
          "tree": {
            "nodes": [
              {"id": "100", "left": "5", "right": "502", "value": 100},
              {"id": "502", "left": "204", "right": "55000", "value": 502},
              {"id": "55000", "left": "1001", "right": None, "value": 55000},
              {"id": "1001", "left": None, "right": "4500", "value": 1001},
              {"id": "4500", "left": None, "right": None, "value": 4500},
              {"id": "204", "left": "203", "right": "205", "value": 204},
              {"id": "205", "left": None, "right": "207", "value": 205},
              {"id": "207", "left": "206", "right": "208", "value": 207},
              {"id": "208", "left": None, "right": None, "value": 208},
              {"id": "206", "left": None, "right": None, "value": 206},
              {"id": "203", "left": None, "right": None, "value": 203},
              {"id": "5", "left": "2", "right": "15", "value": 5},
              {"id": "15", "left": "5-2", "right": "22", "value": 15},
              {"id": "22", "left": None, "right": "57", "value": 22},
              {"id": "57", "left": None, "right": "60", "value": 57},
              {"id": "60", "left": None, "right": None, "value": 60},
              {"id": "5-2", "left": None, "right": None, "value": 5},
              {"id": "2", "left": "1", "right": "3", "value": 2},
              {"id": "3", "left": None, "right": None, "value": 3},
              {"id": "1", "left": "-51", "right": "1-2", "value": 1},
              {"id": "1-2", "left": None, "right": "1-3", "value": 1},
              {"id": "1-3", "left": None, "right": "1-4", "value": 1},
              {"id": "1-4", "left": None, "right": "1-5", "value": 1},
              {"id": "1-5", "left": None, "right": None, "value": 1},
              {"id": "-51", "left": "-403", "right": None, "value": -51},
              {"id": "-403", "left": None, "right": None, "value": -403}
            ],
            "root": "100"
          },
          "target": 30000
        }
        return binary_tree.generate_test_bst(data), data["target"]

    @classmethod
    def _get_data_test_case_10(cls) -> (binary_tree.Node, int):
        data = {
          "tree": {
            "nodes": [
              {"id": "100", "left": "5", "right": "502", "value": 100},
              {"id": "502", "left": "204", "right": "55000", "value": 502},
              {"id": "55000", "left": "1001", "right": None, "value": 55000},
              {"id": "1001", "left": None, "right": "4500", "value": 1001},
              {"id": "4500", "left": None, "right": None, "value": 4500},
              {"id": "204", "left": "203", "right": "205", "value": 204},
              {"id": "205", "left": None, "right": "207", "value": 205},
              {"id": "207", "left": "206", "right": "208", "value": 207},
              {"id": "208", "left": None, "right": None, "value": 208},
              {"id": "206", "left": None, "right": None, "value": 206},
              {"id": "203", "left": None, "right": None, "value": 203},
              {"id": "5", "left": "2", "right": "15", "value": 5},
              {"id": "15", "left": "5-2", "right": "22", "value": 15},
              {"id": "22", "left": None, "right": "57", "value": 22},
              {"id": "57", "left": None, "right": "60", "value": 57},
              {"id": "60", "left": None, "right": None, "value": 60},
              {"id": "5-2", "left": None, "right": None, "value": 5},
              {"id": "2", "left": "1", "right": "3", "value": 2},
              {"id": "3", "left": None, "right": None, "value": 3},
              {"id": "1", "left": "-51", "right": "1-2", "value": 1},
              {"id": "1-2", "left": None, "right": "1-3", "value": 1},
              {"id": "1-3", "left": None, "right": "1-4", "value": 1},
              {"id": "1-4", "left": None, "right": "1-5", "value": 1},
              {"id": "1-5", "left": None, "right": None, "value": 1},
              {"id": "-51", "left": "-403", "right": None, "value": -51},
              {"id": "-403", "left": None, "right": None, "value": -403}
            ],
            "root": "100"
          },
          "target": -1
        }
        return binary_tree.generate_test_bst(data), data["target"]

    @classmethod
    def _get_data_test_case_11(cls) -> (binary_tree.Node, int):
        data = {
          "tree": {
            "nodes": [
              {"id": "100", "left": "5", "right": "502", "value": 100},
              {"id": "502", "left": "204", "right": "55000", "value": 502},
              {"id": "55000", "left": "1001", "right": None, "value": 55000},
              {"id": "1001", "left": None, "right": "4500", "value": 1001},
              {"id": "4500", "left": None, "right": None, "value": 4500},
              {"id": "204", "left": "203", "right": "205", "value": 204},
              {"id": "205", "left": None, "right": "207", "value": 205},
              {"id": "207", "left": "206", "right": "208", "value": 207},
              {"id": "208", "left": None, "right": None, "value": 208},
              {"id": "206", "left": None, "right": None, "value": 206},
              {"id": "203", "left": None, "right": None, "value": 203},
              {"id": "5", "left": "2", "right": "15", "value": 5},
              {"id": "15", "left": "5-2", "right": "22", "value": 15},
              {"id": "22", "left": None, "right": "57", "value": 22},
              {"id": "57", "left": None, "right": "60", "value": 57},
              {"id": "60", "left": None, "right": None, "value": 60},
              {"id": "5-2", "left": None, "right": None, "value": 5},
              {"id": "2", "left": "1", "right": "3", "value": 2},
              {"id": "3", "left": None, "right": None, "value": 3},
              {"id": "1", "left": "-51", "right": "1-2", "value": 1},
              {"id": "1-2", "left": None, "right": "1-3", "value": 1},
              {"id": "1-3", "left": None, "right": "1-4", "value": 1},
              {"id": "1-4", "left": None, "right": "1-5", "value": 1},
              {"id": "1-5", "left": None, "right": None, "value": 1},
              {"id": "-51", "left": "-403", "right": None, "value": -51},
              {"id": "-403", "left": None, "right": None, "value": -403}
            ],
            "root": "100"
          },
          "target": 29751
        }
        return binary_tree.generate_test_bst(data), data["target"]

    @classmethod
    def _get_data_test_case_12(cls) -> (binary_tree.Node, int):
        data = {
          "tree": {
            "nodes": [
              {"id": "100", "left": "5", "right": "502", "value": 100},
              {"id": "502", "left": "204", "right": "55000", "value": 502},
              {"id": "55000", "left": "1001", "right": None, "value": 55000},
              {"id": "1001", "left": None, "right": "4500", "value": 1001},
              {"id": "4500", "left": None, "right": None, "value": 4500},
              {"id": "204", "left": "203", "right": "205", "value": 204},
              {"id": "205", "left": None, "right": "207", "value": 205},
              {"id": "207", "left": "206", "right": "208", "value": 207},
              {"id": "208", "left": None, "right": None, "value": 208},
              {"id": "206", "left": None, "right": None, "value": 206},
              {"id": "203", "left": None, "right": None, "value": 203},
              {"id": "5", "left": "2", "right": "15", "value": 5},
              {"id": "15", "left": "5-2", "right": "22", "value": 15},
              {"id": "22", "left": None, "right": "57", "value": 22},
              {"id": "57", "left": None, "right": "60", "value": 57},
              {"id": "60", "left": None, "right": None, "value": 60},
              {"id": "5-2", "left": None, "right": None, "value": 5},
              {"id": "2", "left": "1", "right": "3", "value": 2},
              {"id": "3", "left": None, "right": None, "value": 3},
              {"id": "1", "left": "-51", "right": "1-2", "value": 1},
              {"id": "1-2", "left": None, "right": "1-3", "value": 1},
              {"id": "1-3", "left": None, "right": "1-4", "value": 1},
              {"id": "1-4", "left": None, "right": "1-5", "value": 1},
              {"id": "1-5", "left": None, "right": None, "value": 1},
              {"id": "-51", "left": "-403", "right": None, "value": -51},
              {"id": "-403", "left": None, "right": None, "value": -403}
            ],
            "root": "100"
          },
          "target": 29749
        }
        return binary_tree.generate_test_bst(data), data["target"]

    def test_case_1(self):
        (bst, target) = self.__class__._get_data_test_case_1()
        assert find_closest_value_in_bst(bst, target) == 13

    def test_case_2(self):
        (bst, target) = self.__class__._get_data_test_case_2()
        assert find_closest_value_in_bst(bst, target) == 100

    def test_case_3(self):
        (bst, target) = self.__class__._get_data_test_case_3()
        assert find_closest_value_in_bst(bst, target) == 208

    def test_case_4(self):
        (bst, target) = self.__class__._get_data_test_case_4()
        assert find_closest_value_in_bst(bst, target) == 4500

    def test_case_5(self):
        (bst, target) = self.__class__._get_data_test_case_5()
        assert find_closest_value_in_bst(bst, target) == 4500

    def test_case_6(self):
        (bst, target) = self.__class__._get_data_test_case_6()
        assert find_closest_value_in_bst(bst, target) == -51

    def test_case_7(self):
        (bst, target) = self.__class__._get_data_test_case_7()
        assert find_closest_value_in_bst(bst, target) == 1001

    def test_case_8(self):
        (bst, target) = self.__class__._get_data_test_case_8()
        assert find_closest_value_in_bst(bst, target) == 5

    def test_case_9(self):
        (bst, target) = self.__class__._get_data_test_case_9()
        assert find_closest_value_in_bst(bst, target) == 55_000

    def test_case_10(self):
        (bst, target) = self.__class__._get_data_test_case_10()
        assert find_closest_value_in_bst(bst, target) == 1

    def test_case_11(self):
        (bst, target) = self.__class__._get_data_test_case_11()
        assert find_closest_value_in_bst(bst, target) == 55_000

    def test_case_12(self):
        (bst, target) = self.__class__._get_data_test_case_12()
        assert find_closest_value_in_bst(bst, target) == 4500
