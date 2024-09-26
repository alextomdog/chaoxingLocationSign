def cookie_serialize(cookies):
    result = ""
    for key, value in cookies.items():
        if key == "account_username":
            continue
        result += f"{key}={value}; "
    return result[:-2]
