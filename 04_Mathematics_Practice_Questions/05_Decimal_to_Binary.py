def int_to_binary(n):
    if decimal_num == 0:
    return "0"

    is_negative = decimal_num < 0
    if is_negative:
        decimal_num = abs(decimal_num)

    binary_str = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_str = str(remainder) + binary_str
        decimal_num //= 2

    if is_negative:
    # Two's complement for negative numbers
    # 1. Invert all bits
    inverted_binary = ''.join('1' if bit == '0' else '0' for bit in binary_str)
    # 2. Add 1
    carry = 1
    result = ""
    for bit in reversed(inverted_binary):
      if bit == '1' and carry == 1:
        result = '0' + result
        carry = 1
      elif bit == '0' and carry == 1:
        result = '1' + result
        carry = 0
      else:
        result = bit + result
    binary_str = result

  return binary_str
    
result = int_to_binary(10)
print(result)