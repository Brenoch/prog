
"""
def Vogal_Consoante(vogal, consoante):
    match vogal:
        case "A, E, I, O, U":
            print("Vogal")
tentar em casa depois

            """

def e_vogal(letra):
    match letra:
        case "a" | "e" | "i" | "o" | "u":
            return True
    return False # caso contrário

def main():
    print(e_vogal("a"))

main()
