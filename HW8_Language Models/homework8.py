############################################################
# CIS 521: Language Models Homework 
############################################################

student_name = "Qihang Dai"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.

import random,string,math

############################################################
# Section 1: Markov Models
############################################################

def tokenize(text):
    text = text.strip()
    res = []
    lastword = []
    for char in text:
        if char in string.punctuation:
            if lastword:
                res.append(''.join(lastword))
            res.append(char)
            lastword = []
        elif char in string.whitespace:
            if lastword:
                res.append(''.join(lastword))
            lastword = []
        else:
            lastword.append(char)
    if lastword:
        res.append(''.join(lastword))
    return res
            

def ngrams(n, tokens):
    res = []
    for i in range(len(tokens)):
        if i < n - 1:
            pre = ('<START>',) * (n - 1 - i) + tuple(tokens[:i])
            res.append((pre, tokens[i]))
        else:
            res.append((tuple(tokens[i - n + 1:i]), tokens[i]))
    if n > 1:
        res.append((tuple(tokens[-n + 1:]), '<END>'))
    if n == 1:
        res.append(((), '<END>'))
    return res

# print(ngrams(3, ["a", "b", "c"]))
# print(ngrams(1, ["a", "b", "c"]))
        



class NgramModel(object):

    def __init__(self, n):
        self.n = n
        self.counts = {}

    def update(self, sentence):
        tokens = tokenize(sentence)
        ngrams_list = ngrams(self.n, tokens)
        for context, token in ngrams_list:
            if context not in self.counts:
                self.counts[context] = {}
            if token not in self.counts[context]:
                self.counts[context][token] = 1
            else:
                self.counts[context][token] += 1


    def prob(self, context, token):
        if context not in self.counts:
            return 0
        if token not in self.counts[context]:
            return 0
        return self.counts[context][token] / sum(self.counts[context].values())

    def random_token(self, context):
         tokens = sorted(self.counts[context].keys())
         r = random.random()
         cumlative_prob = 0
         for t in tokens:
            cumlative_prob += self.prob(context, t)
            if cumlative_prob >= r:
                return t

    def random_text(self, token_count):
        starter = ('<START>',) * (self.n - 1)
        tokens = []
        for i in range(token_count):
            token = self.random_token(starter)
            tokens.append(token)
            if token == '<END>':
                starter = ('<START>',) * (self.n - 1)
            elif self.n > 1:
                starter = starter[1:] + (token,)
                
        return ' '.join(tokens)


    def perplexity(self, sentence):
        tokens = tokenize(sentence)
        ngrams_list = ngrams(self.n, tokens)
        logprob = 0
        for context, token in ngrams_list:
            logprob += math.log(self.prob(context, token))
        return math.exp(-logprob / len(ngrams_list))

def create_ngram_model(n, path):
    model = NgramModel(n)
    with open(path, 'r') as f:
        for line in f:
            model.update(line)
    return model

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = 5

feedback_question_2 = """
understand the concept of n-gram model and how to implement it
"""

feedback_question_3 = """
would be nice to have some more pracitcal examples
"""
