
def main()
    series = [0, 1]

    # Taking User input 
    num_points = int(input("Enter num of terms required in Fibonacci Sequence :"))

    for i in range(2, num_points+1):
    #     print(i)

        temp = series[i-1] + series[i-2]

        series.append(temp)

    series.pop(0) # removing first element - zero
    print(series)
    return

if __name__ == '__main__':
    main()
