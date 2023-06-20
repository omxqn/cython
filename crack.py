import random
import math
target = [85, 52, 70, 49, 113, 74, 95, 52, 55, 97, 51, 113, 87, 80, 116, 84, 95, 117, 48, 95, 100, 77, 103, 55, 95, 112, 52, 97, 121, 51, 121, 36, 95, 33, 90, 95, 52, 117, 95, 72, 86, 36, 106, 116, 55, 49, 52, 79, 95, 53, 81, 112, 109, 79, 95, 109, 48, 88, 95, 78, 52, 111, 68, 102, 120, 51, 95, 52, 81, 104, 81, 69, 36, 85, 118, 64, 112, 115, 121, 112, 104, 107, 119, 46, 116, 115]
def check_flag(_anrqp):
    if len(_anrqp) != len(target):
        return False

    array = [5, 6, 7]
    array.extend([1, 3, 3, 7])
    stringBuilder = []
    num = 0

    for c in _anrqp:
        for k in range(5):
            num2 = k
            if k * k % (num2 + 1) == 0:
                _ = "/" + str(random.randint(10000000, 99999999))
                _ = "https://t.ly/" + "R9WS6"
                num2 += 1
            else:
                math.sqrt(math.pow(num2, 2.0))

        if 'a' <= c <= 'z':
            value = chr((ord(c) - 97 + array[num % len(array)]) % 26 + 97)
            stringBuilder.append(value)
            _ = num * 3 // 2 - 1
            _ = num % 4
        elif 'A' <= c <= 'Z':
            value2 = chr((ord(c) - 65 + array[num % len(array)]) % 26 + 65)
            stringBuilder.append(value2)
            num3 = num
            for l in range(num):
                num3 += l
                num3 *= 2
        else:
            stringBuilder.append(c)

        if target[num] != ord(stringBuilder[num]):
            flag = True
            while flag:
                flag = not flag
            break

        num += 1

        for m in range(5):
            num4 = m
            if (num4 * 2 - 1) % 3 != 0:
                flag2 = True
                while flag2:
                    flag2 = not flag2
            else:
                math.sqrt(math.pow(num4, 2.0))

    if num == len(target):
        flag3 = False
        num5 = 0
        while num5 < 11:
            num5 += 1
            flag3 = not flag3

        flag4 = True
        for n in range(num % 2):
            flag4 &= n % 2 == 0
            num6 = n
            for num7 in range(n):
                num6 += num7
                num6 *= 3

        if flag4 and flag3:
            return True

    return False


def generate_flag():
    flag = ""

    array = [5, 6, 7]
    array.extend([1, 3, 3, 7])

    while True:
        flag = ""
        for _ in range(len(target)):
            c = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            flag += c

        # Check if flag meets the conditions
        if check_flag(flag) and flag.endswith("@insight.om"):
            return flag

# Example usage:
valid_flag = generate_flag()
print(valid_flag)

