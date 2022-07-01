from pyodide import create_proxy
from js import console

x_replace = Element("x_replace")
x_reverse = Element("x_reverse")
x_case_transform = Element("x_case_transform")
x_numeral_system = Element("x_numeral_system")
x_caesar = Element("x_caesar")
x_vigenere = Element("x_vigenere")
x_alphabetical = Element("x_alphabetical")
x_rail_fence = Element("x_rail_fence")
x_base32 = Element("x_base32")
x_base64 = Element("x_base64")
x_ascii85 = Element("x_ascii85")
x_unicode = Element("x_unicode")
x_url_encode = Element("x_url_encode")
x_hash_func = Element("x_hash_func")
x_hmac = Element("x_hmac")

goto_feature = Element("goto_feature")

breadcrumb1 = Element("breadcrumb1")
breadcrumb2 = Element("breadcrumb2")

view_feature = Element("view_feature")
view_main = Element("view_main")


def show_feature():
    view_main.element.style.display = "none"
    view_feature.element.style.display = "block"


def show_main(id):
    view_main.element.style.display = "block"
    view_feature.element.style.display = "none"

    breadcrumb1.element.innerHTML = id.element.closest(
        ":not(button)"
    ).previousElementSibling.innerHTML
    breadcrumb2.element.innerHTML = id.element.innerHTML


def goto_feature_click(event):
    show_feature()


def x_replace_click(event):
    show_main(x_replace)


def x_reverse_click(event):
    show_main(x_reverse)


def x_case_transform_click(event):
    show_main(x_case_transform)


def x_numeral_system_click(event):
    show_main(x_numeral_system)


def x_caesar_click(event):
    show_main(x_caesar)


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


def main():
    goto_feature.element.addEventListener("click", create_proxy(goto_feature_click))
    x_replace.element.addEventListener("click", create_proxy(x_replace_click))
    x_reverse.element.addEventListener("click", create_proxy(x_reverse_click))
    x_case_transform.element.addEventListener(
        "click", create_proxy(x_case_transform_click)
    )
    x_numeral_system.element.addEventListener(
        "click", create_proxy(x_numeral_system_click)
    )
    x_caesar.element.addEventListener("click", create_proxy(x_caesar_click))
    x_vigenere.element.addEventListener("click", create_proxy(x_vigenere_click))
    x_alphabetical.element.addEventListener("click", create_proxy(x_alphabetical_click))
    x_rail_fence.element.addEventListener("click", create_proxy(x_rail_fence_click))
    x_base32.element.addEventListener("click", create_proxy(x_base32_click))
    x_base64.element.addEventListener("click", create_proxy(x_base64_click))
    x_ascii85.element.addEventListener("click", create_proxy(x_ascii85_click))
    x_unicode.element.addEventListener("click", create_proxy(x_unicode_click))
    x_url_encode.element.addEventListener("click", create_proxy(x_url_encode_click))
    x_hash_func.element.addEventListener("click", create_proxy(x_hash_func_click))
    x_hmac.element.addEventListener("click", create_proxy(x_hmac_click))


main()
