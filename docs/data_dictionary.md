# 📊 Data Dictionary — Network Traffic Dataset

## 📌 Overview

This dataset contains **25,192 network traffic records** with **42 features**. It is commonly used for cybersecurity analysis, particularly for anomaly and intrusion detection tasks.

The features represent different aspects of network connections, including traffic behavior, connection patterns, and error rates.

---

## 📂 Feature Definitions

| Feature Name                | Data Type   | Description                                                   |
| --------------------------- | ----------- | ------------------------------------------------------------- |
| duration                    | Numeric     | Length of the connection (in seconds)                         |
| protocol_type               | Categorical | Type of protocol (e.g., TCP, UDP, ICMP)                       |
| service                     | Categorical | Network service on the destination (e.g., HTTP, FTP)          |
| flag                        | Categorical | Status flag of the connection                                 |
| src_bytes                   | Numeric     | Number of data bytes sent from source to destination          |
| dst_bytes                   | Numeric     | Number of data bytes sent from destination to source          |
| land                        | Binary      | 1 if connection is from/to the same host/port; else 0         |
| wrong_fragment              | Numeric     | Number of wrong fragments                                     |
| urgent                      | Numeric     | Number of urgent packets                                      |
| hot                         | Numeric     | Number of “hot” indicators (suspicious activity)              |
| num_failed_logins           | Numeric     | Number of failed login attempts                               |
| logged_in                   | Binary      | 1 if successfully logged in; else 0                           |
| num_compromised             | Numeric     | Number of compromised conditions                              |
| root_shell                  | Binary      | 1 if root shell is obtained                                   |
| su_attempted                | Numeric     | Number of “su root” attempts                                  |
| num_root                    | Numeric     | Number of root accesses                                       |
| num_file_creations          | Numeric     | Number of file creation operations                            |
| num_shells                  | Numeric     | Number of shell prompts invoked                               |
| num_access_files            | Numeric     | Number of operations on access control files                  |
| num_outbound_cmds           | Numeric     | Number of outbound commands (usually 0)                       |
| is_host_login               | Binary      | 1 if login belongs to host list                               |
| is_guest_login              | Binary      | 1 if login is a guest login                                   |
| count                       | Numeric     | Number of connections to the same host in past 2 seconds      |
| srv_count                   | Numeric     | Number of connections to the same service in past 2 seconds   |
| serror_rate                 | Numeric     | % of connections with SYN errors                              |
| srv_serror_rate             | Numeric     | % of connections with SYN errors (same service)               |
| rerror_rate                 | Numeric     | % of connections with REJ errors                              |
| srv_rerror_rate             | Numeric     | % of REJ errors (same service)                                |
| same_srv_rate               | Numeric     | % of connections to the same service                          |
| diff_srv_rate               | Numeric     | % of connections to different services                        |
| srv_diff_host_rate          | Numeric     | % of connections to different hosts                           |
| dst_host_count              | Numeric     | Number of connections to the same destination host            |
| dst_host_srv_count          | Numeric     | Number of connections to the same service on destination host |
| dst_host_same_srv_rate      | Numeric     | % of connections to same service                              |
| dst_host_diff_srv_rate      | Numeric     | % of connections to different services                        |
| dst_host_same_src_port_rate | Numeric     | % of connections from same source port                        |
| dst_host_srv_diff_host_rate | Numeric     | % of connections to different hosts                           |
| dst_host_serror_rate        | Numeric     | % of SYN errors for destination host                          |
| dst_host_srv_serror_rate    | Numeric     | % of SYN errors (same service)                                |
| dst_host_rerror_rate        | Numeric     | % of REJ errors                                               |
| dst_host_srv_rerror_rate    | Numeric     | % of REJ errors (same service)                                |
| class                       | Categorical | Label indicating normal or attack type                        |

---

## 📊 Feature Categories

### 🔹 Traffic Features

* `src_bytes`, `dst_bytes`
* Represent volume of data transferred

### 🔹 Connection Features

* `count`, `srv_count`
* Capture frequency of connections

### 🔹 Login & Access Features

* `num_failed_logins`, `logged_in`, `root_shell`
* Indicate authentication behavior

### 🔹 Error Rate Features

* `serror_rate`, `rerror_rate`, etc.
* Measure abnormal connection responses

### 🔹 Host-Based Features

* `dst_host_*`
* Capture patterns over longer time windows

---

## 🎯 Target Variable

| Column | Description                                                    |
| ------ | -------------------------------------------------------------- |
| class  | Indicates whether the connection is normal or a type of attack |

---

## 📌 Notes

* Dataset contains both **numerical and categorical features**
* Some features are **binary indicators (0 or 1)**
* Error rate features are typically **ratios (0–1 range)**
* Highly suitable for:

  * Anomaly Detection
  * Intrusion Detection Systems (IDS)
  * Network Behavior Analysis

---

## ⚠️ Considerations

* Some features may be **highly correlated**
* Data is **imbalanced in real scenarios**
* Feature scaling is required for distance-based models
* Labels (`class`) are not used in unsupervised training but can be used for evaluation

---

## ✅ Summary

This dataset provides a comprehensive view of network activity and is well-suited for detecting unusual patterns. The combination of traffic, connection, and error-based features allows machine learning models to identify anomalies effectively.
