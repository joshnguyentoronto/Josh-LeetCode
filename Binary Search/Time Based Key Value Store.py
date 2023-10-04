'''
Design a time-based key-value data structure that can store multiple values for the same key 
at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:
    TimeMap() Initializes the object of the data structure.
    void set(String key, String value, int timestamp) 
        Stores the key key with the value value at the given time timestamp.
    String get(String key, int timestamp) 
        Returns a value such that set was called previously, with timestamp_prev <= timestamp. 
        If there are multiple such values, it returns the value associated with the largest timestamp_prev. 
        If there are no values, it returns "".


Example 1:
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
    TimeMap timeMap = new TimeMap();
    timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
    timeMap.get("foo", 1);         // return "bar"
    timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
    timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
    timeMap.get("foo", 4);         // return "bar2"
    timeMap.get("foo", 5);         // return "bar2"
'''

class TimeMap:

    def __init__(self):
        self.main = {}


    def set(self, key, value, timestamp):
        if key in self.main.keys():
            l, r = 0, len(self.main[key]) - 1
            index = 0
            while l <= r:
                m = (l + r) // 2
                if self.main[key][m][0] > timestamp:
                    r = m - 1
                    index = m
                elif self.main[key][m][0] < timestamp:
                    l = m + 1
                    index = m + 1
            if index < len(self.main[key]) - 1:
                self.main[key].insert( [timestamp, value], index )
            else:
                self.main[key].append( [timestamp, value] )
        else:
            self.main[key] = [ [timestamp, value] ]


    def get(self, key, timestamp):
        if key not in self.main.keys():
            return ""
        elif self.main[key][0][0] > timestamp:
            return ""
        else:
            l, r = 0, len(self.main[key]) - 1
            index = 0
            while l <= r:
                m = (l + r) // 2
                if self.main[key][m][0] == timestamp:
                    return self.main[key][m][1]
                elif self.main[key][m][0] > timestamp:
                    r = m - 1
                    index = m - 1
                elif self.main[key][m][0] < timestamp:
                    l = m + 1
                    index = m
            return self.main[key][index][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

            # insert in order to easily retrieve
            # for i in range(len(self.main[key])):
            #     if self.main[key][i][0] > timestamp:
            #         self.main[key].insert( [timestamp, value], i )
            #     elif i == len(self.main[key]) - 1:
            #         self.main[key].append( [timestamp, value] )


            # for i in range(len(self.main[key])):
            #     if self.main[key][i][0] == timestamp:
            #         return self.main[key][i][1]
            #     elif self.main[key][i][0] > timestamp:
            #         return cur
            #     else:
            #         cur = self.main[key][i][1]
            # return cur