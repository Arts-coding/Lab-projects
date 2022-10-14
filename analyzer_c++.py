from data import keywords_list,varable_list,function_list

result_dict = {
    "variables": 0,
    "functions": 0,
    "keywords": 0,
    "class": 0
}


file1 = open('test.cpp', 'r')
file_cpp = file1.readlines()


def class_count(class_file, indx):
    if class_file[indx] == "class":
        result_dict["class"] += 1

def functionArgs_count(arg_lst):
    name_func = ''
    arg_str = ""
    ind = 0

    for y in arg_lst:
        arg_str += y + " "

    for i in range(len(arg_str)):
        if arg_str[i] == "(":
            ind = i
                    
        elif arg_str[i] == ")":
            name_func = arg_str[:ind]
            result_dict[name_func] = 0
            arg_str = arg_str.replace(arg_str, arg_str[ind + 1:i])
            break   
    
    arg_count_lst = arg_str.split()

    for x in arg_count_lst:
        if x in varable_list:
            result_dict[name_func] += 1

def functions_count(arg, indx):
    for x in function_list:
        if x in arg[indx] and arg[indx + 1].count("(") != 0:
            result_dict["functions"] += 1
            functionArgs_count(arg[indx+ 1:])

    if arg[indx][0] == "*" and arg[indx][-2].count("(") != 0 and arg[indx][-1].count(")") != 0:
            functionArgs_count(arg[indx])
            result_dict["functions"] += 1

def variables_count(arg, indx):
    for x in varable_list:
        if x in arg[indx] and arg[indx + 1].count("(") == 0:
            result_dict["variables"] += 1

    if arg[indx][0] == "*":
        if  arg[indx].count("(") == 0 and arg[indx][:-1].count(")") == 0:
            result_dict["variables"] += 1

def keywords_count():
    for x in file_cpp:
        if x == "\n":
            file_cpp.remove(x) 

    for y  in file_cpp:
        run_file = y.split()

        for i in range(len(run_file)):
            if len(run_file[i]) == 0 :
                del run_file[i]
                continue

            variables_count(run_file, i - 1)
            functions_count(run_file, i - 1)
            class_count(run_file, i - 1)

            if run_file[i][0] == '"' and "'":
                continue
            else:
                for x in keywords_list:
                    if x in run_file[i] and run_file[i].count(")") == 0:
                        result_dict["keywords"] +=1
            
    return result_dict
        
print(keywords_count()) 

with open("result.txt", 'w') as f: 
    for key, value in result_dict.items(): 
        f.write('%s:%s\n' % (key, value))