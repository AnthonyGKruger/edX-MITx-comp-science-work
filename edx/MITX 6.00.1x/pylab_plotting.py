mys = []
myl = []
myq = []
myc = []
mye = []

from pylab import plt

for i in range(30):
    mys.append(i)
    myl.append(i)
    myq.append(i**2)
    myc.append(i**3)
    mye.append(1.5**i)

plt.figure('linear')
plt.title('linear')
plt.xlabel('my sample')
plt.ylabel('linear')
plt.plot(mys, myl, label = 'linear')

plt.figure('quadratic')
plt.clf()
plt.plot(mys, myq, label = 'quadratic')
plt.title('quadratic')
plt.xlabel('my sample')
plt.ylabel('quadratic')

plt.figure('cubic')
plt.clf()
plt.plot(mys, myc, label = 'quadratic')
plt.title('cubic')
plt.xlabel('my sample')
plt.ylabel('cubic')

plt.figure('exponential')
plt.clf()
plt.title('exponential')
plt.plot(mys, mye, label = 'exponential')
plt.xlabel('my sample')
plt.ylabel('exponential')
plt.ylim(1000)

plt.figure('exponential cubic')
plt.clf()
plt.title('exponential cubic')
plt.plot(mys, myc,'b--', label = 'cubic', linewidth = '3.0')
plt.plot(mys, mye,'r-', label = 'exponential', linewidth= '3.0')
plt.legend(loc = 'upper left')
