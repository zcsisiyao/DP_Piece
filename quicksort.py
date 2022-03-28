class QuickSort:

    def __init__(self, nums):
        self.lis = nums

    def quicksort(self):
        low, high = 0, len(self.lis) - 1
        self.quick(low, high)
        return self.lis

    def quick(self, low, high):
        if low < high:
            pivotpos = self.Partition(low, high)
            self.quick(low, pivotpos)
            self.quick(pivotpos+1, high)
    def Partition(self, low, high):
        prvot = self.lis[low]
        while low < high:
            while low < high and self.lis[high] >= prvot:
                high -= 1
            self.lis[low] = self.lis[high]
            while low < high and self.lis[low] <= prvot:
                low += 1
            self.lis[high] = self.lis[low]
        self.lis[low] = prvot
        return low
if __name__=="__main__":
    a = QuickSort([5, 2, 85, 34, 74, 2, 74, 6, 45, 8, 17, 2, 90, 7]).quicksort()
    print(a)