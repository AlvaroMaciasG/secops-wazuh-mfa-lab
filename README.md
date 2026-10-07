# SecOps & Infrastructure Lab (Wazuh SIEM)

## Overview
End-to-end deployment of an isolated virtual infrastructure designed to validate defensive controls, centralize telemetry, and execute incident response lifecycles. 

## Architecture & Tech Stack
* **Deployment:** Docker & Docker Compose on Ubuntu Server.
* **Observability:** Wazuh SIEM (Manager, Indexer, Dashboard).
* **Network Security:** UFW, Fail2Ban, custom routing.
* **Automation:** Python scripting for network reconnaissance.

## Key Implementations
1. **Centralized Telemetry:** Engineered custom XML detection rules in Wazuh to parse web server access logs and identify specific threat vectors (e.g., SQL injections).
2. **Incident Response Playbooks:** Developed containment strategies following NIST SP 800-61 methodologies to manage simulated unauthorized access events.
3. **Python Automation:** Built custom socket-based scripts for automated port and service enumeration across the network segment.
