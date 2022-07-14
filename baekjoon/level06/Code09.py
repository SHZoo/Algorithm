word = input()
check_list = []

for iter in range(len(word)) :
    if word[iter] == 'c' and iter != len(word) -1 and word[iter + 1] == '=' :
        check_list.append('c=')
    elif word[iter] == 'c' and iter != len(word) -1 and word[iter + 1] == '-' :
        check_list.append('c-')
    elif word[iter] == 's' and iter != len(word) -1 and word[iter + 1] == '=' :
        check_list.append('s=')
    elif word[iter] == 'z' and iter != len(word) -1 and word[iter + 1] == '=' :
        if iter == 0 :
            check_list.append('z=')
        elif iter > 0 :
            if word[iter -1] == 'd' :
                pass
            else :
                check_list.append('z=')
    elif word[iter] == 'l' and iter != len(word) -1 and word[iter + 1] == 'j' :
        check_list.append('lj')
    elif word[iter] == 'n' and iter != len(word) -1 and word[iter + 1] == 'j' :
        check_list.append('nj')
    elif word[iter] == 'd' and iter != len(word) -1 and word[iter + 1] == '-' :
        check_list.append('d-')
    elif word[iter] == 'd' and iter < len(word) -2 and word[iter + 1] == 'z' and word[iter + 2] == '=' :
        check_list.append('dz=')
    elif word[iter] == 'j' and iter >= 0 and not (word[iter -1] == 'l') and not (word[iter -1 ] == 'n') :
        check_list.append('j')
    elif word[iter] != '=' and word[iter] != '-' and word[iter] != 'j' :
        check_list.append(word[iter])
    elif word[iter] == 'j' and iter == 0 :
        check_list.append('j')
    elif word[iter] == 'j' and iter > 0 :
        if word[iter -1] != 'n' or word[iter -1] != 'l' :
           pass
        else :
            check_list.append('j')
            
print(len(check_list))
    
    
