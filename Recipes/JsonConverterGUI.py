import json
import tkinter

#overall layout setup
window = tkinter.Tk(className='Recipe Converter')
window.geometry('1920x1080')
left = tkinter.Frame(window, width=640, height=1080)
mid = tkinter.Frame(window, width=640, height=1080)
right = tkinter.Frame(window, width=640, height=1080)
left.grid(column=1,row=0,ipadx=100)
mid.grid(column=2,row=0)
right.grid(column=3,row=0,ipadx=100)



allIngredients = []
ingredientY = 3
def printInput():
    #cleans up list of ingredients and splits each ingredient into its separate parts
    global allIngredients
    cleanIngredients = []
    for i in range(len(allIngredients)):
        ingredientParts = allIngredients[i].get(1.0, "end-1c").split(", ")
        ing = []
        ing.append(['"Name":"'+ingredientParts[0]+'",\n','"Time":"'+ingredientParts[1]+'",\n','"Considerations":"'+ingredientParts[2]+'",\n'])
    #gets the info from all the different text boxes
    RecipeName = nameInput.get(1.0, "end-1c")
    RecipeConsiderations = considerationInput.get(1.0, "end-1c")
    RecipeInstructions = instructionsInput.get(1.0, "end-1c")
    RecipeNotes = notesInput.get(1.0, "end-1c")
    RecipeNutrition = nutritionInput.get(1.0, "end-1c").split(", ")

    Recipe = "{\n"
    Recipe += (' "Name":"{RecipeName}",\n')
    Recipe += (' "Time":"{RecipeTime}",\n')
    Recipe += (' "Considerations":"{RecipeConsiderations}",\n')
    Recipe += ' "Tags": [\n'
    for i in range(len(allTags)):
        Recipe += '"'+allTags[i].cget("text")+'":'
        if (allTags[i].get()==1):
            Recipe+= '"True"\n'
        else:
            Recipe+= '"False"\n'
    Recipe += ' ],\n'
    Recipe += ' "Ingredients": [\n'
    for i in range(len(cleanIngredients)):
        Recipe = " {\n"
        Recipe += (cleanIngredients[i][0])
        Recipe += (cleanIngredients[i][1])
        Recipe += (cleanIngredients[i][2])
        Recipe+=' },\n'
    Recipe+= ' ],\n'
    Recipe += (' "Instructions":"{RecipeInstructions}",\n')
    Recipe += (' "Notes":"{RecipeNotes}",\n')
    Recipe += (' "Nutrition": [\n')
    Recipe = " {\n"
    for i in range(len(RecipeNutrition)):
        Recipe += ('  "Nutrient{i}":"{RecipeNutrition[i]}",\n')
    Recipe+=' },\n'
    Recipe+=' ],\n'
    Recipe+='},\n'
    
    print(Recipe)



#function to add an ingredient row
def addIngredient():
    global ingredientY
    
    ingredient = tkinter.Text(right, 
                       height=1,
                       width=50)
    ingredient.pack()
    ingredientY = ingredientY+1
    allIngredients.append(ingredient)

warningLabel = tkinter.Label(mid, text="Warning: if you line break, just delete it. It will cause problems later", )
warningLabel.pack(side="top", ipady=100)

#tags for recipes
tagNames = ["Cakes", "Cookies", "Pies", "Squares", "Desserts", "Muffins", "Breads", "Biscuits", "Frosting", "Soups", 
"Salads", "Pasta", "Casseroles", "Vegetables", "Meat", "Dressings", "Sauces", "Dips", "Drinks"]
allTags = []
for i in range(len(tagNames)):
    tag = tkinter.Checkbutton(mid, text=tagNames[i], onvalue=1, offvalue=0)
    tag.pack()
    allTags.append(tag)



#get the name of the recipe
nameLabel = tkinter.Label(left, text="Recipe Name (no punctuation or special characters please):")
nameLabel.pack()
nameInput = tkinter.Text(left,
                   height = 1,
                   width = 30)
nameInput.pack()

#get the prep time of the recipe
timeLabel = tkinter.Label(left, text="Time to prepare recipe:")
timeLabel.pack()
timeInput = tkinter.Text(left,
                   height = 1,
                   width = 30)
timeInput.pack()

#get the considerations for the recipe
considerationLabel = tkinter.Label(left, text="Considerations (chill time, # fed, etc.):")
considerationLabel.pack()
considerationInput = tkinter.Text(left,
                   height = 1,
                   width = 30)
considerationInput.pack()

#get the instructions for the recipe
instructionsLabel = tkinter.Label(left, text="Instructions for recipe:")
instructionsLabel.pack()
instructionsInput = tkinter.Text(left,
                   height = 4,
                   width = 40)
instructionsInput.pack()

#get the notes for the recipe
notesLabel = tkinter.Label(left, text="Notes (substitutions, tips, etc.):")
notesLabel.pack()
notesInput = tkinter.Text(left,
                   height = 2,
                   width = 40)
notesInput.pack()

#get the instructions for the recipe
nutritionLabel = tkinter.Label(left, text="enter nutrition name and amount, separated by commas \n(e.g. serving size: 1 slice, calories: 30cal):")
nutritionLabel.pack()
nutritionInput = tkinter.Text(left,
                   height = 3,
                   width = 40)
nutritionInput.pack()

ingredientNameLabel = tkinter.Label(right, text="Name of Ingredient, Amount (and units) of ingredient, Details about ingredient\n(commas separating these, write 'none' if no details):")
ingredientNameLabel.pack(side="top")
#button to add ingredient
ingredientButton = tkinter.Button(right,
                                  text = "Add Ingredient",
                                  command = addIngredient)
ingredientButton.pack()



# Button Creation
printButton = tkinter.Button(mid,
                        text = "Submit", 
                        command = printInput)

printButton.pack(side="bottom",pady=30)













window.mainloop()

