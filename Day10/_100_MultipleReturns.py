# Multiple return statements
def format_name(f_name, l_name):
    if f_name =="" or l_name == "":
        return "No valide inputs has been provided!"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Results: {formatted_f_name} {formatted_l_name}"
print( format_name("TeDDy", "rosE"))
# provide empty values
print( format_name("", ""))