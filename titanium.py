
import requests
from rich.console import Console
import whois
from traceroute import traceroute
from ping3 import ping
import os
import time
import socket

console = Console()

Lol = "https://pastebin.com/raw/gJQ840Pz"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def check_backend():
    try:
        response = requests.get(Lol)
        response.raise_for_status()
        return response.text.strip().lower() == "true"
    except requests.exceptions.RequestException:
        return False


def continuous_ping(host):
    clear_screen()
    console.print(
        f"Pinging {host} continuously. Press [green]Ctrl+C[/green] to stop.")

    try:
        while True:
            timestamp = time.strftime("[%H:%M:%S]")
            # Set a longer timeout (in seconds)
            ping_result = ping(host, timeout=3)

            if ping_result is not None:
                console.log(
                    f"{timestamp} Ping to {host}: [green]{ping_result:.3f} ms[/green]")
            else:
                console.log(f"{timestamp} Ping to {host}: [red]Timeout[/red]")

            time.sleep(0.8)  # Introduce a delay of 1 second between pings
    except KeyboardInterrupt:
        console.print("\n[red]Ping stopped by user.[/red]")


def lookup_whois(domain):
    clear_screen()
    console.print(f"Looking up WHOIS for {domain}...")

    try:
        whois_info = whois.whois(domain)

        console.print(f"Domain Name: {whois_info.domain_name}")
        console.print(f"Registrar: {whois_info.registrar}")
        console.print(f"WHOIS Server: {whois_info.whois_server}")
        console.print(f"Creation Date: {whois_info.creation_date}")
        console.print(f"Expiration Date: {whois_info.expiration_date}")
        console.print(f"Updated Date: {whois_info.updated_date}")
        console.print(f"Name Servers: {whois_info.name_servers}")

    except Exception as e:
        console.print(f"[red]Failed to lookup WHOIS: {e}[/red]")


def lookup_dns(host):
    clear_screen()
    console.print(f"Looking up DNS for {host}...")

    try:
        addr_info = socket.getaddrinfo(host, None)
        ip_list = []
        for addr in addr_info:
            ip = addr[4][0]
            ip_list.append(ip)

        name_info = socket.getnameinfo(addr_info[0][4], 0)
        hostname = name_info[0]

        console.print(f"[green]{host} resolves to:")
        for ip in ip_list:
            console.print(f"- {ip}")
        console.print(f"[green]Hostname: {hostname}[/green]")

    except socket.gaierror as e:
        console.print(f"[red]Failed to resolve DNS: {e}[/red]")


def traceroute(host):
    clear_screen()
    console.print(f"Tracing route to {host}...")

    try:
        route = traceroute(host)
        for hop in route:
            console.print(
                f"{hop['hop']} {hop['ip']} {hop['hostname']} {hop['avg_rtt']}ms")
    except:
        console.print(f"[red]Failed to trace route to {host}[/red]")


def check_host_info(ip_address):
    clear_screen()
    headers = {"Accept": "application/json"}
    api_url = f"https://ipinfo.io/{ip_address}/json"

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()

        data = response.json()
        console.print(
            f"\nIP Information for host [green]{data['ip']}[/green]:")
        console.print(f"Country: [green]{data.get('country', 'N/A')}[/green]")
        console.print(f"Region: [green]{data.get('region', 'N/A')}[/green]")
        console.print(f"City: [green]{data.get('city', 'N/A')}[/green]")
        console.print(f"ISP: [green]{data.get('org', 'N/A')}[/green]")
        console.print(
            f"Hostname: [green]{data.get('hostname', 'N/A')}[/green]")
        console.print(f"Anycast: [green]{data.get('anycast', 'N/A')}[/green]")
        console.print(
            f"Location (Lat, Long): [green]{data.get('loc', 'N/A')}[/green]")
        console.print(
            f"Postal Code: [green]{data.get('postal', 'N/A')}[/green]")
        console.print(
            f"Timezone: [green]{data.get('timezone', 'N/A')}[/green]")
    except requests.exceptions.RequestException as e:
        console.print(f"[red]Error while fetching IP information: {e}[/red]")


def main():
    if not check_backend():
        console.print("[red]Killswitch is active. Exiting the tool.[/red]")
        return

    clear_screen()
    console.print("[bold]Titanium[/bold]\n")

    console.print("[cyan]1.[/cyan] Continuous ICMP Ping")
    console.print("[cyan]2.[/cyan] Traceroute")
    console.print("[cyan]3.[/cyan] DNS Lookup")
    console.print("[cyan]4.[/cyan] WHOIS Lookup")
    console.print("[cyan]5.[/cyan] Get IP Information")
    console.print("")

    choice = input("Select an option (1/2/3/4/5): ")

    if choice == "1":
        clear_screen()
        console.print("[bold]Continuous ICMP Ping Tool[/bold]\n")
        host = input("Enter IP/Host: ")
        continuous_ping(host)
    elif choice == "2":
        clear_screen()
        console.print("[bold]Traceroute Tool[/bold]\n")
        host = input("Enter IP/Host: ")
        traceroute(host)
    elif choice == "3":
        clear_screen()
        console.print("[bold]DNS Lookup Tool[/bold]\n")
        host = input("Enter IP/Host: ")
        lookup_dns(host)
    elif choice == "4":
        clear_screen()
        console.print("[bold]WHOIS Lookup Tool[/bold]\n")
        host = input("Enter IP/Host: ")
        lookup_whois(host)
    elif choice == "5":
        clear_screen()
        console.print("[bold]Get IP Information Tool[/bold]\n")
        ip_address = input("Enter IP address: ")
        check_host_info(ip_address)
    else:
        clear_screen()
        console.print("[red]Invalid choice. Exiting.[/red]")
        exit()


if __name__ == "__main__":
    main()
