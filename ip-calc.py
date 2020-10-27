"""
    This script is programmed by Mouhab-dev
    Follow me on Github: https://github.com/mouhab-dev
"""
# For colored output
CRED = '\033[91m'
CEND = '\033[0m'

# Function to convert Decimal to Binary
def dtb(n):
    return format(n,'08b')

print("Welcome to IP Calculator v1.0 by Mouhab-dev")
print("Project Repo on Github: https://github.com/mouhab-dev/ip-calculator")
print("Find me on Github: https://github.com/mouhab-dev\n")

ip=[] # List to store ip address
check_ip=True # Variabke to manage loop over ip address
while check_ip:
    try:
        # Ask user for ip address and then split it based on the '.' and put it in a list
        ip = list(map(int,input("Please, Enter an IP Address: ").split('.')))
        check_ip=False
        # error handling for ip address
        if len(ip) != 4 :
            # Check for X.X.X.X Format
            print(CRED + "Error: IP Address supported format X.X.X.X" + CEND)
            check_ip=True
            continue
        for i in ip:
            # Check if the any digit exceeds 255
            if i > 255:
                print(CRED + "Error: IP Address Range: (0-255)" + CEND)
                check_ip=True
                break
        continue
    except ValueError:
        print(CRED + "Error: Only integers are allowed" + CEND)
        check_ip=True
        continue
    except KeyboardInterrupt:
        print()
        print(CRED + "IP Calculator has been terminated." + CEND)
        exit(0)
    except:
        print(CRED + "An error has occurred." + CEND)
        check_ip=True
        continue

subnet=[] # List to store subnet mask
check_subnet=True # Variable to manage loop over subnet mask
while(check_subnet):
    try:
        # Ask user for subnet mask and then split it based on the '.' and put it in a list
        subnet = list(map(int,input("Please, Enter Subnet Mask: ").split('.')))
        check_subnet=False
        # error handling for subnet
        if len(subnet) != 4:
            print(CRED + "Error: Subnet Mask supported format X.X.X.X" + CEND)
            check_subnet=True
            continue
        for j in subnet:
            # Check if the digits exceeds 255
            if j > 255:
                print(CRED + "Error: Subnet Mask Range: (0-255)" + CEND)
                check_subnet=True
                break
            # Check for invalid subnetmask (continous binary ones)
            if '01' in dtb(j):
                print(CRED + "Error: Invalid subnet mask, it must contain continous ones." + CEND)
                check_subnet=True
                break
        continue
    except ValueError:
        print(CRED + "Error: Only integers are allowed." + CEND)
        check_subnet=True
        continue
    except KeyboardInterrupt:
        print()
        print(CRED + "IP Calculator has been terminated." + CEND)
        exit(0)
    except:
        print(CRED + "An error has occurred." + CEND)
        check_subnet=True
        continue

# full_bin_subnet=""

subnet_ones=0 # count no of ones in subnet mask
t_no_hosts=0 # calculate total number of hosts
network_id=[] # list to store network id
broadcast_address=[0,0,0,0] # list to store broadcast address

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