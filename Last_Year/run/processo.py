
from typing import Counter

with open("results.txt", "a") as file:
    file.write("")
    file.write("Run")

with open("results.txt", "r") as f:
    
    validRuns = 0

    linhas = f.readlines()
    count = 0
    resultados = []
    for linha in linhas:
        if linha.startswith("Run") and count > 3:
            resultados = linhas[count-2].split("   ")
            resultados.pop(0)

            numberOf5s = 0
            numberOf6s = 0

            for resultadoIdx in range(0, len(resultados)):
                resultados[resultadoIdx] = resultados[resultadoIdx].strip()
                resultados[resultadoIdx] = int(resultados[resultadoIdx])
                if resultados[resultadoIdx] == 5:
                    numberOf5s += 1
                if resultados[resultadoIdx] == 6:
                    numberOf6s += 1

            if numberOf5s == 5 and numberOf6s == 5:
                validRuns += 1

        count += 1 

print(validRuns)
