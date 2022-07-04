import base64
import hashlib
import hmac
import binascii
import urllib.parse
import string
import numpy as np
from math import *
from egcd import egcd
from pyodide import create_proxy
from js import console

alphabet = string.ascii_lowercase
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

page_loading = Element("page_loading").element

x_replace = Element("x_replace").element
x_reverse = Element("x_reverse").element
x_case = Element("x_case_transform").element
x_numeral = Element("x_numeral_system").element
x_caesar = Element("x_caesar").element
x_vigenere = Element("x_vigenere").element
x_alphabetical = Element("x_alphabetical").element
x_rail_fence = Element("x_rail_fence").element
x_hill = Element("x_hill").element
x_base32 = Element("x_base32").element
x_base64 = Element("x_base64").element
x_ascii85 = Element("x_ascii85").element
x_unicode = Element("x_unicode").element
x_url_encode = Element("x_url_encode").element
x_hash_func = Element("x_hash_func").element
x_hmac = Element("x_hmac").element

goto_feature = Element("goto_feature").element

breadcrumb1 = Element("breadcrumb1").element
breadcrumb2 = Element("breadcrumb2").element

view_feature = Element("view_feature").element
view_main = Element("view_main").element

view_x_replace = Element("view_x_replace").element
view_x_reverse = Element("view_x_reverse").element
view_x_case = Element("view_x_case").element
view_x_numeral = Element("view_x_numeral").element
view_x_caesar = Element("view_x_caesar").element
view_x_vigenere = Element("view_x_vigenere").element
view_x_hill = Element("view_x_hill").element
view_x_base32 = Element("view_x_base32").element
view_x_base64 = Element("view_x_base64").element
view_x_ascii85 = Element("view_x_ascii85").element
view_x_unicode = Element("view_x_unicode").element
view_x_url_encode = Element("view_x_url_encode").element
view_x_hash = Element("view_x_hash").element
view_x_hmac = Element("view_x_hmac").element

is_encode = Element("is_encode").element
tab_encode = Element("tab_encode").element
tab_decode = Element("tab_decode").element

input = Element("input").element
output = Element("output").element

x_replace_find = Element("x_replace_find").element
x_replace_replace = Element("x_replace_replace").element
x_replace_case_n = Element("x_replace_case_n").element
x_replace_process = Element("x_replace_process").element

x_reverse_char = Element("x_reverse_char").element
x_reverse_line = Element("x_reverse_line").element
x_reverse_process = Element("x_reverse_process").element

x_case_lower = Element("x_case_lower").element
x_case_upper = Element("x_case_upper").element
x_case_cap = Element("x_case_cap").element
x_case_alt = Element("x_case_alt").element
x_case_inv = Element("x_case_inv").element
x_case_process = Element("x_case_process").element

x_numeral_r2 = Element("x_numeral_r2").element
x_numeral_r8 = Element("x_numeral_r8").element
x_numeral_r10 = Element("x_numeral_r10").element
x_numeral_r16 = Element("x_numeral_r16").element
x_numeral_t2 = Element("x_numeral_t2").element
x_numeral_t8 = Element("x_numeral_t8").element
x_numeral_t10 = Element("x_numeral_t10").element
x_numeral_t16 = Element("x_numeral_t16").element
x_numeral_process = Element("x_numeral_process").element

x_caesar_shift = Element("x_caesar_shift").element
x_caesar_shift_p = Element("x_caesar_shift_plus").element
x_caesar_shift_m = Element("x_caesar_shift_minus").element
# x_caesar_case = Element("x_caesar_case").element
x_caesar_process = Element("x_caesar_process").element

x_vigenere_variant = Element("x_vigenere_variant").element
x_vigenere_key = Element("x_vigenere_key").element
x_vigenere_mode = Element("x_vigenere_mode").element
x_vigenere_process = Element("x_vigenere_process").element

x_base32_std = Element("x_base32_std").element
x_base32_hex = Element("x_base32_hex").element
x_base32_process = Element("x_base32_process").element

x_base64_std = Element("x_base64_std").element
x_base64_url = Element("x_base64_url").element
x_base64_process = Element("x_base64_process").element

x_ascii85_std = Element("x_ascii85_std").element
# x_ascii85_z85 = Element("x_ascii85_z85").element
x_ascii85_process = Element("x_ascii85_process").element

x_unicode_sep = Element("x_unicode_sep").element
x_unicode_unc = Element("x_unicode_unc").element
x_unicode_dec = Element("x_unicode_dec").element
x_unicode_hex = Element("x_unicode_hex").element
x_unicode_bin = Element("x_unicode_bin").element
x_unicode_oct = Element("x_unicode_oct").element
x_unicode_ndec = Element("x_unicode_ndec").element
x_unicode_nhex = Element("x_unicode_nhex").element
x_unicode_process = Element("x_unicode_process").element

x_url_enc_process = Element("x_url_encode_process").element

x_hash_md5 = Element("x_hash_md5").element
x_hash_sha1 = Element("x_hash_sha1").element
x_hash_sha256 = Element("x_hash_sha256").element
x_hash_sha384 = Element("x_hash_sha384").element
x_hash_sha512 = Element("x_hash_sha512").element
x_hash_process = Element("x_hash_process").element

x_hmac_key = Element("x_hmac_key").element
x_hmac_md5 = Element("x_hmac_md5").element
x_hmac_sha1 = Element("x_hmac_sha1").element
x_hmac_sha256 = Element("x_hmac_sha256").element
x_hmac_sha384 = Element("x_hmac_sha384").element
x_hmac_sha512 = Element("x_hmac_sha512").element
x_hmac_process = Element("x_hmac_process").element

x_hill_key = Element("x_hill_key").element
x_hill_process = Element("x_hill_process").element


def loading_done():
    page_loading.classList.add("is-hidden")
    show_feature()


def show_feature():
    view_main.classList.add("is-hidden")
    view_feature.classList.remove("is-hidden")
    tab_decode.classList.remove("is-hidden")
    input.value = ""
    output.value = ""
    view_x_replace.classList.add("is-hidden")
    view_x_reverse.classList.add("is-hidden")
    view_x_case.classList.add("is-hidden")
    view_x_numeral.classList.add("is-hidden")
    view_x_caesar.classList.add("is-hidden")
    view_x_vigenere.classList.add("is-hidden")
    view_x_hill.classList.add("is-hidden")
    view_x_base32.classList.add("is-hidden")
    view_x_base64.classList.add("is-hidden")
    view_x_ascii85.classList.add("is-hidden")
    view_x_unicode.classList.add("is-hidden")
    view_x_url_encode.classList.add("is-hidden")
    view_x_hash.classList.add("is-hidden")
    view_x_hmac.classList.add("is-hidden")


def show_main(id):
    view_main.classList.remove("is-hidden")
    view_feature.classList.add("is-hidden")
    breadcrumb1.innerHTML = id.closest(":not(button)").previousElementSibling.innerHTML
    breadcrumb2.innerHTML = id.innerHTML


def switch_input():
    temp = input.value
    input.value = output.value
    output.value = temp


def encode_view():
    tab_encode.classList.add("is-active")
    tab_decode.classList.remove("is-active")
    is_encode.value = 1


def decode_view():
    tab_encode.classList.remove("is-active")
    tab_decode.classList.add("is-active")
    is_encode.value = 0


def tab_encode_click(event):
    if not tab_encode.classList.contains("is-active"):
        encode_view()
        switch_input()


def tab_decode_click(event):
    if not tab_decode.classList.contains("is-active"):
        decode_view()
        switch_input()


def goto_feature_click(event):
    show_feature()


def x_replace_click(event):
    show_main(x_replace)
    view_x_replace.classList.remove("is-hidden")


def x_reverse_click(event):
    show_main(x_reverse)
    view_x_reverse.classList.remove("is-hidden")


def x_case_click(event):
    show_main(x_case)
    view_x_case.classList.remove("is-hidden")


def x_numeral_click(event):
    show_main(x_numeral)
    view_x_numeral.classList.remove("is-hidden")


def x_caesar_click(event):
    show_main(x_caesar)
    view_x_caesar.classList.remove("is-hidden")


def x_vigenere_click(event):
    show_main(x_vigenere)
    view_x_vigenere.classList.remove("is-hidden")


def x_alphabetical_click(event):
    show_main(x_alphabetical)


def x_rail_fence_click(event):
    show_main(x_rail_fence)


def x_hill_click(event):
    show_main(x_hill)
    view_x_hill.classList.remove("is-hidden")


def x_base32_click(event):
    show_main(x_base32)
    view_x_base32.classList.remove("is-hidden")


def x_base64_click(event):
    show_main(x_base64)
    view_x_base64.classList.remove("is-hidden")


def x_ascii85_click(event):
    show_main(x_ascii85)
    view_x_ascii85.classList.remove("is-hidden")


def x_unicode_click(event):
    show_main(x_unicode)
    view_x_unicode.classList.remove("is-hidden")


def x_url_encode_click(event):
    show_main(x_url_encode)
    view_x_url_encode.classList.remove("is-hidden")


def x_hash_func_click(event):
    show_main(x_hash_func)
    view_x_hash.classList.remove("is-hidden")
    tab_decode.classList.add("is-hidden")
    encode_view()


def x_hmac_click(event):
    show_main(x_hmac)
    view_x_hmac.classList.remove("is-hidden")
    tab_decode.classList.add("is-hidden")
    encode_view()


################################################################################


def x_replace_process_click(event):
    x = input.value
    find = x_replace_find.value
    replace = x_replace_replace.value

    if x_replace_case_n.checked:
        x = x.lower()
        find = find.lower()
        replace = replace.lower()

    if int(is_encode.value) == 1:
        output.value = x.replace(find, replace)
    else:
        output.value = x.replace(replace, find)


def x_reverse_process_click(event):
    x = input.value
    if x_reverse_char.checked:
        output.value = x[::-1]
    else:
        temp = []
        for line in x.split("\n"):
            temp.append(line)
        temp.reverse()
        output.value = "\n".join(temp)


def x_case_process_click(event):
    x = input.value
    if x_case_lower.checked:
        output.value = x.lower()
    elif x_case_upper.checked:
        output.value = x.upper()
    elif x_case_cap.checked:
        temp = []
        for word in x.split(" "):
            temp.append(word.capitalize())
        output.value = " ".join(temp)
    elif x_case_alt.checked:
        temp = []
        for i, c in enumerate(x):
            if i % 2 == 0:
                temp.append(c.lower())
            else:
                temp.append(c.upper())
        output.value = "".join(temp)
    elif x_case_inv.checked:
        output.value = x.swapcase()


def x_numeral_process_click(event):
    x = input.value

    if x_numeral_r2.checked:
        x = int(x, 2)
    elif x_numeral_r8.checked:
        x = int(x, 8)
    elif x_numeral_r10.checked:
        x = int(x)
    elif x_numeral_r16.checked:
        x = int(x, 16)

    if x_numeral_t2.checked:
        x = bin(int(x))[2:]
    elif x_numeral_t8.checked:
        x = oct(int(x))[2:]
    elif x_numeral_t10.checked:
        x = str(int(x))
    elif x_numeral_t16.checked:
        x = hex(int(x))[2:]

    output.value = x


def x_caesar_shift_p_click(event):
    x_caesar_shift.value = int(x_caesar_shift.value) + 1


def x_caesar_shift_m_click(event):
    x_caesar_shift.value = int(x_caesar_shift.value) - 1


def x_caesar_encode_decode(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += char

    return result


def x_caesar_process_click(event):
    if int(is_encode.value) == 1:
        output.value = x_caesar_encode_decode(input.value, int(x_caesar_shift.value))
    else:
        output.value = x_caesar_encode_decode(input.value, -int(x_caesar_shift.value))


def x_vigenere_encode(plaintext, num_key):
    count = 0
    ciphertext = ""

    for i in range(len(plaintext)):
        char0 = plaintext[i]

        match int(x_vigenere_variant.value):
            case 1:
                if count < len(num_key):
                    key1 = num_key[count]
                    ciphertext += bytes([(ord(char0) + key1) % 256]).decode("latin-1")
                    count += 1
                if count == len(num_key):
                    count = 0
            case _:
                char = char0.lower()
                if char == " ":
                    ciphertext += " "
                elif char.isdigit():
                    ciphertext += char
                elif char.isalpha():
                    if count < len(num_key):
                        key1 = num_key[count]

                        match int(x_vigenere_variant.value):
                            case 0:
                                ciphertext += chr((ord(char) + key1 - 97) % 26 + 97)
                            case 2:
                                ciphertext += chr(
                                    (key1 - ord(char) + 97 % 26) % 26 + 97
                                )

                        count += 1
                    if count == len(num_key):
                        count = 0

    if int(x_vigenere_variant.value) == 1:
        ciphertext = base64.a85encode(ciphertext.encode("utf-8")).decode("utf-8")

    return ciphertext


def x_vigenere_decode(ciphertext, num_key):
    count = 0
    plaintext = ""

    if int(x_vigenere_variant.value) == 1:
        ciphertext = base64.a85decode(ciphertext).decode("utf-8")

    for i in range(len(ciphertext)):
        char0 = ciphertext[i]

        match int(x_vigenere_variant.value):
            case 1:
                if count < len(num_key):
                    key1 = num_key[count]
                    plaintext += bytes(
                        [(ord(char0.encode("latin-1")) - key1) % 256]
                    ).decode("latin-1")
                    count += 1
                if count == len(num_key):
                    count = 0
            case _:
                char = char0.lower()
                if char == " ":
                    plaintext += " "
                elif char.isdigit():
                    plaintext += char
                elif char.isalpha():
                    if count < len(num_key):
                        key1 = num_key[count]

                        match int(x_vigenere_variant.value):
                            case 0:
                                plaintext += chr((ord(char) - key1 - 97) % 26 + 97)
                            case 2:
                                plaintext += chr((key1 - ord(char) + 97 % 26) % 26 + 97)

                        count += 1
                    if count == len(num_key):
                        count = 0

    return plaintext


def x_vigenere_process_click(event):
    x = input.value
    key0 = x_vigenere_key.value

    num_key = []
    key = key0.lower()

    for i in range(len(key)):
        key1 = key[i]
        num_key.append(ord(key1) - 97)

    match int(is_encode.value):
        case 0:
            y = x_vigenere_decode(x, num_key)
        case 1:
            y = x_vigenere_encode(x, num_key)

    match int(x_vigenere_mode.value):
        case 1:
            y = y.replace(" ", "")
        case 2:
            y = y.replace(" ", "")
            y = [y[i : i + 5] for i in range(0, len(y), 5)]
            y = " ".join(y)
        case _:
            y = y

    output.value = y


def matrix_mod_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = egcd(det, modulus)[1] % modulus
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )

    return matrix_modulus_inv


def x_hill_encode(message, K):
    encrypted = ""
    message_in_numbers = []

    for letter in message:
        message_in_numbers.append(letter_to_index[letter])

    split_P = [
        message_in_numbers[i : i + int(K.shape[0])]
        for i in range(0, len(message_in_numbers), int(K.shape[0]))
    ]

    for P in split_P:
        P = np.transpose(np.asarray(P))[:, np.newaxis]

        while P.shape[0] != K.shape[0]:
            P = np.append(P, letter_to_index[" "])[:, np.newaxis]

        numbers = np.dot(K, P) % len(alphabet)
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            encrypted += index_to_letter[number]

    return encrypted


def x_hill_decode(cipher, Kinv):
    decrypted = ""
    cipher_in_numbers = []

    for letter in cipher:
        cipher_in_numbers.append(letter_to_index[letter])

    split_C = [
        cipher_in_numbers[i : i + int(Kinv.shape[0])]
        for i in range(0, len(cipher_in_numbers), int(Kinv.shape[0]))
    ]

    for C in split_C:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        numbers = np.dot(Kinv, C) % len(alphabet)
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            decrypted += index_to_letter[number]

    return decrypted


def x_hill_process_click(event):
    message = input.value.replace(" ", "")
    key = x_hill_key.value.lower()

    temp = []
    for letter in key:
        temp.append(letter_to_index[letter])
    mtx = np.array(temp).reshape(int(len(temp) / 2), 2)

    K = np.matrix(mtx)
    Kinv = matrix_mod_inv(K, len(alphabet))

    if int(is_encode.value) == 1:
        output.value = x_hill_encode(message, K)
    else:
        output.value = x_hill_decode(message, Kinv)


def x_base32_process_click(event):
    x = input.value

    if int(is_encode.value) == 1:
        if x_base32_std.checked:
            output.value = base64.b32encode(x.encode()).decode()
        elif x_base32_hex.checked:
            output.value = base64.b32hexencode(x.encode()).decode()
    else:
        if x_base32_std.checked:
            output.value = base64.b32decode(x).decode()
        elif x_base32_hex.checked:
            output.value = base64.b32hexdecode(x).decode()


def x_base64_process_click(event):
    x = input.value

    if int(is_encode.value) == 1:
        if x_base64_std.checked:
            output.value = base64.b64encode(x.encode()).decode()
        elif x_base64_url.checked:
            output.value = (
                base64.urlsafe_b64encode(x.encode()).decode().replace("=", "")
            )
    else:
        if x_base64_std.checked:
            output.value = base64.b64decode(x + "==").decode()
        elif x_base64_url.checked:
            output.value = base64.urlsafe_b64decode(x + "==").decode()


def x_ascii85_process_click(event):
    x = input.value

    if int(is_encode.value) == 1:
        output.value = base64.a85encode(x.encode()).decode()
    else:
        output.value = base64.a85decode(x).decode()


def x_unicode_process_click(event):
    x = input.value

    if x_unicode_sep.value == "":
        sep = " "
    else:
        sep = x_unicode_sep.value

    if int(is_encode.value) == 1:
        if x_unicode_unc.checked:
            temp = []
            for i in range(len(x)):
                unc = base64.b16encode(x[i].encode()).decode()
                temp.append("U+" + str(unc))
            output.value = sep.join(temp)
        if x_unicode_dec.checked:
            temp = []
            for i in range(len(x)):
                temp.append(str(ord(x[i])))
            output.value = sep.join(temp)
        if x_unicode_hex.checked:
            temp = []
            for i in range(len(x)):
                temp.append(hex(ord(x[i])).replace("0x", ""))
            output.value = sep.join(temp)
        if x_unicode_bin.checked:
            temp = []
            for i in range(len(x)):
                temp.append(bin(ord(x[i])).replace("0b", ""))
            output.value = sep.join(temp)
        if x_unicode_oct.checked:
            temp = []
            for i in range(len(x)):
                temp.append(oct(ord(x[i])).replace("0o", ""))
            output.value = sep.join(temp)
        if x_unicode_ndec.checked:
            temp = []
            for i in range(len(x)):
                ncr = str(ord(x[i]))
                temp.append("&#" + str(ncr) + ";")
            output.value = sep.join(temp)
        if x_unicode_nhex.checked:
            temp = []
            for i in range(len(x)):
                ncr = hex(ord(x[i])).replace("0x", "")
                temp.append("&#x" + str(ncr) + ";")
            output.value = sep.join(temp)
    else:
        if x_unicode_unc.checked:
            y = x.strip().replace("U+", "").split(sep)
            temp = []
            for i in range(len(y)):
                temp.append(base64.b16decode(y[i].encode()).decode())
            output.value = "".join(temp)
        if x_unicode_dec.checked:
            y = x.strip().split(sep)
            temp = []
            for i in range(len(y)):
                temp.append(chr(int(y[i])))
            output.value = "".join(temp)
        if x_unicode_hex.checked:
            y = x.strip().split(sep)
            temp = []
            for i in range(len(y)):
                temp.append(chr(int(y[i], 16)))
            output.value = "".join(temp)
        if x_unicode_bin.checked:
            y = x.strip().split(sep)
            temp = []
            for i in range(len(y)):
                temp.append(chr(int(y[i], 2)))
            output.value = "".join(temp)
        if x_unicode_oct.checked:
            y = x.strip().split(sep)
            temp = []
            for i in range(len(y)):
                temp.append(chr(int(y[i], 8)))
            output.value = "".join(temp)
        if x_unicode_ndec.checked:
            y = x.strip().replace("&#", "").replace(";", "").split(sep)
            temp = []
            for i in range(len(y)):
                temp.append(chr(int(y[i])))
            output.value = "".join(temp)
        if x_unicode_nhex.checked:
            y = x.strip().replace("&#x", "").replace(";", "").split(sep)
            temp = []
            for i in range(len(y)):
                temp.append(chr(int(y[i], 16)))
            output.value = "".join(temp)


def x_url_enc_process_click(event):
    x = input.value

    if int(is_encode.value) == 1:
        output.value = urllib.parse.quote(x, safe="")
    else:
        output.value = urllib.parse.unquote(x)


def x_hash_process_click(event):
    x = input.value

    if x_hash_md5.checked:
        output.value = hashlib.md5(x.encode()).hexdigest()
    elif x_hash_sha1.checked:
        output.value = hashlib.sha1(x.encode()).hexdigest()
    elif x_hash_sha256.checked:
        output.value = hashlib.sha256(x.encode()).hexdigest()
    elif x_hash_sha384.checked:
        output.value = hashlib.sha384(x.encode()).hexdigest()
    elif x_hash_sha512.checked:
        output.value = hashlib.sha512(x.encode()).hexdigest()


def x_hmac_process_click(event):
    x = input.value
    k = binascii.unhexlify(x_hmac_key.value).strip()

    if x_hmac_md5.checked:
        output.value = hmac.new(k, x.encode(), hashlib.md5).hexdigest()
    elif x_hmac_sha1.checked:
        output.value = hmac.new(k, x.encode(), hashlib.sha1).hexdigest()
    elif x_hmac_sha256.checked:
        output.value = hmac.new(k, x.encode(), hashlib.sha256).hexdigest()
    elif x_hmac_sha384.checked:
        output.value = hmac.new(k, x.encode(), hashlib.sha384).hexdigest()
    elif x_hmac_sha512.checked:
        output.value = hmac.new(k, x.encode(), hashlib.sha512).hexdigest()


def main():
    goto_feature.addEventListener("click", create_proxy(goto_feature_click))

    tab_encode.addEventListener("click", create_proxy(tab_encode_click))
    tab_decode.addEventListener("click", create_proxy(tab_decode_click))

    x_replace.addEventListener("click", create_proxy(x_replace_click))
    x_reverse.addEventListener("click", create_proxy(x_reverse_click))
    x_case.addEventListener("click", create_proxy(x_case_click))
    x_numeral.addEventListener("click", create_proxy(x_numeral_click))
    x_caesar.addEventListener("click", create_proxy(x_caesar_click))
    x_vigenere.addEventListener("click", create_proxy(x_vigenere_click))
    x_alphabetical.addEventListener("click", create_proxy(x_alphabetical_click))
    x_rail_fence.addEventListener("click", create_proxy(x_rail_fence_click))
    x_hill.addEventListener("click", create_proxy(x_hill_click))
    x_base32.addEventListener("click", create_proxy(x_base32_click))
    x_base64.addEventListener("click", create_proxy(x_base64_click))
    x_ascii85.addEventListener("click", create_proxy(x_ascii85_click))
    x_unicode.addEventListener("click", create_proxy(x_unicode_click))
    x_url_encode.addEventListener("click", create_proxy(x_url_encode_click))
    x_hash_func.addEventListener("click", create_proxy(x_hash_func_click))
    x_hmac.addEventListener("click", create_proxy(x_hmac_click))

    x_replace_process.addEventListener("click", create_proxy(x_replace_process_click))
    x_reverse_process.addEventListener("click", create_proxy(x_reverse_process_click))
    x_case_process.addEventListener("click", create_proxy(x_case_process_click))
    x_numeral_process.addEventListener("click", create_proxy(x_numeral_process_click))
    x_caesar_shift_p.addEventListener("click", create_proxy(x_caesar_shift_p_click))
    x_caesar_shift_m.addEventListener("click", create_proxy(x_caesar_shift_m_click))
    x_caesar_process.addEventListener("click", create_proxy(x_caesar_process_click))
    x_vigenere_process.addEventListener("click", create_proxy(x_vigenere_process_click))
    x_base32_process.addEventListener("click", create_proxy(x_base32_process_click))
    x_base64_process.addEventListener("click", create_proxy(x_base64_process_click))
    x_ascii85_process.addEventListener("click", create_proxy(x_ascii85_process_click))
    x_unicode_process.addEventListener("click", create_proxy(x_unicode_process_click))
    x_url_enc_process.addEventListener("click", create_proxy(x_url_enc_process_click))
    x_hash_process.addEventListener("click", create_proxy(x_hash_process_click))
    x_hmac_process.addEventListener("click", create_proxy(x_hmac_process_click))
    x_hill_process.addEventListener("click", create_proxy(x_hill_process_click))

    loading_done()


main()
