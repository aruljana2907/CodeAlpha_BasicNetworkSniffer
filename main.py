from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP
from datetime import datetime

# Open a file to save packet information
output_file = open("captured_packets.txt", "w")

# Counter for packets
packet_number = 0


# Function to print on screen and save to file
def write_line(text):
    print(text)
    output_file.write(text + "\n")


# Function to process each packet
def process_packet(packet):
    global packet_number
    packet_number += 1

    write_line("=" * 60)
    write_line(f"Packet #{packet_number}")
    write_line(f"Time             : {datetime.now().strftime('%H:%M:%S')}")

    if packet.haslayer(IP):
        write_line(f"Source IP        : {packet[IP].src}")
        write_line(f"Destination IP   : {packet[IP].dst}")

        if packet.haslayer(TCP):
            write_line("Protocol         : TCP")
            write_line(f"Source Port      : {packet[TCP].sport}")
            write_line(f"Destination Port : {packet[TCP].dport}")

        elif packet.haslayer(UDP):
            write_line("Protocol         : UDP")
            write_line(f"Source Port      : {packet[UDP].sport}")
            write_line(f"Destination Port : {packet[UDP].dport}")

        else:
            write_line("Protocol         : Other")

        write_line(f"Packet Length    : {len(packet)} bytes")

    else:
        write_line("Non-IP Packet")

    write_line("=" * 60)


# ===========================
# Main Program
# ===========================

write_line("=" * 50)
write_line("       BASIC NETWORK SNIFFER")
write_line("=" * 50)

write_line("\nChoose a filter:")
write_line("1. TCP Packets")
write_line("2. UDP Packets")
write_line("3. All Packets")

choice = input("\nEnter your choice (1/2/3): ")

try:
    packet_count = int(input("Enter number of packets to capture: "))

    write_line(f"\nCapturing {packet_count} packets...\n")

    if choice == "1":
        sniff(filter="tcp", prn=process_packet, count=packet_count)

    elif choice == "2":
        sniff(filter="udp", prn=process_packet, count=packet_count)

    elif choice == "3":
        sniff(prn=process_packet, count=packet_count)

    else:
        write_line("Invalid choice! Please run the program again.")

    write_line("\nCapture completed!")

except ValueError:
    write_line("Please enter a valid number.")

finally:
    output_file.close()