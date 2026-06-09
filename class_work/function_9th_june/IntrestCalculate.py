# Simple interest calculation
def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest
# Compound interest calculation
def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    interest = amount - principal
    return interest