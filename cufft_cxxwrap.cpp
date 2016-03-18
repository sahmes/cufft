#include <cstdio>
#include <complex>
#include <cufft.h>
#include "cufft_cxxwrap.h"

void cufft_core_execute(float* Signal, int N, float2* SignalFFT);
void _rfft(int Length1, float* Vector1, int Length2, std::complex<float>* Vector2) {
    cufft_core_execute(Vector1, Length1, (float2*)Vector2);
}
