"""
    MULTIVALUE CONTAINERS
    
    Sequences:
        Tuple
        List
        String
        
    Set
    Dictionary
    
    
    
    Properties
    1. Indexing
    2. Negative Indexing
    3. Slicing
    4. Concatenation
    5. Multiplicity
    6. Membership Testing
    """
    
#1D
#Indexing#
#   0  1  2
#  -1 -2 -3
my_data = [10, 20, 30]

#2D List (List of Lists)
numbers = [
    [10, 20, 30],
    [30, 40, 50],
    [60, 70, 80],
]


#3D List (List of List of Lists)
large_data = [
                [
                    [10, 20, 30],
                    [30, 40, 50],
                    [60, 70, 80],
                ],
                [
                    [140, 200, 30],
                    [30, 40, 50, 60, 5],
                    [60, 70],
                ],

             ]

print(my_data[0])
print(my_data[-1])
print(len(my_data))

print(numbers[0])
print(numbers[-1])
print(len(numbers))

print(large_data[0])
print(large_data[-1])
print(len(large_data))

print(large_data[1][0][0])
print(large_data[-1][-3][-3])


name = "John's Cafe"#better if 's is to be used
name = 'John\'s Cafe'#we have to define 's by using \
name = """John's Cafe
Welcome to Cafeteria
Today's Menu
Coffee
Cookie"""

print(name)
print(name[0])
print(name[-1])

#3. SLICING
data = list(range(10, 101, 10))
print("data is : ")
print(data)

print("data[0:3]",data[0:3])
print("data[3:7]",data[3:7])
print("data[5:]",data[5:])
print("data[:4]",data[:4])

print("data[:-5]",data[:-5])
print("data[-5:-2]",data[-5:-2])

email = "john@example.com"
print("email[-4:]", email[-4:])
print("email[12:]", email[12:])

#4. CONCATENATION
data1 = [10, 20, 30]
data2 = [40, 50, 60]

data3 = data1 + data2
print(data3)

#5. MULTIPLICITY
data4 = data1 * 2
print(data4)

prices = [100, 500, 500, 300]
prices1 = prices * 2
print(prices1)

#6. MEMBERSHIP TESTING
print(10 in prices)
print(100 not in prices)

quote = "Search the candle rather than cursing the darkness"
print(quote[6])




