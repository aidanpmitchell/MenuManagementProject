from functions import *
import os

spicy_scale_map = {1: "Not spicy", 2: "Low key spicy", 3: "Hot", 4: "Diabolical"}

# making sure print_main_menu doesn't return anything
the_menu = {"1": "Option 1", "2": "Option 2", "3": "Option 3"}
assert print_main_menu(the_menu) is None

# making sure print_restaurant_menu doesn't return anything
assert print_restaurant_menu([], spicy_scale_map) is None

# is_num
assert not is_num(56)
assert is_num('56')
assert is_num('3.0')

#  is_valid_name
assert not is_valid_name("a")
assert not is_valid_name("bo")
assert not is_valid_name(42)
assert not is_valid_name(["soup"])
assert is_valid_name("soup")

# is_valid_spicy_level
assert is_valid_spicy_level("1", spicy_scale_map)
assert not is_valid_spicy_level(1, spicy_scale_map)
assert not is_valid_spicy_level("one", spicy_scale_map)

# is_valid_is_vegetarian
assert is_valid_is_vegetarian("yes")
assert is_valid_is_vegetarian("no")
assert not is_valid_is_vegetarian("maybe")


# is_valid_price
assert is_valid_price("5.9")
assert is_valid_price("10.15")
assert not is_valid_price("five")

# is_valid_calories
assert is_valid_calories("100")
assert not is_valid_calories("50.0")
assert not is_valid_calories("abc")
assert not is_valid_calories(100)

# get_new_menu_dish
get_new_menu_dish_1 = {"name": "burrito", "calories": 500, "price": 12.9,
                       "is_vegetarian": "yes", "spicy_level": 2}
assert get_new_menu_dish(["burrito", "500", "12.90", "yes", "2"], spicy_scale_map) == get_new_menu_dish_1
assert get_new_menu_dish(["a", "500", "12.90", "yes", "2"], spicy_scale_map) == ('name', 'a')
assert get_new_menu_dish(["burrito", "five", "12.90", "yes", "2"], spicy_scale_map) == ('calories', 'five')

# making sure print_dish doesn't return anything
assert print_dish({"name": "burrito", "calories": 500, "price": 12.90, "is_vegetarian": "yes", "spicy_level": 2},
                  spicy_scale_map) is None

# is_valid_index
assert is_valid_index([1, 2, 3], "2")
assert not is_valid_index([1, 2, 3], "4")
assert not is_valid_index([1, 2, 3], "2", 3)

# update_menu_dish
assert update_menu_dish([{'calories': 1}], 1, spicy_scale_map, 'calories', 200, start_idx=0) == -1
assert update_menu_dish([], '1', spicy_scale_map, 'name', 'test1', start_idx=0) == 0
assert update_menu_dish([{'name': 'test'}], '0', spicy_scale_map, 'name', 'test1', start_idx=0) == {'name': 'test1'}

# delete_dish
assert delete_dish([], '2') == 0
assert delete_dish(['a'], '1') == -1
assert delete_dish(['a', 'b', 'c'], '1') == 'b'

# save_menu_to_csv
assert save_menu_to_csv([{'a': 1}], 'filename') == -1
assert save_menu_to_csv([], 'menu.docx') == -1
assert save_menu_to_csv([], 'test1.csv') is None
os.remove('test1.csv')

# load_menu_from_csv
assert load_menu_from_csv('filename.txt', [], spicy_scale_map) == -1
assert load_menu_from_csv('filename.docx', [], spicy_scale_map) == -1
assert load_menu_from_csv('does_not_exist.csv', [], spicy_scale_map) is None

# get_restaurant_expense_rating
menu1 = [{'dish': 'Pizza', 'price': 8.99}, {'dish': 'Burger', 'price': 9.99}, {'dish': 'Salad', 'price': 6.99}]
assert get_restaurant_expense_rating(menu1) == 8.656666666666666
menu2 = [{'dish': 'Spaghetti', 'price': 15.99}, {'dish': 'Steak', 'price': 25.99}, {'dish': 'Wine', 'price': 18.99}]
assert get_restaurant_expense_rating(menu2) == 20.323333333333334
menu3 = [{'dish': 'Noodles', 'price': 12.99}, {'dish': 'Fries', 'price': 2.99}, {'dish': 'Bread', 'price': 4.99}]
assert get_restaurant_expense_rating(menu3) == 6.989999999999999
