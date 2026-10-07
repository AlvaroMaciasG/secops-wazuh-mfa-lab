import socket

target_ip = "192.168.50.5"
ports = [21, 22, 80, 443, 3306, 5432]

print(f"[*] Iniciando escaneo de puertos sobre {target_ip}")
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target_ip, port))
    if result == 0:
        print(f"[+] Puerto {port}: ABIERTO")
    s.close()
