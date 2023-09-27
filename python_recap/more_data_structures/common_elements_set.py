def common_elements(set_1, set_2):
    # set_1 & set_2 intersection
    # set_1 | set_2 union
    #set_1 ^ set_2 symetric union
    #set_1 - set_2 difference
    return set_1 ^ set_2 

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))