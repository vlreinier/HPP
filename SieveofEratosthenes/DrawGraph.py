import matplotlib.pyplot as plt

hundred_thousand = [0.58134, 0.72418, 0.43484, 0.40433, 0.30308, 0.88535]
million = [20.96852, 23.48197, 13.725178, 9.85413, 9.26566, 11.67370]
ten_million = [574.22539, 716.24521, 418.00950, 316.41230, 312.063257, 316.33694]

processes = [
'SEQ',
'PAR 1',
'PAR 2',
'PAR 4',
'PAR 8',
'PAR 16',
]

for i in [hundred_thousand, million, ten_million]:
    plt.title("Runtimes Sieve of Eratosthenes")
    plt.xlabel("Number of processes ->")
    plt.ylabel("Runtimes in seconds ->")
    plt.plot(processes, i)
    name = [k for k,v in locals().items() if v == i][0].replace("\n", "")
    plt.savefig(f"{name}.jpg")
    plt.close()