import os
import subprocess
import psutil
import time
from scapy.all import ARP, Ether, srp
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QHBoxLayout, QLineEdit, QMessageBox, QGridLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont, QMovie, QPixmap
from PyQt5.QtCore import Qt, QSize

# User Credentials (Username: Password)
USER_CREDENTIALS = {"admin": "password123", "nitin": "securepass"}

# Ethical hacking tools and their commands
TOOLS = {
    "Metasploit": "curl https://raw.githubusercontent.com/rapid7/metasploit-framework/master/msfupdate | bash",
    "Nmap (Network Scanner)": "sudo apt install nmap -y",
    "Zphisher (Phishing Tool)": "git clone https://github.com/htr-tech/zphisher.git && cd zphisher && bash zphisher.sh",
    "SQLmap (SQL Injection)": "git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev",
    "Aircrack-ng (Wi-Fi Cracking)": "sudo apt install aircrack-ng -y",
    "Hydra (Brute-force Attacker)": "sudo apt install hydra -y",
    "DDoS Attack (hping3)": "sudo apt install hping3 -y",
    "MITM Attack (Ettercap)": "sudo apt install ettercap -y"
}

class HackerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DarkOps Toolkit by Nitin")
        self.setGeometry(200, 200, 900, 600)
        self.setStyleSheet("background-color: black; color: #00ff00;")

        layout = QVBoxLayout()

        title = QLabel("DarkOps Toolkit–Stealth. Precision. Control.")
        title.setFont(QFont("Courier", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.bg_label = QLabel(self)
        self.bg_movie = QMovie("matrix.gif")
        self.bg_movie.setScaledSize(QSize(700, 150))
        self.bg_label.setMovie(self.bg_movie)
        self.bg_movie.start()
        layout.addWidget(self.bg_label, alignment=Qt.AlignCenter)

        grid_layout = QGridLayout()
        row, col = 0, 0

        for tool in TOOLS.keys():
            tool_layout = QVBoxLayout()
            tool_label = QLabel(f"<b>{tool}</b>")
            tool_label.setFont(QFont("Courier", 14))
            tool_label.setStyleSheet("color: #00ff00;")
            tool_layout.addWidget(tool_label)
            
            install_button = QPushButton("Install")
            install_button.setStyleSheet("background-color: #008000; color: white; font-weight: bold; padding: 5px;")
            install_button.clicked.connect(lambda checked, t=tool: self.run_command(f"Installing {t}...", TOOLS[t]))
            tool_layout.addWidget(install_button)

            run_button = QPushButton("Run")
            run_button.setStyleSheet("background-color: cyan; color: black; font-weight: bold; padding: 5px;")
            run_button.clicked.connect(lambda checked, t=tool: self.run_command(f"Running {t}...", t.lower()))
            tool_layout.addWidget(run_button)

            update_button = QPushButton("Update")
            update_button.setStyleSheet("background-color: yellow; color: black; font-weight: bold; padding: 5px;")
            update_button.clicked.connect(lambda checked, t=tool: self.run_command(f"Updating {t}...", f"sudo apt update && sudo apt upgrade {t.lower()} -y"))
            tool_layout.addWidget(update_button)

            remove_button = QPushButton("Remove")
            remove_button.setStyleSheet("background-color: red; color: white; font-weight: bold; padding: 5px;")
            remove_button.clicked.connect(lambda checked, t=tool: self.run_command(f"Removing {t}...", f"sudo apt remove {t.lower()} -y"))
            tool_layout.addWidget(remove_button)

            grid_layout.addLayout(tool_layout, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1

        layout.addLayout(grid_layout)

        self.console = QTextEdit()
        self.console.setReadOnly(True)
        self.console.setStyleSheet("background-color: black; color: lime; font-family: Monospace; font-size: 16px; border: 2px solid #00ff00; padding: 10px;")
        self.console.setMinimumHeight(200)
        layout.addWidget(self.console)
        
        self.setLayout(layout)
    
    def run_command(self, action_message, command):
        self.console.append(f"[+] {action_message}\n")
        output = subprocess.getoutput(command)
        self.console.append(output + "\n")

# Run the application
if __name__ == "__main__":
    app = QApplication([])
    hacker_gui = HackerGUI()
    hacker_gui.show()
    app.exec_()
