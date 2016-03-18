%module cufft

%{
    #define SWIG_FILE_WITH_INIT
    #include "cufft_cxxwrap.h"
%}

%include "numpy.i"

%init %{
    import_array();
%}

%apply (int DIM1, float* IN_ARRAY1) {(int Length1, float* Vector1)}
%apply (int DIM1, std::complex<float>* ARGOUT_ARRAY1) {(int Length2, std::complex<float>* Vector2)}

%include "cufft_cxxwrap.h"

%pythoncode %{
import numpy as np
def rfft(x):
  return _rfft(np.asarray(x, dtype=np.float32), len(x)/2+1)
%}