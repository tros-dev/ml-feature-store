import numpy as np
from scipy.stats import ks_2samp

def detect_drift(reference_data: np.ndarray, current_data: np.ndarray, alpha=0.05):
    statistic, p_value = ks_2samp(reference_data, current_data)
    return p_value < alpha

