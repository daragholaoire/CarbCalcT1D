class Item:
    def __init__(self, ingredient, carbs, meassurement): #maybe just leave at self
        self.ingredient = ingredient
        self.carbs = int(carbs)
        self.meassurement = int(meassurement)
        self.total = int(carbs) * (int(meassurement)/100)
        


def main():
    print ("Hello. Welcome to the recipe book for Type 1 Diabetics! \nYou can use this programme to caluclate the total carbs in recipes and how much insulin you should take for a portion."  )
    carbs_to_insulin = input("What is your carbs to insulin ratio? \n(i.e. How many grams of carbs per 1 unit of insulin you take.)" )



    ingredientList = []
    i=0

    while i == 0 or input("Do you have another product? Y/n").lower()[0] == "y":
        i+=1
        recipeDict = {
            "item" : input("What is the next item?"),
            "carbs per 100g" : input("How many carbs per 100g?"),
            "meassurement" : input("How many grams of this item are you using?")
        }

        # validate input

        print (recipeDict)
        # create item from input
        newItem = Item(recipeDict.get("item"), recipeDict.get("carbs per 100g"), recipeDict.get("meassurement"))

        # add item to list /// consider case where item may already exist

        ingredientList.append(newItem)

        # print(ingredientList)
    sum = 0
    for ingredient in ingredientList:
        sum += ingredient.total

    print(f"Total carbs in meal: {sum}")

    insulin_required = float(sum) / float(carbs_to_insulin)
    print(f"You must take {insulin_required}g of insulin. \nBon Apetite!")
        

main()