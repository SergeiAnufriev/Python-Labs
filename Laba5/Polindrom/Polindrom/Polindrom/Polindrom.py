print("Program opredelyet yvlyetsy li namber polindromom")

def pal(s):
    return "YES" if s == s[::-1] else "NO"
namber = input("Input namber: ") 
print(pal(namber.replace(" ", "").lower()))
