"""
    This script is programmed by Mouhab-dev
    Follow me on Github: https://github.com/mouhab-dev
"""
# Function to convert Decimal to Binary
def dtb(n):  
    return bin(n).replace("0b", "")

print("Welcome to IP Calculator v1.0 by Mouhab-dev")
print("Find me on Github: https://github.com/mouhab-dev\n")

# Ask user for ip address and then split it based on the '.' and put it in a list
ip = list(map(int,input("Please, Enter an IP Address: ").split('.')))
# Ask user for subnet mask and then split it based on the '.' and put it in a list
subnet = list(map(int,input("Please, Enter Subnet Mask: ").split('.')))

full_bin_subnet=""

subnet_ones=0 # count no of ones in subnet mask
t_no_hosts=0 # calculate total number of hosts

network_id=[]
broadcast_address=[0,0,0,0]

for i in range(4):

    # count the number of ones in the subnet mask
    subnet_ones = subnet_ones + len(dtb(subnet[i]).strip('0'))
    
    # perform a logical and operation between ip and subnet mask to get the network id
    network_id.append(int(ip[i]) & int(subnet[i]))
    
    # Convert Subnet Mask to (32) binary digits
    '''
    if dtb(subnet[i]) == "0":
        full_bin_subnet = full_bin_subnet + dtb(subnet[i])*8
    else:
        full_bin_subnet = full_bin_subnet + dtb(subnet[i])
    '''

    # Calculate Broadcast Address
    if subnet[i] == 255 :
        broadcast_address[i] = network_id[i]
    else:
        broadcast_address[i] = 255 - subnet[i] + network_id[i]


# print(full_bin_subnet)

print("--------------------------------------------")

# Print the CIDR Notation for the given subnet mask
print("CIDR: /",subnet_ones)

# Print Network ID
print("Network ID:",'.'.join(map(str, network_id)))

# Calculate Total Number of Hosts in the subnet
t_no_hosts = pow(2,32-subnet_ones) - (2)

# Print First Host Address
first_id = network_id.copy()
first_id[3] += 1
print("First Host Address:",'.'.join(map(str, first_id)))

# Print Last Host Address
last_address = broadcast_address.copy()
last_address[3] -= 1
print("Last Host Address:",'.'.join(map(str, last_address)))

# Print Broadcast Address
print("Broadcast Address:",'.'.join(map(str, broadcast_address)))

# Print Total Number of Hosts
print("Total number of Hosts =",t_no_hosts)

# Exit successfully
exit(0)