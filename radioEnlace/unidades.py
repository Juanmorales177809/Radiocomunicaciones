from tkinter import messagebox
import convertir


def agregar(valor,unidadDe,unidadA):
    # try:
        num = valor
        if unidadDe == "W":
            if unidadA == "W":
                messagebox.showerror("Error", message='No puede elegir las mismas unidades')
                return num, unidadDe
            elif unidadA == "mW":
                conv= convertir.watsMwats(num)
                return conv, unidadA
                insertar(textUnit,'mW')
            elif unidadA=="dB":
                conv= convertir.todB(num)
                return conv, unidadA
            elif unidadA=="dBm":
                conv= convertir.todB(num)
                conv= convertir.dBDBm(conv)
                return conv, unidadA
            else:
                messagebox.showerror("Error", message='No es una entrada valida')
        elif unidadDe == "mW":
            if unidadA == "W":
                conv= convertir.mWatsWats(num)
                return conv, unidadA
            elif unidadA == "mW":
                messagebox.showerror("No puede elegir las mismas unidades")
                return num, unidadA
            elif unidadA=="dBm":
                conv= convertir.todBm(num)
                return conv, unidadA
            elif unidadA=="dB":
                conv= convertir.todBm(num)
                conv= convertir.dBmDB(conv)
                return conv, unidadA
            else:
                messagebox.showerror("Error", message='No es una entrada valida')
        elif unidadDe == "dB":
            if unidadA == "W":
                conv= convertir.toWats(num)
                return conv, unidadA
            elif unidadA == "dB":
                messagebox.showerror("No puede elegir las mismas unidades")
                return num, unidadA
            elif unidadA=="dBm":
                conv= convertir.dBDBm(num)
                return conv, unidadA
            elif unidadA=="mW":
                conv= convertir.dBDBm(num)
                conv= convertir.tomWats(conv)
                return conv, unidadA
            else:
                messagebox.showerror("Error", message='No es una entrada valida')
        elif unidadDe == "dBm":
            if unidadA == "W":
                conv= convertir.dBmDB(num)
                conv= convertir.toWats(conv)
                return conv, unidadA
            elif unidadA == "dBm":
                messagebox.showerror("No puede elegir las mismas unidades")
                return num, unidadA
            elif unidadA=="dB":
                conv= convertir.dBmDB(num)
                return conv, unidadA
            elif unidadA=="mW":
                conv= convertir.tomWats(num)
                return conv, unidadA
            else:
                messagebox.showerror("Error", message='No es una entrada valida')
        elif unidadDe == "mW":
            if unidadA == "W":
                conv= convertir.mWatsWats(num)
                return conv, unidadA
            elif unidadA == "mW":
                messagebox.showerror("No puede elegir las mismas unidades")
                return num, unidadA
            elif unidadA=="dBm":
                conv= convertir.todBm(num)
                return conv, unidadA
            elif unidadA=="dB":
                conv= convertir.mWatsWats(num)
                conv= convertir.todB(conv)
                return conv, unidadA
            else:
                messagebox.showerror("Error", message='No es una entrada valida')
        elif unidadDe == "metros":
            if unidadA == "Kilometros":
                conv= convertir.meToKm(num)
                return conv, unidadA
            elif unidadA == 'metros':
                return num, unidadA
            else:
                messagebox.showerror("Error", message='No es una entrada valida')
        elif unidadDe == "Kilometros":
            if unidadA == "metros":
                conv= convertir.kmToM(num)
                return conv, unidadA
            elif unidadA == 'Kilometros':
                return num, unidadA
            else:
                messagebox.showerror("Error", message='No es una entrada valida')
        elif unidadDe == "dBd":
            if unidadA == "dBi":
                conv= convertir.dBdTodBi(num)
                return conv, unidadA
            elif unidadA == "dBd":
                return num, unidadA
            else:
                messagebox.showerror("Error", message='No es una entrada valida') 
        elif unidadDe == "dBi":
            if unidadA == "dBd":
                conv= convertir.dBiTodBd(num)
                return conv, unidadA
            elif unidadA == "dBi":
                return num, unidadA
            else:
                messagebox.showerror("Error", message='No es una entrada valida')
    # except:
    #     messagebox.showerror("Error", message='Ingrese valores')