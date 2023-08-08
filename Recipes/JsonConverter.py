# JSON Converter: A simple program that anyone can run and enter information from a recipe
# in order to get a json file that can be used with the recipe website.
import json

#gets recipe info from user
print("JSON converter: enter requested information for your recipe, pressing ENTER will submit whatever you have.")
RecipeName = input('enter name of recipe (just letters please, no special characters):\n')
RecipeTime = input('enter time to prepare recipe:\n')
RecipeConsiderations = input('enter considerations for recipe (chill time, # fed, etc.):\n')

#gets recipe ingredients from user one at a time. broken by entering 'end'
print('Recipe Ingredients, enter "END" to end.\n')
RecipeIngredients = []
nextIngredient = True
while nextIngredient== True:
    ingredientName = input('enter name of ingredient: \n')
    if (ingredientName.upper() == 'END'):
        nextIngredient=False
        break        
    ingredientAmount = input('enter amount (and units) of ingredient:\n')
    if (ingredientAmount.upper() == 'END'):
        nextIngredient=False
        break  
    ingredientDetails = input('any extra details about the ingredient, just press enter if there are none:\n')
    if (ingredientDetails.upper() == 'END'):
        nextIngredient=False
        break  
    ingredient = {'Name':ingredientName,'Amount':ingredientName,'Details':ingredientDetails,} 
    RecipeIngredients.append(ingredient)

RecipeInstructions = input('enter instructions for recipe, press ENTER to submit, making a new line will submit what you have:\n')
RecipeNotes = input('enter any notes (substitutions, tips, etc.):\n')
RecipeNutrition = []

#gets recipe nutrition from user one at a time. broken by entering 'end'
print('Recipe Nutrition, enter "END" to end.\n')
while True:
    nutritionVal = input('enter nutrition name and amount (e.g. calories: 30cal):\n')
    if nutritionVal.upper == 'END':
        break
    RecipeNutrition.append(nutritionVal)

#this block formats all of the previous info into a style that can be converted into a json file
Recipe = "{\n"
Recipe += (' "Name":"{RecipeName}",\n')
Recipe += (' "Time":"{RecipeTime}",\n')
Recipe += (' "Considerations":"{RecipeConsiderations}",\n')
Recipe += ' "Ingredients": [\n'
for i in range(len(RecipeIngredients)):
    Recipe = " {\n"
    Recipe += ('  "Name":"'+RecipeIngredients[i]["Name"]+'",\n')
    Recipe += ('  "Amount":"'+RecipeIngredients[i]["Amount"]+'",\n')
    Recipe += ('  "Details":"'+RecipeIngredients[i]["Details"]+'",\n')
    Recipe+=' },\n'
Recipe+=' ],\n'
Recipe += (' "Instructions":"{RecipeInstructions}",\n')
Recipe += (' "Notes":"{RecipeNotes}",\n')
Recipe += (' "Nutrition": [\n')
Recipe = " {\n"
for i in range(len(RecipeNutrition)):
    Recipe += ('  "Nutrient{i}":"{RecipeNutrition[i]}",\n')
Recipe+=' },\n'
Recipe+=' ],\n'
Recipe+='},\n'

#outputs as both a txt and a json file so it's easier to see what went wrong
fileName = RecipeName.replace(" ", "_") + '.txt'
jsonName = fileName.split('.', 1)[0]+'.json'
with open(fileName, 'w') as f:
    f.write(Recipe)
with open(fileName, encoding="latin-1") as inputFile:
    contents = inputFile.read()
    if (idx := contents.find('{')) >=0:
        d = json.loads(contents[idx:])
        with open(jsonName, 'w') as jout:
            json.dump(d,jout,indent=4)