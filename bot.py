import socket
from dnslib import DNSRecord, RR, QTYPE, A
from dnslib.server import DNSServer, BaseResolver

class MyResolver(BaseResolver):
    def __init__(self, domain, ip_address):
        self.domain = domain
        self.ip_address = ip_address
    
    def resolve(self, request, handler):
        reply = request.reply()
        qname = request.q.qname
        qtype = QTYPE[request.q.qtype]

        if str(qname) == self.domain + '.' and qtype == "A":
            reply.add_answer(RR(rname=qname, rtype=QTYPE.A, rclass=1, ttl=300, rdata=A(self.ip_address)))
        
        return reply

def main():
    domain = input("Enter the domain: ")
    ip_address = input("Enter the IP address: ")
    port = input("Enter the port (1 for default 53): ")

    if port == "1":
        port = 53
    else:
        port = int(port)
    
    resolver = MyResolver(domain, ip_address)
    server = DNSServer(resolver, port=port, address="0.0.0.0", tcp=False)
    server.start_thread()

    print(f"DNS server is running on port {port}... Press Ctrl+C to stop.")
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        server.stop()
        print("DNS server stopped.")

if __name__ == "__main__":
    main()
