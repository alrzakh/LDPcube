<div style="position: absolute; top: 0; right: 0;">
  <img src="./images/LDP^3.png" alt="Repository Logo" width="200"/>
</div>


# Local Differential Privacy with Post Processing - LDP³

This repository contains a snapshot of the code for LDP³: a comprehensive post-processing framework for Local Differential Privacy (LDP). LDP³ integrates multiple post-processing techniques to enhance the utility of privatized data while maintaining strong privacy guarantees. It also includes evaluation metrics and benchmarking tools to assess different LDP protocols and post-processing strategies. Our works on LDP³ provide insights into improving the usability of LDP-collected data across various applications: 

```
LDP³: An Extensible and Multi-Threaded Toolkit for Local Differential Privacy Protocols and Post-Processing Methods
Balioglu, B.K., Khodaie, A. & Gursoy, M.E. 
```

```
Post-Processing in Local Differential Privacy: An Extensive Evaluation and Benchmark Platform
Khodaie, A., Balioglu, B.K. & Gursoy, M.E.
In Proceedings of the 40th International Conference on ICT Systems Security and Privacy Protection (IFIP SEC 2025)
```

## Contents

### **protocols**  
This directory contains implementations of six state-of-the-art Local Differential Privacy (LDP) protocols:  
- **Generalized Randomized Response (GRR)**  
- **Binary Local Hashing (BLH)**  
- **Optimized Local Hashing (OLH)**  
- **simple-RAPPOR**  
- **Optimized Unary Encoding (OUE)**  
- **Subset Selection (SS)**  

### **post_processing**  
This directory includes seven widely used post-processing methods for improving the utility of LDP-collected data:  
- **Base-Pos**  
- **Norm**  
- **Norm-Mul**  
- **Norm-Sub**  
- **Norm-Cut**  
- **Power**  
- **Power-NS**  

### **metrics**  
We provide implementations of four different error metrics to evaluate the performance of LDP protocols and post-processing techniques:  
- **L1 Distance**  
- **L2 Distance**  
- **Kullback-Leibler (KL) Divergence**  
- **Earth Mover's Distance (EMD)**  

### **data_loader**  
This directory contains scripts for loading and preprocessing datasets used in the experiments.  

### **utils**  
This directory includes utility scripts for input parsing, result formatting, and other helper functions used throughout the toolkit.  

### **ldpcube.py**  
The main script to execute the LDP³ toolkit, integrating LDP protocols, post-processing methods, and evaluation metrics.  

## Dependencies

## Guide


