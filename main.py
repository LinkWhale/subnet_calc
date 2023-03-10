import functions

u_ip = input("Input a valid IP: ")
u_bin_ip = functions.calculate_bin(u_ip.split("."))

u_mask_bits = input("Input mask bits (1-32): ")
u_subnet_mask_bin = []
u_subnet1 = []
u_subnet_mask_bin = functions.calculate_subnet_mask(u_mask_bits, u_subnet_mask_bin)
u_subnet_mask = functions.calculate_nonbin(u_subnet_mask_bin)
u_subnet = functions.calculate_subnet(u_bin_ip, u_subnet_mask_bin, u_subnet1)
u_bcast =

print(f"IP: {u_ip}\nIP binary: {u_bin_ip}\nMask Bits: {u_mask_bits}\nSubnet mask binary:\
{u_subnet_mask_bin}\nSubnet mask: {u_subnet_mask}\nSubnet: {u_subnet}")