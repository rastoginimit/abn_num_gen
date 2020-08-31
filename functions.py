def get_abn_checksum(digits9):
    # wights for last 9 digits in an ABN
    weights      = (3, 5, 7, 9, 11, 13, 15, 17, 19)
    
    #prefix with zero, if needed
    digits9      = str(digits9).zfill(9)
    
    #calculte the weighted sum
    weighted_sum = 0    
    for i in range(9):
        weighted_sum += weights[i] * int(digits9[i])
    
    #first 2 digits (checksum) to be prefixed with the 9 digitst to make it a valid ABN
    checksum     = 89 - (weighted_sum%89) + 10
    return str(checksum)

def is_valid_abn(abn):
    # wights forall 11 digits in an ABN
    weights        = (10, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19)
    abn_digits     = str(abn)
    
    #subtract 1 from the first digit
    abn_digit1     = abn_digits[:1]
    abn_digit1     = str(int(abn_digit1) - 1)
    abn_new_digits = abn_digit1 + abn_digits[1:]
    
    #calculte the weighted sum
    weighted_sum   = 0
    for i in range(11):
        weighted_sum += weights[i] * int(abn_new_digits[i])
    
    #validate via modulo 89
    if (weighted_sum%89 == 0):
        return True 
    return False
