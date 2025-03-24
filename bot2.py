from dnslib import *
import socketserver

FAKE_IP = "1.2.3.4"  # آی‌پی فیک برای پاسخ دادن

class DNSHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()  # دریافت درخواست DNS
        dns_request = DNSRecord.parse(data)  # پردازش درخواست
        qname = str(dns_request.q.qname)  # نام دامنه درخواست شده

        print(f"[+] DNS Request for: {qname}")  # چاپ درخواست

        reply = dns_request.reply()  # ایجاد پاسخ به درخواست
        # اضافه کردن پاسخ به نوع A (آی‌پی) برای دامنه
        reply.add_answer(RR(qname, QTYPE.A, rdata=A(FAKE_IP), ttl=60))

        # ارسال پاسخ به درخواست‌کننده
        self.request[1].sendto(reply.pack(), self.client_address)

if __name__ == "__main__":
    print("[+] DNS Server Running on Port 53...")
    server = socketserver.UDPServer(("0.0.0.0", 53), DNSHandler)
    try:
        server.serve_forever()  # شروع به کار سرور
    except KeyboardInterrupt:
        print("\n[!] Server stopped.")  # قطع سرور در صورت فشردن Ctrl+C