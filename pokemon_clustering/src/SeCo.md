# SeCo Framework for Choosing k in K-Means

This document explains the SeCo (Separation–Concordance) framework to help determine the optimal number of clusters (k) in K-Means through parallelised sampling and stability evaluation.

Summary

- Separation: Between-cluster sum-of-squares (higher = cleaner splits)
- Concordance: Median Cramer's V across the best solutions (higher = stable solutions)
- SeCo Plot: Scatter of Concordance vs Separation — pick the top-right zone

Prerequisites

pip install numpy pandas scikit-learn scipy joblib matplotlib

Code and explanation are included in the original project notebook. The notebook copies representative SeCo code and explains parameters such as `k_range`, `kmsamples`, and `topsep`.
