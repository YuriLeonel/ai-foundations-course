import numpy as np
from scipy.stats import norm
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# 1. Creating a Bayesian Network to model the problem
model = DiscreteBayesianNetwork([
    ('PurchaseHistory', 'Purchase'),
    ('TimeOnSite', 'Purchase'),
    ('ClickedPromotion', 'Purchase')
])

# 2. Defining conditional probabilities (CPDs)
cpd_history = TabularCPD(variable='PurchaseHistory', variable_card=2, values=[[0.7], [0.3]])
cpd_time = TabularCPD(variable='TimeOnSite', variable_card=2, values=[[0.6], [0.4]])
cpd_promotion = TabularCPD(variable='ClickedPromotion', variable_card=2, values=[[0.8], [0.2]])

# Purchase is influenced by other variables
cpd_purchase = TabularCPD(
    variable='Purchase',
    variable_card=2,
    values=[
        [0.9, 0.7, 0.8, 0.4, 0.6, 0.2, 0.3, 0.1],  # Probability of not purchasing
        [0.1, 0.3, 0.2, 0.6, 0.4, 0.8, 0.7, 0.9]   # Probability of purchasing
    ],
    evidence=['PurchaseHistory', 'TimeOnSite', 'ClickedPromotion'],
    evidence_card=[2, 2, 2]
)

# 3. Adding CPDs to the model
model.add_cpds(cpd_history, cpd_time, cpd_promotion, cpd_purchase)

# 4. Validating the model
assert model.check_model()

# 5. Predicting purchase probability given a scenario
inference = VariableElimination(model)
result = inference.query(variables=['Purchase'], evidence={
    'PurchaseHistory': 1,  # The customer has purchase history
    'TimeOnSite': 0,       # The customer spent little time on the site
    'ClickedPromotion': 1   # The customer clicked on a promotion
})

print("Purchase Probabilities:")
print(result) # Result of the probability of purchasing or not purchasing based on evidence

# 6. Exploring distributions to model additional uncertainty
# Example: time on site follows a normal distribution
mean_time = 5  # minutes
std_time = 2
observed_time = 6
time_prob = norm.cdf(observed_time, loc=mean_time, scale=std_time)

print(f"Probability of the customer spending less than {observed_time} minutes on the site: {time_prob:.2f}")