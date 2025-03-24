from dnslib import *
import socketserver

FAKE_IP = "1.2.3.4"

class DNSHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        dns_request = DNSRecord.parse(data)
        qname = str(dns_request.q.qname)

        print(f"[+] DNS Request for: {qname}")

        reply = dns_request.reply()
        reply.add_answer(RR(qname, QTYPE.A, rdata=A(FAKE_IP), ttl=60))

        self.request[1].sendto(reply.pack(), self.client_address)

if __name__ == "__main__":
    print("[+] DNS Server Running on Port 53...")
    server = socketserver.UDPServer(("0.0.0.0", 53), DNSHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Server stopped.")