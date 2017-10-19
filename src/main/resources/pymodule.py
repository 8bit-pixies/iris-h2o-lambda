from __future__ import division
from hex.genmodel.easy import RowData
from hex.genmodel.easy import EasyPredictModelWrapper
from java.lang import Math
import irisModel
#import NamesHolder_irisModel
#from collections import Counter


def feature_preprocessing(c0, c1, c2, c3):
  return c0, c1, c2, c3

def predict(c0, c1, c2, c3):
  # add feat preprocessing here
  c0, c1, c2, c3 = feature_preprocessing(c0, c1, c2, c3)
  
  row = RowData()
  row.put('c0', c0)
  row.put('c1', c1)
  row.put('c2', c2)
  row.put('c3', c3)

  #prediction
  model = EasyPredictModelWrapper(irisModel())
  p = model.predict(row)

  #[label, class0Prob, class1Prob], [intercept], [features] = 3 + 1 + x
  return [float(p.label), p.classProbabilities[0], p.classProbabilities[1], p.classProbabilities[2]]

