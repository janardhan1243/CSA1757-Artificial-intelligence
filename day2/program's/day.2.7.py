import math

class DecisionTree:
    def __init__(self):
        self.tree = None

    def entropy(self, data):
        labels = [row[-1] for row in data]
        label_counts = {label: labels.count(label) for label in set(labels)}
        total = len(labels)
        return sum([-count/total * math.log2(count/total) for count in label_counts.values()])

    def information_gain(self, data, attribute_index):
        total_entropy = self.entropy(data)
        values = set([row[attribute_index] for row in data])
        weighted_entropy = 0
        for value in values:
            subset = [row for row in data if row[attribute_index] == value]
            weighted_entropy += (len(subset) / len(data)) * self.entropy(subset)
        return total_entropy - weighted_entropy

    def best_split(self, data):
        best_gain = 0
        best_attribute = None
        for attribute_index in range(len(data[0]) - 1):
            gain = self.information_gain(data, attribute_index)
            if gain > best_gain:
                best_gain = gain
                best_attribute = attribute_index
        return best_attribute

    def build_tree(self, data):
        if len(set([row[-1] for row in data])) == 1:
            return data[0][-1]
        if len(data[0]) == 1:
            return max(set([row[-1] for row in data]), key=[row[-1] for row in data].count)

        best_attribute = self.best_split(data)
        tree = {best_attribute: {}}
        values = set([row[best_attribute] for row in data])
        for value in values:
            subset = [row for row in data if row[best_attribute] == value]
            tree[best_attribute][value] = self.build_tree([row[:best_attribute] + row[best_attribute+1:] for row in subset])
        return tree

    def fit(self, data):
        self.tree = self.build_tree(data)

    def predict(self, row, tree=None):
        if tree is None:
            tree = self.tree
        if isinstance(tree, str):
            return tree
        attribute = list(tree.keys())[0]
        value = row[attribute]
        return self.predict(row, tree[attribute][value])

data = [
    [0, 0, 0, 'No'],
    [0, 0, 1, 'No'],
    [1, 0, 0, 'Yes'],
    [1, 1, 0, 'Yes'],
    [1, 1, 1, 'Yes'],
    [0, 1, 1, 'No'],
]

tree = DecisionTree()
tree.fit(data)

print("Decision Tree:", tree.tree)

test_row = [1, 0, 0]
print("Prediction for row [1, 0, 0]:", tree.predict(test_row))
