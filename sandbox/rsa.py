# RSA algorithm is a public key encryption technique and is considered as the most secure way of encryption.
# Resource: https://www.di-mgt.com.au/rsa_alg.html#note5


from numpy import mod
import sympy
import time
import matplotlib.pyplot as plt


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def convert_to_int(text):
    converted = []
    for letter in text:
        converted.append(ord(letter) - 96)
    return converted


def convert_to_ascii(text):
    converted = ''
    for number in text:
        converted = converted + chr(number + 96)
    return converted


def choose_e(phi, n):
    print('Choosing e...')
    for e in range(2 ** 31, 2, -1):
        if gcd(e, phi) == 1 and gcd(e, n) == 1:
            return e


def modular_inverse(a, m):  # modular inverse of e modulo phi
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x = x + m0

    return x


def encrypt(text, public_key):
    key, n = public_key
    ctext = [pow(ord(char), key, n) for char in text]
    return ctext


def decrypt(ctext, private_key, d, n):
    m = []
    for x in ctext:
        c = pow(x,  d) % n
        m.append(c)
    return m


def RSA():
    enc = []
    dec = []
    p = 43
    q = 23
    print('p = ', p, ' q = ', q)
    n = p * q
    print('n = ', n)
    phi = (p - 1) * (q - 1)
    time_start1 = time.time()
    print('phi = ', phi)
    e = 529
    print('e = ', e)
    d = modular_inverse(e, phi)
    print('d = ', d)
    coba = encrypt("GIH", [e, n])
    print(coba)
    text = 'GIH'
    print("---------------------")
    dp = d % (p - 1)
    dq = d % (q - 1)
    qInv = modular_inverse(q, p)
    privat_key = [dp, dq, qInv, p, q]
    print(privat_key)
    decc = decrypt(coba, privat_key, d, n)
    print(decc)
    print('Plaintext: ', text)
    converted = convert_to_int(text)
    for number in converted:
        enc.append(pow(number, e, n))
    print('Encrypted text: ', enc)
    for number in enc:
        dec.append(pow(number, d, n))
    decrypted = convert_to_ascii(dec)
    print('Decrypted text: ', decrypted)
    time_finish1 = time.time()
    print('Time for classic decryption: ', time_finish1 - time_start1)
    rsa_time=time_finish1 - time_start1
    return p, q, e, d, enc, rsa_time


# The CRT method of decryption is about four times faster overall
# Even though there are more steps in this procedure,
# the modular exponentiation to be carried out uses much shorter exponents and so it is less expensive in the end
def CRT(p, q, dP, dQ, c):
    qInv = modular_inverse(q, p)
    m1 = pow(c, dP, p)
    m2 = pow(c, dQ, q)
    h = (qInv * (m1 - m2)) % p
    m = m2 + h * q
    return m


def main():
    print('------ RSA ------')
    p, q, _, d, enc, rsa_time = RSA()
    time_start2 = time.time()
    dp = d % (p - 1)
    dq = d % (q - 1)
    text = 'GIH'
    
    for number in enc:
        text = text + chr(CRT(p, q, dp, dq, number) + 96)
        print(text)
    print('Decrypted using CRT: ', text)
    time_finish2 = time.time()

    print('Time for CRT decryption: ', time_finish2 - time_start2)
    # x-coordinates of left sides of bars
    # left = [1, 1.5]
    # heights of bars
    # height = [rsa_time, time_finish2 - time_start2]
    # labels for bars
    # tick_label = ['RSA Ecryption', 'CRT Decryption']
    # plotting a bar chart
    # plt.bar(left, height, tick_label = tick_label,
		# width = 0.5, color = ['blue', 'black'])
    # naming the x-axis
    # plt.xlabel('Algorithm')
    # naming the y-axis
    # plt.ylabel('Time Taken')
    # plot title
    # plt.title('Decryption Time')
    # function to show the plot
    #plt.show()
    
main()