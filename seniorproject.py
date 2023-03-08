
import numpy as np

def anomaly_detection(data, sigma_threshold=5):
    "Detects anomalies in the dataset provided using the sigma rule"

    sigma = np.std(data)
    mean = np.mean(data)
    anomalies = []
    for i in range(len(data)):
        if abs(data[i] - mean) > sigma_threshold * sigma:
            anomalies.append(data[i])
            return anomalies

def test_anomaly_detection():
    "Tests the anomaly detection function."

    data = list(np.random.randn(1000))
    data = data + [10]
    anomalies = anomaly_detection(data)
    print(anomalies)