from dnslib import DNSRecord, DNSHeader, RR, A
from dnslib.server import DNSServer, BaseResolver
import logging

class RedirectResolver(BaseResolver):
    def __init__(self, ip):
        self.ip = ip

    def resolve(self, request, handler):
        reply = request.reply()
        qname = request.q.qname
        reply.add_answer(RR(qname, rdata=A(self.ip), ttl=60))
        return reply

def main():
    logging.basicConfig(level=logging.INFO)

    # گرفتن آدرس IP از کاربر
    ip_to_redirect = input("لطفاً آدرس IP سرور را وارد کنید: ")

    # ایجاد resolver سفارشی
    resolver = RedirectResolver(ip_to_redirect)

    # پیکربندی و شروع سرور DNS
    server = DNSServer(resolver, port=53, address="0.0.0.0")
    server.start_thread()

    print(f"سرور DNS شروع به کار کرد و تمام درخواست‌ها را به {ip_to_redirect} هدایت می‌کند.")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("سرور DNS متوقف شد.")
        pass

if __name__ == "__main__":
    main()
