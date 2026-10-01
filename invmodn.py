import math
def invmodn(b,n): 

#function y = invmodn( b,n);
    '''
    This function calculates the inverse of an element b mod n
    It uses the extended euclidean algorithm
    '''

    n0=n
    b0=b
    t0=0
    t=1

    q=math.floor(n0/b0)
    r=n0-q*b0

    while r>0:
        temp=t0-q*t
        if temp>=0: 
            #(temp >=0),
            #temp=mod(temp,n);
            temp = temp % n
        #end;
        if temp < 0:
            temp= n - ( (-temp) % n) #mod(-temp,n));
        #end;
        t0=t
        t=temp
        n0=b0
        b0=r
        q=math.floor(n0/b0)
        r=n0-q*b0
    #end

    if b0 !=1:
        y=[]

        #disp('No inverse');
    else:
        y = t % n
        #return y
        #y=mod(t,n)
    #end;
    return y  