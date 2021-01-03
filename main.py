from socket import *
import time
import datetime

print("---------  Cyber Python  ---------")
print("")

host = input("Enter Your Host: ")
start_port = int(input("Enter The Start Port "))
end_port = int(input("Enter The End Port "))

active_ports = []

start_time = datetime.datetime.now()
print("Starting MahmoudScan 1.0 at", start_time)
print("MahmoudScan report for", host)
print("Ports range from", start_port, "to", end_port)
print("\n")

for port in range(start_port, end_port):
    s = socket(AF_INET, SOCK_STREAM)
    result = s.connect_ex((host, port))

    if result == 0:
        print("port", port, "is open")
        active_ports.append(port)
    else:

        print("port", port, "is close")
    time.sleep(2)

end_time = datetime.datetime.now()
print("\n")
print("The end time is", end_time, "- the open ports are", active_ports)
print("MahmoudScan completed successfully")
