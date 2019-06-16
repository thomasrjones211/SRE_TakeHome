from textwrap import wrap
from ipaddress import*


def read_input_pairs_check_output_to_file (filename):
    input_file = open(filename, "r")
    pairs = input_file.readlines()
    file = open("IP_output.txt", "w")
    for each_pair in pairs:
        pairs_array = each_pair.split(",")
        if len(pairs_array)==2:
            hexcode = pairs_array[0]
            subnet = pairs_array[1][:-1]
            result = (check_hex_subnet(hexcode, subnet))
            file.write("Is "+hexcode+" in "+subnet+"?   "+str(result)+"\n")
        else:
            continue
    file.close()


def check_hex_subnet (hexcode, subnet):
    return host_in_subnet(hex_to_ip(hexcode), subnet)


def hex_to_ip (hexcode):
    xhex = hexcode
    hex = xhex[2:]
    hexpairs = (wrap(hex, 2))
    octets = [int(i, 16) for i in hexpairs]
    IP = '.'.join(str(i) for i in octets)
    IP += "/32"
    return IP


def host_in_subnet (ipv4, subnet):
    a = ip_network(subnet)
    b = ip_network(ipv4)
    if b.subnet_of(a):
        return True
    else:
        return False


read_input_pairs_check_output_to_file("IP_input.txt")



