**Titanium Network Toolkit**

*Versatile Command-Line Network Analysis and Diagnostics Tool*

![License](https://img.shields.io/badge/license-MIT-blue)

---

**Description:**

The *Titanium Network Toolkit* is a powerful and user-friendly command-line tool designed for network analysis and diagnostics. This script provides various network-related functions, making it an invaluable utility for network administrators, developers, or anyone interested in troubleshooting network connectivity and domain-related issues.

**Features:**

- **Continuous ICMP Ping:** Monitor the availability and latency of a remote host with continuous ICMP ping. Press Ctrl+C to stop the pinging process.

- **Traceroute:** Trace the route taken by packets from your local machine to a destination host, displaying intermediate hops and response times.

- **DNS Lookup:** Retrieve DNS information for a given IP address or hostname, including a list of associated IP addresses and the hostname.

- **WHOIS Lookup:** Perform a WHOIS query to gather information about a domain name, including registration details, registrar, and name servers.

- **Get IP Information:** Retrieve detailed information about an IP address, including its country, region, city, ISP, hostname, and more.

---

**Usage:**

1. **Clone or Download:** Clone or download this repository to your local machine.

2. **Install Dependencies:** Install the required Python packages listed in the `requirements.txt` file using the following command:

pip install -r requirements.txt

markdown
Copy code

3. **Run the Script:** Execute the script by running the following command in your terminal:

python titanium_network_toolkit.py

vbnet
Copy code

4. **Select an Option:** Follow the on-screen prompts to choose the desired network tool and provide the necessary input.

**Example Usage:**

```bash
$ python titanium_network_toolkit.py
