class KnowledgeBase:
    def __init__(self):
        self.facts = []
        self.rules = []

    def add_fact(self, fact):
        self.facts.append(fact)

    def add_rule(self, condition, conclusion):
        self.rules.append((condition, conclusion))

class ExpertSystem:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def infer(self):
        new_facts_found = True
        while new_facts_found:
            new_facts_found = False
            for condition, conclusion in self.knowledge_base.rules:
                if all(fact in self.knowledge_base.facts for fact in condition):
                    if conclusion not in self.knowledge_base.facts:
                        self.knowledge_base.facts.append(conclusion)
                        new_facts_found = True

# Creating the knowledge base
kb = KnowledgeBase()

# Adding facts
kb.add_fact("high fever")
kb.add_fact("cough")

# Adding rules
kb.add_rule(["high fever", "cough"], "respiratory infection")
kb.add_rule(["respiratory infection", "difficulty breathing"], "pneumonia")

# Creating the expert system
system = ExpertSystem(kb)

# Running inference
system.infer()

# Displaying the updated facts
print("Inferred facts:")
print(kb.facts)