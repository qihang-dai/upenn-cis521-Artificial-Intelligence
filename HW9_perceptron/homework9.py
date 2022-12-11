############################################################
# CIS 521: Perceptrons Homework
############################################################

student_name = "Qihang Dai"

############################################################
# Imports
############################################################

import perceptrons_data as data

# Include your imports here, if any are used.



############################################################
# Section 1: Perceptrons
############################################################

class BinaryPerceptron(object):

    def __init__(self, examples, iterations):
        self.weights = {}
        for example in examples:
            for feature in example[0]:
                self.weights[feature] = 0
        
        for i in range(iterations):
            for example in examples:
                x = example[0]
                y = example[1]
                y_hat = self.predict(x)
                if y_hat != y:
                    for feature in x:
                        if y:
                            self.weights[feature] += x[feature]
                        else:
                            self.weights[feature] -= x[feature]



    def predict(self, x):
        res = 0
        for feature in x:
            res += self.weights[feature] * x[feature]
        if res > 0:
            return True
        else:
            return False

class MulticlassPerceptron(object):

    def __init__(self, examples, iterations):
        self.weights = {}
        for x, y in examples:
            if y not in self.weights:
                self.weights[y] = {}
                for feature in x:
                    self.weights[y][feature] = 0

        for i in range(iterations):
            for x, y in examples:
                y_hat = self.predict(x)
                if y_hat != y:
                    for feature in x:
                        self.weights[y][feature] += x[feature]
                        self.weights[y_hat][feature] -= x[feature]


    def predict(self, x):
        max_val = float('-inf')
        max_label = None
        for label in self.weights:
            res = 0
            for feature in x: 
                if feature not in self.weights[label]:
                    self.weights[label][feature] = 0
                res += self.weights[label][feature] * x[feature]
            if res > max_val:
                max_val = res
                max_label = label
        return max_label


############################################################
# Section 2: Applications
############################################################

class IrisClassifier(object):

    def __init__(self, data):
        train_data = []
        for x, y in data:
            hashmap = {}
            for i in range(len(x)):
                hashmap[i] = x[i]
            train_data.append((hashmap, y))
        self.perceptron = MulticlassPerceptron(train_data, 25)


    def classify(self, instance):
        hashmap = {}
        for i in range(len(instance)):
            hashmap[i] = instance[i]
        return self.perceptron.predict(hashmap)

class DigitClassifier(object):

    def __init__(self, data):
        train_data = []
        for x, y in data:
            hashmap = {}
            for i in range(len(x)):
                hashmap[i] = x[i]
            train_data.append((hashmap, y))
        self.perceptron = MulticlassPerceptron(train_data, 15)

    def classify(self, instance):
        hashmap = {}
        for i in range(len(instance)):
            hashmap[i] = instance[i]
        return self.perceptron.predict(hashmap)

class BiasClassifier(object):

    def __init__(self, data):
        train_data = []
        for x, y in data:
            hashmap = {}
            hashmap[0] = x - 1
            train_data.append((hashmap, y))
        self.perceptron = BinaryPerceptron(train_data, 5)

    def classify(self, instance):
        hashmap = {}
        hashmap[0] = instance - 1
        return self.perceptron.predict(hashmap)

class MysteryClassifier1(object):

    def __init__(self, data):
        train_data = []
        for x, y in data:
            hashmap = {}
            hashmap[0] = x[0] * x[0] + x[1] * x[1] - 4
            train_data.append((hashmap, y))
        self.perceptron = BinaryPerceptron(train_data, 5)
            

    def classify(self, instance):
        hashmap = {}
        hashmap[0] = instance[0] * instance[0] + instance[1] * instance[1] - 4
        return self.perceptron.predict(hashmap)

class MysteryClassifier2(object):

    def __init__(self, data):
        train_data = []
        for x, y in data:
            hashmap = {}
            hashmap[0] = x[0] * x[1] * x[2]
            train_data.append((hashmap, y))
        self.perceptron = BinaryPerceptron(train_data, 5)

    def classify(self, instance):
        hashmap = {}
        hashmap[0] = instance[0] * instance[1] * instance[2]
        return self.perceptron.predict(hashmap)

############################################################
# Section 3: Feedback
############################################################

feedback_question_1 = 5

feedback_question_2 = """
Not sure about this one.
"""

feedback_question_3 = """
None of them.
"""
