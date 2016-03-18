#include <cmath>
#include <cufft.h>

void cufft_core_execute(float* Signal_h, int Size, float2* SignalFFT_h) {
    float *Signal_d;
    float2 *SignalFFT_d;
    cudaMalloc((void**)&Signal_d, Size*sizeof(float));
    cudaMalloc((void**)&SignalFFT_d, (Size/2+1)*sizeof(float2));
    cudaMemcpy(Signal_d, Signal_h, Size*sizeof(float), cudaMemcpyHostToDevice);
    cufftHandle Plan;
    cufftPlan1d(&Plan, Size, CUFFT_R2C, 1);
    cufftExecR2C(Plan, (cufftReal*)Signal_d, (cufftComplex*)SignalFFT_d);
    cudaMemcpy(SignalFFT_h, SignalFFT_d, (Size/2+1)*sizeof(float2), cudaMemcpyDeviceToHost);
    cudaFree(Signal_d);
    cudaFree(SignalFFT_d);
}