#creates the obstacle limits you specify--------
class obstacle():
    def __init__(x,y,l,h):
        r=1
    def limits(x,y,l,h):
        lx=x
        ly=600
        ll=x+l
        lh=ly-h
        return [lx,ly,ll,lh]
        
        
