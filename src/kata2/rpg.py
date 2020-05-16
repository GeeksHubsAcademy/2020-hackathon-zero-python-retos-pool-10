#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    gen_password = ''
    for i in range(passLen):
        num_or_letter = random.randint(0, 1)
        if num_or_letter == 1:
            cap_or_low = random.randint(0, 1)
            if cap_or_low == 1:
                tmp_num = random.randint(65, 90)
                tmp_letter = chr(tmp_num)
                gen_password = gen_password + tmp_letter

            else:
                tmp_num = random.randint(97, 122)
                tmp_letter = chr(tmp_num)
                gen_password = gen_password + tmp_letter

        else:
            tmp_num = random.randint(33, 64)
            gen_password = gen_password + chr(tmp_num)

    return gen_password

# if __name__ == "__main__":
#     print(RandomPasswordGenerator(20))
    