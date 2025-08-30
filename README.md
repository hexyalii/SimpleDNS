# Custom DNS Resolver

A simple Python-based DNS server that resolves a specified domain to a custom IP address.  
This project uses the `dnslib` library to handle DNS queries and is perfect for testing or local development purposes.

## Features

- Resolve a specific domain to a custom IP address.
- Lightweight and easy to use.
- Supports IPv4 "A" records.
- Configurable port (default: 53).

## Requirements

- Python 3.7+
- `dnslib` library

Install dependencies via pip:

```bash
pip install dnslib
```

## Getting Started

Clone the repository:

```bash
git clone https://github.com/hexyalii/SimpleDNS.git
cd SimpleDNS
```

Run the DNS server:

```bash
python custom_dns_resolver.py
```

You will be prompted to enter:

1. **Domain**: The domain you want to resolve (e.g., `example.com`).  
2. **IP address**: The IP address you want the domain to resolve to (e.g., `127.0.0.1`).  
3. **Port**: Enter `1` for the default DNS port (53) or specify another port.

Example:

```text
Enter the domain: example.com
Enter the IP address: 127.0.0.1
Enter the port (1 for default 53): 1
DNS server is running on port 53... Press Ctrl+C to stop.
```

Press `Ctrl+C` to stop the server.

## Notes

- Make sure the chosen port is available and not blocked by your firewall.  
- Running on port 53 may require administrative privileges.  
- This server is intended for testing and development purposes only. **Not recommended for production use.**

## License

This project is licensed under the MIT License.
