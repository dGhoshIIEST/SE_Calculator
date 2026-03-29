def hex_to_decimal(hex_str):
    if not hex_str.startswith("H'"):
        raise ValueError("Invalid HEX format")

    try:
        value = hex_str[2:]
        decimal = int(value, 16)
        return f"D'{decimal}"
    except:
        raise ValueError("Invalid HEX input")
