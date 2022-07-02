from pyodide import create_proxy
from js import console

x_replace = Element("x_replace").element
x_reverse = Element("x_reverse").element
x_case = Element("x_case_transform").element
x_numeral = Element("x_numeral_system").element
x_caesar = Element("x_caesar").element
x_vigenere = Element("x_vigenere").element
x_alphabetical = Element("x_alphabetical").element
x_rail_fence = Element("x_rail_fence").element
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

view_x_caesar = Element("view_x_caesar").element

input = Element("input").element
output = Element("output").element

x_caesar_shift = Element("x_caesar_shift").element
x_caesar_shift_plus = Element("x_caesar_shift_plus").element
x_caesar_shift_minus = Element("x_caesar_shift_minus").element
x_caesar_process = Element("x_caesar_process").element


def show_feature():
    view_main.style.display = "none"
    view_feature.style.display = "block"


def show_main(id):
    view_main.style.display = "block"
    view_feature.style.display = "none"
    breadcrumb1.innerHTML = id.closest(":not(button)").previousElementSibling.innerHTML
    breadcrumb2.innerHTML = id.innerHTML


def goto_feature_click(event):
    show_feature()


def x_replace_click(event):
    show_main(x_replace)


def x_reverse_click(event):
    show_main(x_reverse)


def x_case_click(event):
    show_main(x_case)


def x_numeral_click(event):
    show_main(x_numeral)


def x_caesar_click(event):
    show_main(x_caesar)
    view_x_caesar.style.display = "block"


def x_vigenere_click(event):
    show_main(x_vigenere)


def x_alphabetical_click(event):
    show_main(x_alphabetical)


def x_rail_fence_click(event):
    show_main(x_rail_fence)


def x_base32_click(event):
    show_main(x_base32)


def x_base64_click(event):
    show_main(x_base64)


def x_ascii85_click(event):
    show_main(x_ascii85)


def x_unicode_click(event):
    show_main(x_unicode)


def x_url_encode_click(event):
    show_main(x_url_encode)


def x_hash_func_click(event):
    show_main(x_hash_func)


def x_hmac_click(event):
    show_main(x_hmac)


def x_caesar_shift_plus_click(event):
    x_caesar_shift.value = int(x_caesar_shift.value) + 1


def x_caesar_shift_minus_click(event):
    x_caesar_shift.value = int(x_caesar_shift.value) - 1


def x_caesar_process_click(event):
    shift = int(x_caesar_shift.value)
    plaintext = input.value
    ciphertext = x_caesar_encrypt(plaintext, shift)
    output.value = ciphertext


def x_caesar_encrypt(plaintext, key_val):
    ciphertext = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        new_char = char.lower()
        if new_char == " ":
            ciphertext += " "
        elif char.isalpha():
            ciphertext += chr((ord(new_char) + key_val - 97) % 26 + 97)

    return ciphertext


def main():
    goto_feature.addEventListener("click", create_proxy(goto_feature_click))

    x_replace.addEventListener("click", create_proxy(x_replace_click))
    x_reverse.addEventListener("click", create_proxy(x_reverse_click))
    x_case.addEventListener("click", create_proxy(x_case_click))
    x_numeral.addEventListener("click", create_proxy(x_numeral_click))
    x_caesar.addEventListener("click", create_proxy(x_caesar_click))
    x_vigenere.addEventListener("click", create_proxy(x_vigenere_click))
    x_alphabetical.addEventListener("click", create_proxy(x_alphabetical_click))
    x_rail_fence.addEventListener("click", create_proxy(x_rail_fence_click))
    x_base32.addEventListener("click", create_proxy(x_base32_click))
    x_base64.addEventListener("click", create_proxy(x_base64_click))
    x_ascii85.addEventListener("click", create_proxy(x_ascii85_click))
    x_unicode.addEventListener("click", create_proxy(x_unicode_click))
    x_url_encode.addEventListener("click", create_proxy(x_url_encode_click))
    x_hash_func.addEventListener("click", create_proxy(x_hash_func_click))
    x_hmac.addEventListener("click", create_proxy(x_hmac_click))

    x_caesar_shift_plus.addEventListener(
        "click", create_proxy(x_caesar_shift_plus_click)
    )
    x_caesar_shift_minus.addEventListener(
        "click", create_proxy(x_caesar_shift_minus_click)
    )
    x_caesar_process.addEventListener("click", create_proxy(x_caesar_process_click))


main()
