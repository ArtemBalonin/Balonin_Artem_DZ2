my_list = [57.8, 46.51, 97, 25, 33.1, 35.90, 87.10, 100.23, 54.40, 246.15]
store_id = id(my_list)
print(my_list)
print(f"{'a':-^100}")
end_word:str = ", "
for i, num in enumerate(my_list):
    fix_price = str(f"{float(num):.2f}").split(".")
    if i == len(my_list) -1:
        end_word = "\n"
    print(f"{fix_price[0]} руб {fix_price[1]} коп", end=end_word)

print(f"{'b':-^100}")
print(f"id before sort {store_id}")
my_list.sort()
print(my_list)
print(f"id after sort {id(my_list)}")
if store_id == id(my_list):
    print("In place")
else:
    print("Diff obj")
print(f"{'c':-^100}")
copy_of_list = my_list.copy()
copy_of_list.sort(reverse=True)
print(copy_of_list)
print(store_id)
print(id(copy_of_list))
if store_id == id(copy_of_list):
    print("In place")
else:
    print("Diff obj")
print(f"{'d':-^100}")
print("five biger prices", my_list[-6:-1])
