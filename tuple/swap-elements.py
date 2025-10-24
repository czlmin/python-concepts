# def swap_elements(tpl):
#     n = len(tpl)
#     lst = list(tpl)
#     new_lst = []
#     new_lst.append(lst[-1])
#     new_lst += lst[1:n-1]
#     new_lst.append(lst[0])
#     new_tpl = tuple(new_lst)
#     return new_tpl

def swap_elements(tpl):
    if len(tpl) < 2:
        return tpl
    else:
        return (tpl[-1], ) + tpl[1:-1] + (tpl[0], )

# tpl1 = (10, 20, 30)
# print(swap_elements(tpl1))

tpl = (10, 20, 30, 40, 50, 60, 70)
print((tpl[-1], ), tpl[1:-1])
print(swap_elements(tpl))
