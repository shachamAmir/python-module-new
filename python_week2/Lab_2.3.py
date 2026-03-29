from http import server


port_list = [8080, 8443, 22, 8080, 443, 3000]
unique_ports = set(port_list)
unique_ports.discard(22)

print(unique_ports)

server_names = ["web01", "web02", "web03"]

print(22 in unique_ports)
print(22 in server_names)

valid_set = [ (1,2), (3,4) ]

invalid_set = {[1,2], [3,4]} #! This will raise an error because lists are mutable and cannot be added to a set

