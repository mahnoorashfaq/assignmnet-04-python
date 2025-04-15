def main():
    Numbers: list[int] = [1, 2, 3, 4]

    for i in range(len(Numbers)):  
        element_at_index = Numbers[i]  
        Numbers[i] = element_at_index * 2 
        print(Numbers)

if __name__ == '__main__':
 main()