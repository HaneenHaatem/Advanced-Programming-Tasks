import dis

def calculate_sum(a, b):
    return a + b

print("Disassemble calculate_sum function:")
dis.dis(calculate_sum)


# expected output :

#   3           RESUME                   0

#   4           LOAD_FAST_LOAD_FAST      1 (a, b)
#               BINARY_OP                0 (+)
#               RETURN_VALUE

