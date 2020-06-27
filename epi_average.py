import math
import data_graphs
import scipy.integrate
import numpy
import matplotlib.pyplot as plt

def SIR_model(y, t, r, a):
    S, I, R = y
	
    dSdt = -r * S * I
    dIdt = r * S * I - a * I
    dRdt = a * I

    return [dSdt, dIdt, dRdt]

N = 2607000
I0 = 8
S0 = N - I0
R0 = 0.0
r = data_graphs.get_values()[1]
a = data_graphs.get_values()[0]

t = numpy.linspace(0, 600, 10000)

solution = scipy.integrate.odeint(SIR_model, [S0, I0, R0], t, args = (r, a))

plt.figure(figsize = [12, 6])
susceptibles = plt.plot(t, solution[:, 0], label = "S(t)")
infectives = plt.plot(t, solution[:, 1], label = "I(t)")
recovered = plt.plot(t, solution[:, 2], label = "R(t)")

def total_recovered(recovered):
    xvalues = recovered[0].get_xdata()
    yvalues = recovered[0].get_ydata()
    
    return yvalues[-1]

def generate_graph(susceptibles, infectives, recovered):
    plt.grid()
    plt.legend()
    plt.xlabel("Time(Days)")
    plt.ylabel("Individuals")
    plt.title("SIR Model")
    plt.show()
        
def find_R0():
    return (r * S0) / a

def maximum(infectives):
    xvalues = infectives[0].get_xdata()
    yvalues = infectives[0].get_ydata()
    max_infectives = max(yvalues)
    for i in range(len(xvalues)):
        if yvalues[i] == max_infectives:
            break

    return max_infectives, xvalues[i]

def duration(infectives):
    xvalues = infectives[0].get_xdata()
    yvalues = infectives[0].get_ydata()
    for i in range(len(yvalues)):
        if round(yvalues[i]) == 0:
            break

    return xvalues[i]

print("R0(Basic Reproduction Rate): " + str(round(find_R0(), 2)))
print("Maximum number of infectives: " + str(int(round(maximum(infectives)[0]))))
print("Time location of maximum number of infectives: " + str(round(maximum(infectives)[1], 2)) + " Days")
print("Total number of recovered: " + str(int(round(total_recovered(recovered)))))
print("Duration of the epidemic: " + str(round(duration(infectives), 2)) + " Days")
print("The graph of epidemic is generated.")
generate_graph(susceptibles, infectives, recovered)
