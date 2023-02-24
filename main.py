

def calculate_nonbin(list_of_bin):
    list_of_nonbin = [0, 0, 0, 0]
    non_bin = []
    bits = 128
    current_oct = 0
    try:
        for x in list_of_bin:
            x = int(x)
            if x == 1:
                non_bin.append(bits)
            else:
                non_bin.append(0)
            if bits > 1:
                bits /= 2
            else:
                bits = 128
    except ValueError:
        print("Invalid IP")
    while current_oct <= 3:
        for y in non_bin[0:8]:
            list_of_nonbin[current_oct] += y
        del non_bin[0:8]
        current_oct += 1
    return list_of_nonbin


def calculate_bin(non_bin):
    bin1 = []
    for x in non_bin:
        try:
            x = int(x)
            bits = 128
            while bits >= 1:
                if x >= bits:
                    bin1.append(1)
                    x -= bits
                    bits /= 2
                else:
                    bin1.append(0)
                    bits /= 2
        except ValueError:
            print("invalid input")
    return bin1


def calculate_subnet_mask(sub, binary):
    try:
        sub = int(sub)
        for x in range(sub):
            binary.append(1)
        for y in range(32 - sub):
            binary.append(0)
        calculate_nonbin(binary)
        return binary
    except ValueError:
        print("Invalid Subnet")


def convert(var, v_type):
    current_step = 0
    if v_type == "int":
        while current_step < len(var):
            var[current_step] = int(var[current_step])
            current_step += 1
    elif v_type == "str":
        while current_step < len(var):
            var[current_step] = str(var[current_step])
            current_step += 1
    else:
        print("spelt it wrong dumbass")


def calculate_subnet(ip, subnet_mask):
    current_step = 0
    while current_step < len(ip):
        subnet.append(ip[current_step] * subnet_mask[current_step])
        current_step += 1
    return subnet


u_ip = input("Input a valid IP: ")
u_bin_ip = calculate_bin(u_ip.split("."))

u_mask_bits = input("Input mask bits (1-32): ")
u_subnet_mask_bin = []
u_subnet_mask_bin = calculate_subnet_mask(u_mask_bits, u_subnet_mask_bin)
u_subnet_mask = calculate_nonbin(u_subnet_mask_bin)
u_subnet = calculate_subnet(u_bin_ip, u_subnet_mask_bin)

print(f"IP: {u_ip}\nIP binary: {u_bin_ip}\nMask Bits: {u_mask_bits}\nSubnet mask binary: {u_subnet_mask_bin}\nSubnet mask: {u_subnet_mask}\nSubnet: {u_subnet}")