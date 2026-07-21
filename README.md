# CodeAlpha Basic Network Sniffer

My first cybersecurity internship project.

# 🛡️ Basic Network Sniffer

## 📌 Project Overview

The **Basic Network Sniffer** is a Python-based cybersecurity tool developed as part of the **CodeAlpha Cyber Security Internship**.

It captures live network packets from the local network and displays important information such as source and destination IP addresses, protocol type, port numbers, packet length, and timestamp. The application also allows users to filter packets by TCP, UDP, or capture all packets. Captured packet details are automatically saved to a text file for future analysis.

---

## ✨ Features

- 📡 Capture live network packets
- 🌐 Display Source IP Address
- 🌐 Display Destination IP Address
- 🔍 Identify TCP and UDP protocols
- 🔢 Display Source and Destination Port Numbers
- 📏 Show Packet Length
- ⏰ Display Capture Time
- 🎯 Filter packets (TCP / UDP / All)
- 💾 Save captured packets to `captured_packets.txt`
- 🖥️ User-friendly console interface

---

## 🛠️ Technologies Used

- Python 3.x
- Scapy
- Npcap (Windows)

---

## 📂 Project Structure

```
CodeAlpha_BasicNetworkSniffer
│
├── main.py
├── README.md
├── requirements.txt
├── captured_packets.txt
└── screenshots
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_BasicNetworkSniffer.git
```

### 2. Move into the project folder

```bash
cd CodeAlpha_BasicNetworkSniffer
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Npcap

Download and install **Npcap** from:

https://npcap.com/

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📷 Sample Output

```
============================================================
Packet #1
Time             : 18:06:41
Source IP        : 10.243.29.72
Destination IP   : 224.0.0.251
Protocol         : UDP
Source Port      : 5353
Destination Port : 5353
Packet Length    : 119 bytes
============================================================
```

---

## 📁 Output File

All captured packets are automatically saved in:

```
captured_packets.txt
```

---

## 📸 Screenshots

Add screenshots of:

- Program Menu
- TCP Packet Capture
- UDP Packet Capture
- captured_packets.txt

---

## 🚀 Future Improvements

- Support IPv6 packet details
- Export captured packets to CSV
- Display TCP Flags
- Graphical User Interface (GUI)
- Advanced packet filtering
- Packet statistics dashboard

---

## 👩‍💻 Author

**Janani A**

Cyber Security Student

CodeAlpha Cyber Security Intern

---

## 📜 License

This project was developed for educational purposes as part of the CodeAlpha Cyber Security Internship.