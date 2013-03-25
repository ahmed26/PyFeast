import numpy as np
from ctypes import * 

def select(data, labels, n_observations, n_features, n_select, method):
  
  selected_features = []

  try:
    libFSToolbox = CDLL("libFSToolbox.so"); 
  except:
    print "Error: could not find libFSToolbox"
    exit()

# JMI(n_features_to_ret, int n_samples, int n_feats, double *featureMatrix, double *classcol, outputFeatures);
  output = np.zeros(n_select)
  c_n_observations = c_int(n_observations)
  c_n_select = c_int(n_select)
  c_n_features = c_int(n_features)

  # right now just call only JMI, work out the rest later
  libFSToolbox.JMI(c_n_select,
                   c_n_observations,
                   c_n_features, 
                   data.ctypes.data_as(POINTER(c_double)),
                   labels.ctypes.data_as(POINTER(c_double)),
                   output.ctypes.data_as(POINTER(c_double))
                   )

  return selected_features