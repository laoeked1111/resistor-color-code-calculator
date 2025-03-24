
# numerical values that correspond to each color band on the resistor
COLORS = {
    "BLACK": 0, 
    "BROWN": 1, 
    "RED": 2, 
    "ORANGE": 3, 
    "YELLOW": 4, 
    "GREEN": 5, 
    "BLUE": 6, 
    "VIOLET": 7, 
    "GRAY": 8, 
    "WHITE": 9,
    "GOLD": -1,
    "SILVER": -2,
    "PINK": -3
}

# percentage tolerances that correspond to each color
TOLERANCES = {
    "BROWN": 1,
    "RED": 2,
    "ORANGE": 0.05,
    "YELLOW": 0.02,
    "GREEN": 0.5,
    "BLUE": 0.25,
    "VIOLET": 0.1,
    "GRAY": 0.01, 
    "GOLD": 5,
    "SILVER": 10, 
    None: 0
}


def color_to_value(color1, color2, color3, color4=None):
    """
    Converts either a 3- or 4-band resistor color code into its value.

    Args:
        color1: str, corresponds to a value band
        color2: str, corresponds to a value band
        color3: str, corresponds to the multiplier band
        color4: str, corresponds to the tolerance. Default is None.

    Ret:
        min_val: minimum resistance value given by calculated value and tolerance
        val: nominal value of resistance
        max_val: maximum resistance value given by calculated value and tolerance
    """

    assert color1 in COLORS, AssertionError("Color 1 not valid!")
    assert color2 in COLORS, AssertionError("Color 2 not valid!")
    assert color3 in COLORS, AssertionError("Color 3 not valid!")
    assert color4 in TOLERANCES, AssertionError("Color 4 not valid!")

    val = (COLORS[color1] * 10 + COLORS[color2]) * (10 ** COLORS[color3])
    tol = TOLERANCES[color4]
    max_val = val * (1+tol/100)
    min_val = val * (1-tol/100)

    return min_val, val, max_val 




def value_to_prefix(val, decimals=2):

    """
    Converts a value of a resistor to a string form with certain decimal placesfor better readability.

    Args:
        val: number, the value of the resistor
        decimals: int, number of decimal places in the return value

    Ret:
        str, the value rewritten with SI prefix
    """

    num = val
    unit = "R"
    if val >= 1e9:
        num = val / 1e9
        unit = "GR"
    elif val >= 1e6:
        num = val / 1e6
        unit = "MR"
    elif val >= 1e3:
        num = val / 1e3
        unit = "kR"
    
    return f"{num: .{decimals}f} {unit}"



def value_tol_to_color(val, tol=0):
    """
    Gives the band colors that would be on a resistor of resistance {val} and tolerance {tol}. 
    If {tol} not in {TOLERANCES}, use the largest value that is less than {tol}.

    Args:
        val: num, resistance value
        tol: num, tolerance on resistor, taken as a percentage
    
    Ret:
        colors: 3-4 element tuple of strings containing the colors on the resistor
    """

    num = val
    multiplier = 0

    while num < 10 or num > 99:
        if num < 10:
            num *= 10
            multiplier -= 1
        if num > 99:
            num /= 10
            multiplier += 1
    
    assert multiplier in COLORS.values(), AssertionError("No valid multiplier band!")

    color1, color2, color3, color4 = None, None, None, None

    for color, value in COLORS.items():
        if value == num // 10: color1 = color
        if value == num % 10: color2 = color
        if value == multiplier: color3 = color
    
    if tol == 0:
        return color1, color2, color3
    
    tol_diff = tol
    for color, tolerance in TOLERANCES.items():
        if abs(tol - tolerance) < tol_diff:
            tol_diff = abs(tol - tolerance)
            color4 = color
    
    return color1, color2, color3, color4



def three_value_to_color(min_val, val, max_val):
    """
    Gives the band colors that would be aon a resistor of resistance {val}, with maximum standard tolerance range 
    allowed by both {min_val} and {max_val}. 

    Args:
        min_val: num, minimum resistance value allowed
        val: num, nominal resistance value
        max_val: num, maximum resistance value allowed

    Ret:
        colors: 3-4 element tuple of strings containing colors on the resistor
    """

    min_diff = abs((min_val - val) / val) * 100
    max_diff = abs((max_val - val) / val) * 100

    tol = min(min_diff, max_diff)

    return value_tol_to_color(val, tol)
