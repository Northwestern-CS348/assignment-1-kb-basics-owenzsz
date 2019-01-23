import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        if isinstance(fact, Fact):
            if fact not in self.facts:
                self.facts.append(fact)
                # if the fact/rule is already in the list, do not append
                #if the input is a fact, append to the fact list
        if isinstance(fact, Rule):
            if fact not in self.rules:
                self.rules.append(fact) #if it's a rule, append it to the rule list
        print("Asserting {!r}".format(fact))
        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        ans = ListOfBindings()
        arr = []
        for existingFact in self.facts:
            if match(existingFact.statement, fact.statement)!=False: #find if there is any match in the current facts
                arr.append(existingFact) #if yes, append it to the empty array for future use
                ans.add_bindings(match(existingFact.statement, fact.statement), arr) #append the matches to the listofbindings
        return ans
        print("Asking {!r}".format(fact))
