def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1 = list(str(num1))
    num2 = list(str(num2))

    num1_dic = {num:num1.count(num) for num in num1}
    num2_dic = {num:num2.count(num) for num in num2}

    count = 0


    for key in num1_dic.keys():
        try:
             num2_dic[key]
             if num2_dic[key] == num1_dic[key]:
                 count+=1
        except: 
            return False

    if count == len(num2_dic.keys()):
        return True
    else:
        return False