if __name__ == '__main__':
    score_sheet = dict()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_sheet[name] = score

    scores = list( score_sheet.values() )
    scores.sort()
    
    second_max = scores[1]
    for x in scores:
        if x > scores[0]:
            second_max = x
            break;
    
    names = []
    for name in score_sheet:
        if score_sheet[name] == second_max:
            names.append(name)
    
    names.sort()
    for n in names: print(n)
