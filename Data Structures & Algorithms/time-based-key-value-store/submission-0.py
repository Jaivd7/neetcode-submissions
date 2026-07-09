class TimeMap:

    def __init__(self):
        self.hmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key in self.hmap.keys()):
            self.hmap[key].append((value,timestamp))
        else:
            self.hmap[key] = [(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hmap.keys():
            curr = self.hmap[key]
            low = 0
            high = len(curr)-1
            #print(curr, len(curr))
            #print("low is", low, "high is ", high)
            while(low<=high):
                mid = (low+high)//2
                #print(curr[mid])
                if(curr[mid][1] == timestamp):
                    return curr[mid][0]
                elif(curr[mid][1]>timestamp):
                    high = mid - 1
                else:
                    low = mid + 1
                #print(low, high)
            if high >= 0:
                return curr[high][0]
            else:
                return ""
        else:
            return ""
