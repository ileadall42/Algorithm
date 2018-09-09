def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    symbol=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    value=[1000,900,500,400, 100, 90,  50, 40,  10, 9,   5,  4,   1]
    str=''
    i=-1

    while num != 0:
        i+=1
        while value[i]<=num:
            num-=value[i]
            str+=symbol[i]
    return str

def intToRoman2(num):
    str=''
    symbol_value={
        "M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1
    }
    for key in symbol_value:
        while num!=0 and symbol_value[key]<=num:
            num-=symbol_value[key]
            str+=key
    return str




print(intToRoman(5))
print(intToRoman2(5))