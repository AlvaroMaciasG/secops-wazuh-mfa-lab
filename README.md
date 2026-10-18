# SecOps & Linux IAM Lab (MSc Cybersecurity Final Project)

> **Context:** This repository contains the documentation and configurations for my Master's Degree Final Project in Cybersecurity. It demonstrates an end-to-end defensible network architecture, focusing on Security Operations (SecOps), centralized telemetry, and access control.

## 🎯 Overview
The objective of this lab is to build, monitor, and defend an isolated virtualized infrastructure. Instead of just focusing on offensive penetration testing, this project emphasizes the **Blue Team** perspective: ingesting logs into a SIEM, writing custom detection rules, responding to incidents, and hardening Linux servers with strict Identity and Access Management (IAM) controls.

## 🛠️ Architecture & Tech Stack
* **Observability & SIEM:** Wazuh (Manager, Indexer, Dashboard) deployed via Docker.
* **Linux IAM & Security:** Pluggable Authentication Modules (PAM), Google Authenticator (MFA), UFW (Firewall), Fail2Ban.
* **Vulnerability Management:** OpenVAS (GVM), OWASP ZAP.
* **Threat Simulation:** Kali Linux, Metasploit, Nmap, Python.

## 🛡️ Key Defenses & Implementations

### 1. Identity & Access Management (Linux IAM)
To protect the infrastructure against unauthorized access and brute-force attacks, strict IAM controls were implemented on the Ubuntu servers:
* **Multi-Factor Authentication (MFA):** Integrated `pam_google_authenticator.so` in the PAM control file (`/etc/pam.d/sshd`) to enforce OTP validation before password authentication.
* **Least Privilege:** Segmented administrative roles by creating standard users and restricting `root` access.
* **Service Hardening:** Enforced modern MAC algorithms for SSH tunnels and disabled outdated cryptographic protocols.

### 2. SecOps & Centralized Telemetry (Wazuh SIEM)
* **Log Ingestion:** Deployed Wazuh agents across the infrastructure to centralize `auth.log` and `access.log` telemetry.
* **Custom Detection Rules:** Engineered custom XML rules in Wazuh's correlation engine (Rule ID: 100050) to parse Apache web server logs and detect active SQL Injection attacks.
* **Incident Response:** Developed a SOC playbook (UC-SOC-001) for containment, successfully demonstrating an active response workflow (dynamic IP blocking) when a threat is detected.

### 3. Threat Simulation & Vulnerability Management
To validate the defensive controls, controlled attacks were executed following OSSTMM and PTES methodologies:
* Exploited a critical backdoor (CVE-2011-2523) and Web vulnerabilities (SQLi) to test SIEM alerting.
* Conducted post-exploitation simulations (evidence deletion, pivoting) to audit the resilience of the logging architecture.
