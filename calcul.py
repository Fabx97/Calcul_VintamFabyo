ue1 = {
    'R101':10, 'R102':10, 'R103':7, 'R104':7, 'R105':0, 'R106':5,
    'R107':0, 'R108':6, 'R109':0, 'R110':5, 'R111':4, 'R112':2,
    'R113':5, 'R114':5, 'R115':0, 'SAE11':20, 'SAE12':20, 'SAE13':0,
    'SAE14':0, 'SAE15':0, 'SAE16':7
}

list_ue1 = [20] * len(ue1)  # 21 coefficients de 20


def calcul():
    total_note = 0
    total_coef = 0
    
    for note, coef in zip(ue1.values(), list_ue1):
        total_note += note * coef
        total_coef += coef
    
    moyenne = total_note / total_coef
    return moyenne


print("Moyenne UE1 :", calcul())
