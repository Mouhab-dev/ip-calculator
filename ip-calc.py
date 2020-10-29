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

# Function to convert from CIDR Notation to Subnet mask
def cidr_to_subnet(CIDR):
    counter = 0
    subnet=[]
    while (CIDR>8):
        CIDR = CIDR-8
        counter +=1
    for i in range(4):
        if i < counter:
            subnet.append(255)
        elif i == counter:
            subnet.append(256-pow(2,(8-CIDR)))
        else:
            subnet.append(0)
    return subnet

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
        # Ask user for subnet mask with CIDR or full subnet mask
        CIDR=input("Please, Enter Subnet Mask: ")
        # CIDR Notation code
        if CIDR[0] == '/':
            CIDR=int(CIDR[1:])
            # if CIDR not in range (8-30) raise an error invalid subnet mask
            if not CIDR in range(8,31):
                print(CRED + "Invalid shorthand notation. Must be in the range of 8-30." + CEND)
                check_subnet=True
                continue
            else:
                # else send cidr to the conversion fn to obtain full subnet mask
                subnet=cidr_to_subnet(CIDR)
                # set check_subnet to false to exit while loop
                check_subnet=False
        else:
            # Ask user for subnet mask and then split it based on the '.' and put it in a list
            subnet = list(map(int,CIDR.split('.')))
            # check if the first value not equal 255
            if subnet[0] != 255:
                print(CRED + "Invalid subnet mask. The lowest allowed mask must be 255.0.0.0" + CEND)
                check_subnet=True
                continue
            # set check_subnet to false to exit while loop
            check_subnet=False
        # Check if user has inputted the full length of the subnet mask
        if len(subnet) != 4:
            print(CRED + "Error: Subnet Mask supported format X.X.X.X" + CEND)
            check_subnet=True
            continue
        # check if the rest of the digits excceds 255 skip the first digit we have already checked above
        for j in subnet[1:] :
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

subnet_ones=0 # count no of ones in subnet mask
t_no_hosts=0 # calculate total number of hosts
network_id=[] # list to store network id
broadcast_address=[0,0,0,0] # list to store broadcast address

for i in range(4):

    # count the number of ones in the subnet mask
    subnet_ones = subnet_ones + len(dtb(subnet[i]).strip('0'))
    
    # perform a logical and operation between ip and subnet mask to get the network id
    network_id.append(int(ip[i]) & int(subnet[i]))

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