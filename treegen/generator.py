from sklearn.tree import _tree
import numpy as np

class ClassifierTreeGenerator:

    @staticmethod
    def toPython(tree, feature_names):
        tree_ = tree.tree_
        feature_name = [
            feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
            for i in tree_.feature
        ]

        core_result = []

        def recurse(node, depth):
            indent = "  " * depth
            if tree_.feature[node] != _tree.TREE_UNDEFINED:
                name = feature_name[node]
                threshold = tree_.threshold[node]
                core_result.append("{}if({} <= {}):".format(indent, name, threshold))
                recurse(tree_.children_left[node], depth + 1)
                core_result.append("{}else: ".format(indent, name, threshold))
                recurse(tree_.children_right[node], depth + 1)
            else:
                core_result.append("{}return {}".format(indent, tree_.value[node]))

        recurse(0, 1)

        return "\n".join(core_result)

    @staticmethod
    def toPHP(tree, feature_names):
        tree_ = tree.tree_
        feature_name = [
            feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
            for i in tree_.feature
        ]

        core_result = []

        def recurse(node, depth):
            indent = "  " * depth

            if tree_.feature[node] != _tree.TREE_UNDEFINED:
                name = feature_name[node]
                threshold = tree_.threshold[node]
                core_result.append("{}if({} <= {}){{".format(indent, name, threshold))
                recurse(tree_.children_left[node], depth + 1)
                core_result.append("{} }}else{{  ".format(indent, name, threshold))
                recurse(tree_.children_right[node], depth + 1)
                core_result.append('{}}}'.format(indent))
            else: 
                core_result.append("{}  return {}; ".format(indent, np.argmax(tree_.value[node])))

        recurse(0, 1)

        return str("\n".join(core_result))

    @staticmethod
    def toSQL(tree, feature_names):
        tree_ = tree.tree_
        feature_name = [
            feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
            for i in tree_.feature
        ]

        core_result = []

        def recurse(node, depth):
            indent = "" * depth

            if tree_.feature[node] != _tree.TREE_UNDEFINED:
                name = feature_name[node]
                threshold = tree_.threshold[node]
                core_result.append("{}if({} <= {},".format(indent, name, threshold))
                recurse(tree_.children_left[node], depth + 1)
                core_result.append(", ".format(indent, name, threshold))
                recurse(tree_.children_right[node], depth + 1)
                core_result.append('{} )'.format(indent))
            else:
                core_result.append("{} {}  ".format(indent, np.argmax(tree_.value[node])))

        recurse(0, 1)

        return str("".join(core_result))
