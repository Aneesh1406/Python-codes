def calculatepercentage(Obtained, Total = 500):
    output = ((Obtained/Total) * 100)
    return output
    
def main():   
    
    print("Enter obtained marks :")
    value2 = int(input())
    
    result = calculatepercentage(value2) #Default argument
    
    print("Percentage is : ",result)

if __name__=="__main__":
    main()