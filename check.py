############------------ IMPORTS ------------############
import scapy.all as scapy


############------------ FUNCTION(S) ------------############
def sniff(what_to_sniff):
    scapy.sniff(iface=what_to_sniff, store=False, prn=process_sniffed_packet)


def process_sniffed_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
        print(packet.show())

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    sniff("eth0")