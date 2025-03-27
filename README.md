<p align="center">
  <img src="./images/LDP^3.png" alt="Repository Logo" width="200"/>
</p>
<h1 align="center">Local Differential Privacy with Post Processing - LDP³</h1>

This repository contains a snapshot of the code for LDP³: a comprehensive post-processing toolkit for Local Differential Privacy (LDP). LDP³ integrates multiple post-processing techniques to enhance the utility of privatized data while maintaining strong privacy guarantees. It also includes evaluation metrics and benchmarking tools to assess different LDP protocols and post-processing strategies. Our works on LDP³ provide insights into improving the usability of LDP-collected data across various applications: 

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
- **Randomized Aggregatable Privacy-Preserving Ordinal Response (RAPPOR)**  
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
This directory contains scripts for loading and preprocessing the dataset to be used in the experiments.  

### **utils**  
This directory includes utility scripts for input parsing, result formatting, and other helper functions used throughout the toolkit.  

### **ldpcube.py**  
The main script to execute the LDP³ toolkit, integrating LDP protocols, post-processing methods, and evaluation metrics in a multi-threaded manner.  

## Dependencies
Our code is implemented and tested on Python 3.12. Our code uses the following packages.
- `numpy==2.1.3`  
- `tabulate==0.9.0`
- `xxhash==3.5.0` 

## Running the Code

To execute the program, use the following command:

```sh
python3 ldpcube.py -e EPSILON -p PROTOCOLS -m METHODS -r REPEAT -t THREAD_NUMBER -d DATASET -u UTILITY_METRIC
```

### Command-Line Arguments

- `-e EPSILON`: Specifies the privacy budget ε.
- `-p PROTOCOLS`: Defines the LDP protocol(s) to use. Possible protocols are those implemented in the Protocol Module. Multiple protocols can be specified, or use `"all"` to run experiments with all available protocols.
- `-m METHODS`: Defines the post-processing (PP) method(s) to use. Available methods are those in the Post-Processing Module. Multiple methods can be specified, or use `"all"` to run experiments with all available methods.
- `-r REPEAT`: Specifies the number of repetitions per experiment to account for the randomness of LDP and ensure statistical significance (e.g., `10`).
- `-t THREAD_NUMBER`: Defines the number of parallel threads for multi-threaded execution.
- `-d DATASET`: Specifies the dataset file path (e.g., `my_dataset.csv`). The dataset should contain rows of values where each row corresponds to one user's data. The dataset parser can be modified to support different formats.
- `-u UTILITY_METRIC`: Specifies the utility metric to evaluate errors, selected from those implemented in the Utility Measurement Module.

### Example Usage

```sh
python3 ldpcube.py -e 1.0 -p rappor -m norm-sub -r 10 -t 4 -d data.csv -u l1
```

This command runs the program with:
- `ε = 1.0`
- `rappor` as the LDP protocol
- `norm-sub` as the PP method
- 10 repetitions per experiment
- 4 parallel threads
- `data.csv` as the dataset
- `l1` (L1 Distance) as the utility metric

If you use our code, please cite:

```
@inproceedings{khodaie2025benchmark,
  title={Post-Processing in Local Differential Privacy: An Extensive Evaluation and Benchmark Platform},
  author={Khodaie, Alireza and Balioglu, Berkay Kemal and Gursoy, M. Emre},
  booktitle={Proceedings of the 40th International Conference on ICT Systems Security and Privacy Protection (IFIP SEC 2025)},
  year={2025},
  organization={IFIP TC-11}
}
```

```
@inproceedings{balioglu2025ldpcube,
  title={LDP³: An Extensible and Multi-Threaded Toolkit for Local Differential Privacy Protocols and Post-Processing Methods},
  author={Balioglu, Berkay Kemal and Khodaie, Alireza and Gursoy, M. Emre},
  booktitle={IEEE International Conference on Cyber Security and Resilience (IEEE CSR 2025)},
  year={2025},
  organization={IEEE CSR}
}
```
