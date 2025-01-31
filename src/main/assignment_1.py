import math

def ApproximationAlgorithm(x0, tol):
    
    i = 0
    diff = x0
    x = x0
    
    print(f"{i} : {x}")
    
    while diff >= tol:
        i += 1
        y = x
        x = (x/2) + (1/x)
        
        print(f"{i} : {x}")
        
        diff = abs(x - y)
    
    print(f"\nConvergence after {i} iterations\n")

def BisectionMethod(a, b, N0, tol):
    
    p = 0
    i = 0
    
    while abs(b - a) > tol and i < N0:
        i += 1
        p = (a + b) / 2
        print(f"{i} : {p}")
        
        fa = a*a*a + 4 * a*a - 10
        fp = p*p*p + 4 * p*p - 10
        
        if (fa < 0 and fp > 0) or (fa > 0 and fp < 0):
            b = p
        else:
            a = p
    
    print(f"\np = {p}\n")

def FixedPointIteration(p0, N0, tol):
    
    res = "FAILURE"
    p = 0
    i = 1
    
    while i <= N0:
        # Equation a
        p = p0 - p0 * p0 * p0 - 4 * p0 * p0 + 10  
        
        # Equation b
        # p = math.sqrt(10 - p0*p0*p0) / 2  
        
        if math.isnan(p):
            print("\nResult diverges")
            break
        
        print(f"{i} : {p}")
        
        if abs(p - p0) < tol:
            res = "SUCCESS"
            break
        
        i += 1
        p0 = p
    
    print(f"\n{res} after {i} iterations\n")

def NewtonRaphsonMethod(ppre, tol, N0):
    
    i = 1
    
    print(f"{i} : {ppre}")
    while i <= N0:
        fpre = math.cos(ppre) - ppre
        fdpre = -math.sin(ppre) - 1
        
        if fdpre != 0:
            pnext = ppre - (fpre / fdpre)
            
            if abs(pnext - ppre) < tol:
                print(f"\npnext = {pnext}")
                print("SUCCESS")
                break
            
            i += 1
            ppre = pnext
            print(f"{i} : {ppre}")
        else:
            print("FAILURE, derivative = 0)")
            break
    
    if i > N0:
        print("Max iterations reached.")

if __name__ == "__main__":
    # test cases
    ApproximationAlgorithm(1.5, 0.000001)
    
    BisectionMethod(1, 2, 20, 0.001)
    
    FixedPointIteration(1.5, 25, 0.000001)
    
    NewtonRaphsonMethod(math.pi/4, 15 * 10**-15, 50)


