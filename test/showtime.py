from test import NoFirst


class Second(NoFirst):
    def __init__(self,a,b,c):
       NoFirst.__init__(self,a,b,c)
    def show(self):
        print("你真秀")