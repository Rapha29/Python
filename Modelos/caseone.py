def caminhosfechados(numero):
    closed_paths_dict = {
        0: 1,
        4: 1,
        6: 1,
        8: 2,
        9: 1
    }
    
    digits = list(str(numero))
    closed_paths_count = 0
    for digit in digits:
        digit = int(digit)
        if digit in closed_paths_dict:
            closed_paths_count += closed_paths_dict[digit]
    
    return closed_paths_count

if __name__ == "__main__":
    number = 630   #esse aqui é o stdin
    result = caminhosfechados(number)
    print(result)