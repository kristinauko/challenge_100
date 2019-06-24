"""
You are given a list dishes, where each element consists of a list of strings 
beginning with the name of the dish, followed by all the ingredients used in 
preparing it. You want to group the dishes by ingredients, so that for each 
ingredient you'll be able to find all the dishes that contain it (if there are 
at least 2 such dishes).

Return an array where each element is a list beginning with the ingredient 
name, followed by the names of all the dishes that contain this ingredient. 
The dishes inside each list should be sorted lexicographically, and the result 
array should be sorted lexicographically by the names of the ingredients.
"""


def groupingDishes(dishes):
    """Take a list of dishes and return a list of ingredients, followed by dishes"""
    
    ingredients = {}
    
    for item in dishes:
        
        for i in range(1, len(item)):

            if item[i] not in ingredients.keys():
                ingredients[item[i]] = []
                
            dish = ingredients[item[i]]
            dish.append(item[0])
            ingredients[item[i]] = sorted(dish)
        

    final_list = []

    for key, value in ingredients.items():

        if len(value) >= 2:
            value.insert(0, key)
            final_list.append(value)

    final_list.sort()

    return final_list
 

print("*** TEST 1 ***")           

print(groupingDishes([["Salad","Tomato","Cucumber","Salad","Sauce"], 
 ["Pizza","Tomato","Sausage","Sauce","Dough"], 
 ["Quesadilla","Chicken","Cheese","Sauce"], 
 ["Sandwich","Salad","Bread","Tomato","Cheese"]]))

# [["Cheese","Quesadilla","Sandwich"], 
#  ["Salad","Salad","Sandwich"], 
#  ["Sauce","Pizza","Quesadilla","Salad"], 
#  ["Tomato","Pizza","Salad","Sandwich"]]

print("*** TEST 2 ***") 

print(groupingDishes([["Pasta","Tomato Sauce","Onions","Garlic"], 
 ["Chicken Curry","Chicken","Curry Sauce"], 
 ["Fried Rice","Rice","Onions","Nuts"], 
 ["Salad","Spinach","Nuts"], 
 ["Sandwich","Cheese","Bread"], 
 ["Quesadilla","Chicken","Cheese"]]))

# [["Cheese","Quesadilla","Sandwich"], 
#  ["Chicken","Chicken Curry","Quesadilla"], 
#  ["Nuts","Fried Rice","Salad"], 
#  ["Onions","Fried Rice","Pasta"]]
