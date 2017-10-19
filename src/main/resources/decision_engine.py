def decision_engine(p):
    """
    Takes in the prediction object and prettifies it
    to be consumed by the outbound payload
    """
    return [float(p.label), 
    p.classProbabilities[0], 
    p.classProbabilities[1], 
    p.classProbabilities[2]]