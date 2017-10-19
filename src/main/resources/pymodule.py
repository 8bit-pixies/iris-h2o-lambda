from hex.genmodel.easy import RowData
from hex.genmodel.easy import EasyPredictModelWrapper
from java.lang import Math
import irisModel
import NamesHolder_irisModel

def feature_preprocessing(c0, c1, c2, c3):
    print("feature preprocessing complete...!")
    return c0, c1, c2, c3

def predict(vals):
    """
    The predict function - you generally do not have to 
    touch this component
    """
    row = RowData()  
    names = NamesHolder_irisModel().VALUES
    for idx, nm in enumerate(names):
        row.put(nm, vals[idx])
    
    # prediction portion
    model = EasyPredictModelWrapper(irisModel())
    p = model.predict(row)
    print("predict complete...!")
    return p

def decision_engine(p):
    """
    Takes in the prediction object and prettifies it
    to be consumed by the outbound payload
    """
    return [float(p.label), 
    p.classProbabilities[0], 
    p.classProbabilities[1], 
    p.classProbabilities[2]]

def pipeline(*argv):
    # add feat preprocessing here
    ls = feature_preprocessing(*argv)
    
    # prediction portion
    p = predict(ls)
    
    # post processing here...if required
    res = decision_engine(p)
    return res

