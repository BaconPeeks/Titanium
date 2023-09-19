# Description:
The Titanium Network Toolkit is a versatile command-line tool designed for network analysis and diagnostics. This script provides various network-related functions, including continuous ICMP ping, traceroute, DNS lookup, WHOIS lookup, and IP information retrieval. It's a handy utility for network administrators, developers, or anyone interested in troubleshooting network connectivity and domain-related issues.

Features:

Continuous ICMP Ping: Monitor the availability and latency of a remote host with continuous ICMP ping. Press Ctrl+C to stop the pinging process.
Traceroute: Trace the route taken by packets from your local machine to a destination host, displaying intermediate hops and response times.
DNS Lookup: Retrieve DNS information for a given IP address or hostname, including a list of associated IP addresses and the hostname.
WHOIS Lookup: Perform a WHOIS query to gather information about a domain name, including registration details, registrar, and name servers.
Get IP Information: Retrieve detailed information about an IP address, including its country, region, city, ISP, hostname, and more.
Usage:
Clone or download this repository to your local machine.
Install the required Python packages listed in the requirements.txt file using pip install -r requirements.txt.
Run the script by executing python titanium_network_toolkit.py in your terminal.
Follow the on-screen prompts to choose the desired network tool and provide the required input.
Example Usage:

ruby
Copy code
```$ python titanium_network_toolkit.py```
Requirements:
Python 3.x
Required Python packages (see requirements.txt for details)
Contributing:
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on GitHub.
