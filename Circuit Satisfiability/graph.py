import matplotlib.pyplot as plt

data = [
501.755280,
303.369553,
203.861919,
196.863818,
195.822393,
193.720058,
194.065160,
193.691350
]

processes = [
'1',
'2',
'4',
'8',
'16',
'32',
'64',
'128'
]

plt.plot(processes, data)
plt.title("Runtimes Circuit Satisfiability on different number of processors")
plt.xlabel("Number of processes ->")
plt.ylabel("Runtimes in seconds ->")
plt.xticks(processes)
plt.savefig("graph.jpg")
plt.show()