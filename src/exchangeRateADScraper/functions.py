import global_vars


def get_code_month(string_month):
    code_month = None
    if string_month is not None and " " in string_month.strip():
        code_month = string_month.split()[0]
        code_month = global_vars.LIST_MONTH.get(code_month)
    return code_month
