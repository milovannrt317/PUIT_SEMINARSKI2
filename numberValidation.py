# funkcije iskoriscene za ogranicavanje unosa korisnika na samo brojevne vrednosti
def tryFloatInt(st, opc):
    try:
        if opc == 'int':
            int(st)
        else:
            float(st)
        return True
    except ValueError:
        return False


def validateFloat(P):
    if P == "" or P == '-' or tryFloatInt(P, "float"):
        return True
    else:
        return False


def validateInt(P):
    if P == "" or tryFloatInt(P, "int"):
        return True
    else:
        return False
