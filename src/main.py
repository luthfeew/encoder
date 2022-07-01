from pyodide import create_proxy

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

view_feature = Element("view_feature")
view_main = Element("view_main")


def goto_feature_click(event):
    view_main.element.style.display = "none"
    view_feature.element.style.display = "block"


def x_replace_click(event):
    view_main.element.style.display = "block"
    view_feature.element.style.display = "none"


def main():
    x_replace.element.addEventListener("click", create_proxy(x_replace_click))
    goto_feature.element.addEventListener("click", create_proxy(goto_feature_click))


main()
