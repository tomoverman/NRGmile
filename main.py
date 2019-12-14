import numpy as np
import math
# integrate difficulty function numerically using composite trapezoidal rule
def integrate_trap(dist, alt, z):
    n=len(dist)
    x=np.linspace(0,dist[n-1],n*5)
    val=0
    a=4.2351
    for i in range(0,n*5-1):
        ddist1 = eval_interp_deriv(x[i+1],z,dist,alt)
        ddist = eval_interp_deriv(x[i], z, dist, alt)
        val += ((x[i+1]-x[i])/2) * (np.exp(a*ddist1/5280) + np.exp(a*ddist/5280))
    return val


# integrate difficulty function numerically using composite simpson's rule
def integrate_simp(dist, alt, z):
    n=len(dist)
    nodes=int(math.ceil(n*5/2)*2)
    x=np.linspace(0,dist[n-1],nodes)
    val=0
    a=4.2351
    h=(x[nodes-1]-x[0])/(nodes)
    for i in range(1,(nodes)/2):
        ddist = eval_interp_deriv(x[2*i-2],z,dist,alt)
        ddist1 = eval_interp_deriv(x[2*i-1],z,dist,alt)
        ddist2 = eval_interp_deriv(x[2*i],z,dist,alt)
        val += (h/3) * (np.exp(a*ddist/5280) + 4*np.exp(a*ddist1/5280) + np.exp(a*ddist2/5280))
    return val

def segment_solver(dist, alt, z, nrg, num_days):
    day = nrg/num_days
    n = len(dist)
    nodes = int(math.ceil(n * 5 / 2) * 2)
    x = np.linspace(0, dist[n - 1], nodes)
    val = 0
    a = 4.2351
    h = (x[nodes - 1] - x[0]) / (nodes)
    count=1
    s=np.zeros(num_days)
    for i in range(1, (nodes) / 2):
        ddist = eval_interp_deriv(x[2 * i - 2], z, dist, alt)
        ddist1 = eval_interp_deriv(x[2 * i - 1], z, dist, alt)
        ddist2 = eval_interp_deriv(x[2 * i], z, dist, alt)
        val += (h / 3) * (np.exp(a * ddist / 5280) + 4 * np.exp(a * ddist1 / 5280) + np.exp(a * ddist2 / 5280))
        if val >= day*count:
            s[count-1]=x[2*i]
            count += 1
    return s

# find z values of natural cubic spline used to characterize the cubic spline interpolant
def interp(dist, alt):
    n = len(dist)
    v=np.zeros(n)
    u=np.zeros(n)
    z=np.zeros(n)
    h=np.zeros(n)
    b=np.zeros(n)
    for i in range(0,n-1):
        h[i] = dist[i+1]-dist[i]
        b[i] = (alt[i+1]-alt[i])/h[i]
    u[0] = 2*(h[0] + h[1])
    v[0] = 6*(b[1]-b[0])
    for i in range(1,n-2):
        u[i] = 2*(h[i+1] + h[i]) - h[i]**2/u[i-1]
        v[i] = 6*(b[i+1] - b[i]) - h[i]*v[i-1]/u[i-1]
    z[n-1]=0
    for i in reversed(range(2, n-1)):
        z[i]=(v[i-1]-h[i]*z[i+1])/u[i-1]
    z[0]=0
    return z


# find the value of the cubic spline interpolant at the given distance
def eval_interp(x,z,dist,alt):
    n=len(dist)
    for i in reversed(range(0,n-1)):
        if x-dist[i]>=0:
            break
    h=dist[i+1]-dist[i]
    tmp=(z[i]/2) + (x-dist[i])*(z[i+1]-z[i])/(6*h)
    tmp=-(h/6)*(z[i+1]+2*z[i])+(alt[i+1]-alt[i])/h + (x-dist[i])*tmp
    val = alt[i] + (x-dist[i])*tmp
    return val


# # find the value of the first derivative of the cubic spline interpolant at the given distance
def eval_interp_deriv(x,z,dist,alt):
    n=len(dist)
    for i in reversed(range(0,n-1)):
        if x-dist[i]>=0:
            break
    h=dist[i+1]-dist[i]
    val=(z[i+1]/(2*h)) * (x-dist[i])**2 - (z[i]/(2*h)) * (dist[i+1]-x)**2 + (alt[i+1]/h - h*z[i+1]/6) - (alt[i]/h-h*z[i]/6)
    return val