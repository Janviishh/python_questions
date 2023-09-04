def main():
    tuple1 = tuple(("one", "two", "three"))
    tuple2 = tuple(("1", "2", "3"))
    list1 = list(tuple1)
    list1[0]= "number"
    tuple1 = tuple(list1)
    list2= list(tuple2)
    list2[0] = "number"
    tuple2 = tuple(list2)
    # change value at index 0 of both tuple to string "number"
    # Your code goes here
    
    
    print(tuple1)
    print(tuple2)
    
    return 0

if __name__ == '__main__':
    main()
if __name__ == '__main__':
    main()

