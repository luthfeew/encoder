import base64
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

view_x_replace = Element("view_x_replace").element
view_x_reverse = Element("view_x_reverse").element
view_x_case = Element("view_x_case").element
view_x_numeral = Element("view_x_numeral").element
view_x_caesar = Element("view_x_caesar").element
view_x_base32 = Element("view_x_base32").element
view_x_base64 = Element("view_x_base64").element
view_x_ascii85 = Element("view_x_ascii85").element

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

x_base32_std = Element("x_base32_std").element
x_base32_hex = Element("x_base32_hex").element
x_base32_process = Element("x_base32_process").element

x_base64_std = Element("x_base64_std").element
x_base64_url = Element("x_base64_url").element
x_base64_process = Element("x_base64_process").element

x_ascii85_std = Element("x_ascii85_std").element
# x_ascii85_z85 = Element("x_ascii85_z85").element
x_ascii85_process = Element("x_ascii85_process").element


def show_feature():
    view_main.classList.add("is-hidden")
    view_feature.classList.remove("is-hidden")
    input.value = ""
    output.value = ""
    view_x_replace.classList.add("is-hidden")
    view_x_reverse.classList.add("is-hidden")
    view_x_case.classList.add("is-hidden")
    view_x_numeral.classList.add("is-hidden")
    view_x_caesar.classList.add("is-hidden")
    view_x_base32.classList.add("is-hidden")
    view_x_base64.classList.add("is-hidden")
    view_x_ascii85.classList.add("is-hidden")


def show_main(id):
    view_main.classList.remove("is-hidden")
    view_feature.classList.add("is-hidden")
    breadcrumb1.innerHTML = id.closest(":not(button)").previousElementSibling.innerHTML
    breadcrumb2.innerHTML = id.innerHTML


def switch_input():
    temp = input.value
    input.value = output.value
    output.value = temp


def tab_encode_click(event):
    if not tab_encode.classList.contains("is-active"):
        tab_encode.classList.add("is-active")
        tab_decode.classList.remove("is-active")
        is_encode.value = 1
        switch_input()


def tab_decode_click(event):
    if not tab_decode.classList.contains("is-active"):
        tab_encode.classList.remove("is-active")
        tab_decode.classList.add("is-active")
        is_encode.value = 0
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


def x_alphabetical_click(event):
    show_main(x_alphabetical)


def x_rail_fence_click(event):
    show_main(x_rail_fence)


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


def x_url_encode_click(event):
    show_main(x_url_encode)


def x_hash_func_click(event):
    show_main(x_hash_func)


def x_hmac_click(event):
    show_main(x_hmac)


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
    x_base32_process.addEventListener("click", create_proxy(x_base32_process_click))
    x_base64_process.addEventListener("click", create_proxy(x_base64_process_click))
    x_ascii85_process.addEventListener("click", create_proxy(x_ascii85_process_click))


main()
