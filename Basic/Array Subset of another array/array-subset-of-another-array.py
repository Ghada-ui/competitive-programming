#User function Template for python3

def isSubset( a1, a2, n, m):
    dict_a1 = {}
    for item in a1:
        dict_a1[item] = dict_a1.get(item, 0) + 1
        
    for item in a2:
        if item not in dict_a1 or dict_a1[item] == 0:
            return 'No'
        dict_a1[item] -= 1
        
    return 'Yes'
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends