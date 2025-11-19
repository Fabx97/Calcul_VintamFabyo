import matplotlib.pyplot as plt 

import numpy as np 

ue1note={
    "R101":10,
    "R102":10,
    "R103":10,
    "R104":2
}
ue1coef={
    "R101":5,
    "R102":5,
    "R103":5,
    "R104":5,
    "R105":10
}
ue2note={
    "R101":10,
    "R102":10,
    "R103":10,
    "R104":15
}
ue2coef={
    "R101":5,
    "R102":5,
    "R103":5,
    "R104":5,
    "R105":15
}
ue3note={
    "R101":10,
    "R102":10,
    "R103":10,
    "R104":20
}
ue3coef={
    "R101":5,
    "R102":5,
    "R103":5,
    "R104":5,
    "R105":20
}

def calcul():
    for element in (ue1note.keys()):
        total_note1 = 0
        total_coef1 = 0
        total_note2 = 0
        total_coef2 = 0
        total_note3 = 0
        total_coef3 = 0
        total_note1 += ue1note[element]*ue1coef[element] 
        total_coef1 += ue1coef[element]
        total_note2 += ue2note[element]*ue2coef[element]
        total_coef2 += ue2coef[element]
        total_note3 += ue3note[element]*ue3coef[element]
        total_coef3 += ue3coef[element]
        moyenne_ue1 = total_note1 / total_coef1
        moyenne_ue2 = total_note2 / total_coef2
        moyenne_ue3 = total_note3 / total_coef3
    plt.bar(["ue1","ue2","ue3"],[moyenne_ue1, moyenne_ue2, moyenne_ue3])
    def color(value):
        if value > 10:
            return 'green'
        elif value > 8:
            return 'orange'
        else:
            return 'red'
