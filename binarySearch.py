
class binarySearch(object):
    def __init__(self,end,step):
        self.step = step
        self.end = end
        #the 3 nmethods produces array for binary search
        if self.end in self.toTwenty():
            self.nList = self.toTwenty()
        elif self.end in self.toForty():
            self.nList = self.toForty()
        elif self.end in self.toOneThousand():
            self.nList = self.toOneThousand()

        self.length = len(self.nList)
        #getter method to return self as array
    def __getitem__(self, index):
        return self.nList[index]
        #List comprehension
    def toTwenty(self):
        return [n for n in range(self.step,(self.end * self.step)+1, self.step)]
    def toForty(self):
        return [n for n in range(self.step,(self.end * self.step)+1,self.step)]
    def toOneThousand(self):
        return [n for n in range(self.step,(self.end * self.step)+1,self.step)]
        #binary search


    def search(self,num):
        count = 0
        lower = 0
        upper = self.length-1
        mid = (lower+upper)//2 #same as int((lower+upper)/2)
        #if our num is at the step return index 0
        if num == self.nList[lower]:
            mid = lower
            #if our num is at the end return last index(righ)
        elif num == self.nList[upper]:
            mid = upper
        while lower <= upper and self.nList[mid] != num:
            count += 1
            if self.nList[mid] == num:
                return {"count": count, "index": mid}
            elif self.nList[mid] > num:
                #working with the upper half
                upper = mid-1
            else:
                #working with the upper half
                lower = mid+1
            mid = (lower+upper)//2
        if lower > upper:
            return {"count": 0, "index": -1}#num not found
        return {"count": count, "index":mid}