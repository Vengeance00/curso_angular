def calculoIVA():
    total = float(input("Total de la factura: "))
    iva = int(input("Porcentaje de iva: "))
    if iva != 0:
        if iva < 0:
            return "El iva no puede ser negativo"
    else:
        iva = 21
    return total * ((iva * 0.01) + 1)

print("Total con iva",calculoIVA())