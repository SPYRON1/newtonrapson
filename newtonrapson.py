def squarerootNR(x,epsilon):
    """assume x>=0 and epsilon >0
    return y s.t. y*y is within epsilon of x"""
    assert x>=0,'x must be non negative,not'+str(x)
    assert epsilon>0,'epsilon must be positive,not'+str(epsilon)
    x=float(x)
    guess=x/2.0
    guess=0.001
    diff=guess**2-x
    ctr=1
    while abs(diff)>epsilon and ctr<=100:
        #print'error:',diff, 'guess',guess
        guess=guess-diff/(2.0*guess)
        diff=guess**2-x
        ctr+=1
    assert ctr<=100,'iteration count exceeded'
    print('Ni method Num.iteration',ctr,'estimation', guess)
    return guess
#squarerootNR(3, 0.001)