from hex.genmodel.easy import RowData
from hex.genmodel.easy import EasyPredictModelWrapper
from java.lang import Math
import irisModel
import NamesHolder_irisModel
from feature_preprocessing import feature_preprocessing
from decision_engine import decision_engine

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

def pipeline(*argv):
    # add feat preprocessing here
    ls = feature_preprocessing(*argv)
    
    # prediction portion
    p = predict(ls)
    
    # post processing here...if required
    res = decision_engine(p)
    return res

