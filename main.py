import functions

u_ip = input("Input a valid IP: ")
u_bin_ip = functions.calculate_bin(u_ip.split("."))

u_mask_bits = int(input("Input mask bits (1-32): "))
u_subnet_mask_bin = []
u_subnet1 = []
u_subnet_mask_bin = functions.calculate_subnet_mask(u_mask_bits, u_subnet_mask_bin)
u_subnet_mask = functions.calculate_nonbin(u_subnet_mask_bin)
u_subnet = functions.calculate_subnet(u_bin_ip, u_subnet_mask_bin, u_subnet1)
u_bcast = functions.calculate_bcast(u_subnet, u_mask_bits)
u_bcast_nonbin = functions.calculate_nonbin(u_bcast)
u_subnet_nonbin = functions.calculate_nonbin(u_subnet)
u_range = functions.establish_range(u_subnet_nonbin, u_bcast_nonbin)


print(f"IP: {u_ip}\nIP binary: {u_bin_ip}\nMask Bits: {u_mask_bits}\nSubnet mask binary:\
{u_subnet_mask_bin}\nSubnet mask: {u_subnet_mask}\nSubnet: {u_subnet_nonbin}\nBcast: {u_bcast_nonbin}\nRange: {u_range}")
