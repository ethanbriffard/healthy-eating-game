from cProfile import label

#from graphics import *
import os

from screeninfo import get_monitors
import tkinter as tk

from tkinter import PhotoImage
from tkinter import font
import tkinter.messagebox

width_screen = get_monitors()[0].width
height_screen = get_monitors()[0].height

#var pour drag
recommandations = {
    "4-6 years old": {
        "fruits_vegetables": {"min": 5, "max": None, "unit": "portion/day"},
        "legumes": {"min": 1, "max": None, "unit": "portion/day"},
        "nuts": {"min": 1, "max": None, "unit": "portion/day"},
        "starchy_foods": {"min": 1, "max": None, "unit": "portion/day"},
        "fish_eggs_meat": {"min": 1, "max": 1, "unit": "portion/day"},
        "red_meat": {"min": 0, "max": 1, "unit": "g/day"},
        "dairy": {"min": 3, "max": 3, "unit": "portion/day"},
        "fats": {"min": 1, "max": 1, "unit": "portion/day"},
        "sugary_drinks": {"min": 0, "max": 0.5, "unit": "glass/day"},
        "alcohol": {"min": 0, "max": 0, "unit": "glass/day"}
    },

    "7-11 years old": {
        "fruits_vegetables": {"min": 5, "max": None, "unit": "portion/day"},
        "legumes": {"min": 1, "max": None, "unit": "portion/day"},
        "nuts": {"min": 1, "max": None, "unit": "portion/day"},
        "starchy_foods": {"min": 1, "max": None, "unit": "portion/day"},
        "fish_eggs_meat": {"min": 1, "max": 1, "unit": "portion/day"},
        "red_meat": {"min": 0, "max": 1, "unit": "g/day"},
        "dairy": {"min": 3, "max": 3, "unit": "portion/day"},
        "fats": {"min": 1, "max": 1, "unit": "portion/day"},
        "sugary_drinks": {"min": 0, "max": 1, "unit": "glass/day"},
        "alcohol": {"min": 0, "max": 0, "unit": "glass/day"}
    },

    "12-17 years old": {
        "fruits_vegetables": {"min": 5, "max": None, "unit": "portion/day"},
        "legumes": {"min": 1, "max": None, "unit": "portion/day"},
        "nuts": {"min": 1, "max": None, "unit": "portion/day"},
        "starchy_foods": {"min": 1, "max": None, "unit": "portion/day"},
        "fish_eggs_meat": {"min": 1, "max": 1, "unit": "portion/day"},
        "red_meat": {"min": 0, "max": 1, "unit": "g/week"},
        "dairy": {"min": 3, "max": 3, "unit": "portion/day"},
        "fats": {"min": 1, "max": 1, "unit": "portion/day"},
        "sugary_drinks": {"min": 0, "max": 1, "unit": "glass/day"},
        "alcohol": {"min": 0, "max": 0, "unit": "glass/day"}
    },

    "adults": {
        "fruits_vegetables": {"min": 5, "max": None, "unit": "portion/day"},
        "legumes": {"min": 1, "max": None, "unit": "portion/day"},
        "nuts": {"min": 1, "max": None, "unit": "portion/day"},
        "starchy_foods": {"min": 1, "max": None, "unit": "portion/day"},
        "fish_eggs_meat": {"min": 1, "max": 1, "unit": "portion/day"},
        "red_meat": {"min": 0, "max": 1, "unit": "g/week"},
        "dairy": {"min": 2, "max": 2, "unit": "portion/day"},
        "fats": {"min": 1, "max": 1, "unit": "portion/day"},
        "sugary_drinks": {"min": 0, "max": 1, "unit": "glass/day"},
        "alcohol": {"min": 0, "max": 1, "unit": "glass/day"}
    },

    "75+ years old": {
        "fruits_vegetables": {"min": 5, "max": None, "unit": "portion/day"},
        "legumes": {"min": 1, "max": None, "unit": "portion/day"},
        "nuts": {"min": 1, "max": None, "unit": "portion/day"},
        "starchy_foods": {"min": 1, "max": None, "unit": "portion/day"},
        "fish_eggs_meat": {"min": 1, "max": 1, "unit": "portion/day"},
        "red_meat": {"min": 0, "max": 1, "unit": "g/week"},
        "dairy": {"min": 3, "max": 3, "unit": "portion/day"},
        "fats": {"min": 1, "max": 1, "unit": "portion/day"},
        "sugary_drinks": {"min": 0, "max": 1, "unit": "glass/day"},
        "alcohol": {"min": 0, "max": 0.5, "unit": "glass/day"}
    }
}
recommendations_final = {
    "4-6 years old": {
        "fruits_vegetables": "Help children get used to eating fruits and vegetables at every meal. Gradually increase intake toward at least 5 portions per day.",
        "legumes": "At least 2 times per week (lentils, beans, chickpeas…).",
        "nuts": "Before age 6, do not give whole nuts because of choking risks. Serve them ground or mixed into preparations several times a week.",
        "starchy_foods": "Pasta, rice, potatoes, and wholegrain or semi-wholegrain bread every day according to appetite. Prefer wholegrain or semi-wholegrain versions.",
        "fish_eggs_meat": "1 egg or 50 g of fish, meat, or poultry per meal is enough. Fish twice a week including one oily fish.",
        "red_meat": "Limit red meat consumption. Processed meat should remain exceptional.",
        "dairy": "3 dairy products per day (milk, yogurt, cheese).",
        "fats": "Small quantities every day. Prefer rapeseed, walnut, and olive oils.",
        "sugary_drinks": "Drink water freely. Limit sugary drinks to less than half a glass per day.",
        "alcohol": "Not allowed."
    },

    "7-11 years old": {
        "fruits_vegetables": "Fruits and vegetables at every meal to progressively reach 5 portions per day.",
        "legumes": "At least 2 times per week.",
        "nuts": "Offer unsalted nuts several times a week in small handfuls.",
        "starchy_foods": "Starchy foods every day, preferably wholegrain or semi-wholegrain versions.",
        "fish_eggs_meat": "Gradually increase portions up to about 100 g of meat or fish around age 11 (or 2 eggs). Fish twice a week including one oily fish.",
        "red_meat": "Limit processed meat; only occasional white ham or poultry ham is recommended.",
        "dairy": "3 dairy products per day.",
        "fats": "Small quantities every day. Prefer rapeseed, walnut, and olive oils.",
        "sugary_drinks": "Limit sodas and sugary drinks to less than half a glass per day.",
        "alcohol": "Not allowed."
    },

    "12-17 years old": {
        "fruits_vegetables": "At least 5 fruits and vegetables per day.",
        "legumes": "At least 2 times per week.",
        "nuts": "One small handful of unsalted nuts per day.",
        "starchy_foods": "At least one serving of wholegrain or semi-wholegrain starchy foods per day.",
        "fish_eggs_meat": "Fish twice a week including one oily fish. Portions similar to adults.",
        "red_meat": "Limit red meat to 500 g per week and processed meat to 150 g maximum per week.",
        "dairy": "3 dairy products per day.",
        "fats": "Small quantities every day. Prefer rapeseed, walnut, and olive oils.",
        "sugary_drinks": "Limit sugary drinks to a maximum of one glass per day.",
        "alcohol": "Not allowed."
    },

    "adults": {
        "fruits_vegetables": "At least 5 fruits and vegetables per day.",
        "legumes": "Eat legumes at least twice a week because they are naturally rich in fiber.",
        "nuts": "Eat one small handful of unsalted and unsweetened nuts every day.",
        "starchy_foods": "Wholegrain bread or cereals, pasta, semolina, and rice: at least once a day.",
        "fish_eggs_meat": "Fish twice a week including one oily fish.",
        "red_meat": "Maximum 500 g of red meat per week, about 3 or 4 steaks. \nAlternate between meat, poultry, fish, eggs, and legumes.",
        "dairy": "2 dairy products per day.",
        "fats": "Added fats can be eaten every day in small amounts. \nPrefer rapeseed, walnut, and olive oils.",
        "sugary_drinks": "Limit sugary drinks, fatty, sugary, salty, and ultra-processed foods.",
        "alcohol": "Maximum 2 glasses per day and not every day."
    },

    "75+ years old": {
        "fruits_vegetables": "At least 5 fruits and vegetables per day.",
        "legumes": "At least 2 times per week.",
        "nuts": "One small handful of unsalted nuts per day.",
        "starchy_foods": "Eat wholegrain or semi-wholegrain starchy foods every day.",
        "fish_eggs_meat": "Fish twice a week including one oily fish. Maintain sufficient protein intake.",
        "red_meat": "Limit red meat to 500 g per week.",
        "dairy": "3 dairy products per day to help preserve bone mass.",
        "fats": "Small quantities every day, preferably oils rich in omega-3.",
        "sugary_drinks": "Limit sugary drinks and ultra-processed foods.",
        "alcohol": "Limit alcohol consumption."
    }
}

food_categories = {
    "fruits_vegetables": ["carrot", "orange", "banana", "kiwi", "apple", "onion", "leek", "zucchini"],
    "legumes": ["beans", "chickpeas"],
    "nuts": ["almonds", "walnuts", "pistachios"],
    "starchy_foods": ["pasta", "bread", "potatoes"],
    "fish_eggs_meat": ["fish", "eggs"],
    "red_meat": ["salami", "chicken", "ham"],
    "dairy": ["cheese", "milk", "yogurt"],
    "fats": ["oil", "butter"],
    "sugary_drinks": ["juice", "fanta"],
    "alcohol": ["vodka", "beer"]
}
food_categories_titles = {
    "fruits_vegetables": "Fruits&Vegetables",
    "legumes": "Legumes",
    "nuts": "Nuts",
    "starchy_foods": "Starchy Foods",
    "fish_eggs_meat": "Proteins",
    "red_meat": "Red meat",
    "dairy": "Dairy",
    "fats": "Fats",
    "sugary_drinks": "Sugary Drinks",
    "alcohol": "Alcohol"
}


class Tube:
    def __init__(self, category, x_coordinate, y_coordinate):
        self.category = category
        self.img = os.path.join("image", f"{self.category}.png")
        self.width = None
        self.height = None
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.fulfillment = 0
        self.canvas = None
        self.canvas_full = None
        self.title = food_categories_titles[category]


class Food:
    category_counts = {
        "fruits_vegetables": 0,
        "legumes": 0,
        "nuts": 0,
        "starchy_foods": 0,
        "fish_eggs_meat": 0,
        "red_meat": 0,
        "dairy": 0,
        "fats": 0,
        "sugary_drinks": 0,
        "alcohol": 0
    }

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.img = os.path.join("image", f"{self.name}.png")
        self.number = 0
        self.prev_in_plate = False
        self.in_plate = False


class Recommendation:
    def __init__(self, age, fruits_vegetables, legumes, nuts, starchy_foods, fish_eggs_meat, dairy, fats, alcohol,
                 sugary_drinks, red_meat):
        self.age = age
        self.fruits_vegetables = fruits_vegetables
        self.legumes = legumes
        self.nuts = nuts
        self.starchy_foods = starchy_foods
        self.fish_eggs_meat = fish_eggs_meat
        self.dairy = dairy
        self.fats = fats
        self.sugary_drinks = sugary_drinks
        self.alcohol = alcohol
        self.red_meat = red_meat


class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry(str(width_screen) + "x" + str(height_screen))
        self.window.title("How to eat well?")

        self.window.resizable(width=False, height=False)
        self.canvas_fond = tk.Canvas(self.window, width=width_screen, height=height_screen, bg="light grey")
        self.canvas_fond.place(relwidth=1, relheight=1)
        self.explanation = "Prepare your meals for the day and turn every tubes into green!"
        self.instructions = tk.Label(
            self.canvas_fond,
            text=self.explanation,
            font=("Helvetica", 20, "bold"),
            fg="red",  # Couleur du texte
            bg="light grey"  # Couleur de fond (optionnel)
        )
        self.instructions.pack()

        self.options_age = []

        # Create the list of options
        for age in recommandations:
            self.options_age.append(age)

        # Variable to keep track of the option
        # selected in OptionMenu
        self.value_OptionMenu = tk.StringVar(self.window)
        self.value_OptionMenu.set(self.options_age[3])
        self.question_menu = tk.OptionMenu(self.window,
                                           self.value_OptionMenu,
                                           *self.options_age,
                                           command=self.select_age, )

        self.question_menu.config(width=18)  # Largeur en nombre de caractères
        self.question_menu.config(font=('Arial', 16))
        self.question_menu.place(x=width_screen - 250, y=height_screen - 200)

        self.submit_button = tk.Button(self.window, text='Submit', command=self.show_recommendations)
        self.submit_button.config(width=18)  # Largeur en nombre de caractères
        self.submit_button.config(font=('Arial', 16))

        self.submit_button.place(x=width_screen - 250, y=height_screen - 250)

        self.food_images = []

        self.food_map = {}  #contient img_id relié à la classe food

        self.id_images = []

        self.decoration_images = []
        try:
            self.knife_image = PhotoImage(file="image/knife.png")
            self.spoon_image = PhotoImage(file="image/spoon.png")
            self.forks_image = PhotoImage(file="image/forks.png")
            self.plate_img = PhotoImage(file="image/plate.png")
        except:
            self.knife_image = None
            self.plate_img = PhotoImage(width=300, height=300)
            self.plate_img.put(("blue",), to=(0, 0, 300, 300))

            print("plate_img unreachable")

        try:

            self.empty_tube = PhotoImage(file="image/empty_tube.png")

            self.red_tube = PhotoImage(file="image/red_tube.png")
            self.green_tube = PhotoImage(file="image/green_tube.png")
            self.blue_tube = PhotoImage(file="image/blue_tube.png")

            self.tube_width = self.empty_tube.width()
            self.tube_height = self.empty_tube.height()


        except:

            self.tube_width = 100
            self.tube_height = 400
            self.empty_tube = PhotoImage(width=self.tube_width, height=self.tube_height)
            self.empty_tube.put(("grey",), to=(0, 0, self.tube_width // 2, self.tube_height // 2))

            self.red_tube = PhotoImage(width=self.tube_width, height=self.tube_height)
            self.red_tube.put(("red",), to=(0, 0, self.tube_width // 2, self.tube_height // 2))

            self.green_tube = PhotoImage(width=self.tube_width, height=self.tube_height)
            self.green_tube.put(("green",), to=(0, 0, self.tube_width // 2, self.tube_height // 2))

            self.blue_tube = PhotoImage(width=self.tube_width, height=self.tube_height)
            self.blue_tube.put(("blue",), to=(0, 0, self.tube_width // 2, self.tube_height // 2))

            print("Tubes unreachable")

        self.plates_coordinates = []
        self.meals_names = ["Breakfast", "Lunch", "Snack", "Dinner"]
        self.box_meals_names = []



        self.box_tool = [self.knife_image, self.spoon_image, self.forks_image]

        for i in range(4):
            self.show_decorations(self.plate_img, (i + 0.5) * (self.plate_img.width() + 100),
                                  height_screen - self.plate_img.height())
            self.show_decorations(self.box_tool[-3 + i], (i + 0.75) * (self.plate_img.width() + 100),
                                  height_screen - self.plate_img.height())
            self.show_decorations(self.box_tool[-1 + i], (i + 0.40) * (self.plate_img.width() + 100),
                                  height_screen - self.plate_img.height() - 50)
            self.plates_coordinates.append([(i + 0.5) * (self.plate_img.width() + 100), height_screen - self.plate_img.height()])
            meal_name = tk.Label(self.canvas_fond,
                           text=self.meals_names[i],
                           font=("Helvetica", 18, "bold"),
                           fg="Blue",  # Couleur du texte
                           bg="light grey"
                           )
            self.box_meals_names.append(meal_name)
            self.box_meals_names[-1].place(x=self.plates_coordinates[i][0], y=self.plates_coordinates[i][1] +90, anchor="center")



        self.age = "adults"

        self.food_boxes = []

        self.tube_boxes = []

        self.line = 0
        self.column = 0
        self.num_of_column_tubes = 0
        self.num_of_rows_tubes = 0

        for category, name in food_categories.items():

            self.new_tube = Tube(category, width_screen - (self.tube_width - 20) * (self.num_of_column_tubes + 1),
                                 25 + (self.tube_height + 40) * self.num_of_rows_tubes)
            self.num_of_column_tubes += 1
            if self.num_of_column_tubes > 4:
                self.num_of_column_tubes = 0
                self.num_of_rows_tubes += 1
            self.tube_boxes.append(self.new_tube)

            self.show_tube(self.new_tube)
            self.new_fulfillment(self.new_tube)

            for i in range(len(name)):
                self.food_boxes.append(Food(name[i], category))
                self.show_food(self.food_boxes[-1], 50 + self.column * 150, 100 + self.line * 150)
                self.column += 1
                if self.column > 5:
                    self.column = 0
                    self.line = self.line + 1

    def select_age(self, *args):
        self.age = self.value_OptionMenu.get()
        for tube in self.tube_boxes:
            self.new_fulfillment(tube)
        print(self.age)

    def show_recommendations(self, *args):
        message = "Let's see your results: \n \n"
        for tube in self.tube_boxes:
            max_val = recommandations[self.age][tube.category]["max"]
            min_val = recommandations[self.age][tube.category]["min"]
            if max_val is None:
                max_val = 10
            if min_val is None:
                min_val = 0

            message += food_categories_titles[tube.category] + " :  \n@"

            if min_val <= int(Food.category_counts[tube.category]) <= max_val:
                message += "Well done your quantity is perfect!"

            else:
                message += recommendations_final[self.age][tube.category]

            message += " \n\n"

        self.popup = tk.Toplevel(self.window)
        self.popup.title("Results")
        self.popup.geometry("1600x1100")
        self.popup.resizable(width=False, height=False)
        self.popup.config(bg="light green")

        self.popup_fond = tk.Canvas(self.popup, width=1100, height=1100, bg="light green")
        self.popup_fond.pack(fill="both", expand=True)

        #tk.messagebox.showinfo("Results", message)

        label_knife  = tk.Label(self.popup_fond, image=self.knife_image, bg="light green")
        label_knife2 = tk.Label(self.popup_fond, image=self.knife_image, bg="light green")
        label_knife.pack(side="left", padx=10)
        label_knife2.pack(side="right", padx=10)

        self.popup_message = tk.Label(
            self.popup_fond,
            text=message,
            fg="grey",
            font=("Helvetica", 20, "bold"),
            bg="light green",
            #wraplength=750,
            justify=tk.LEFT,
        )
        self.popup_message.pack(side="right", fill="both", expand=True, padx=10)

        """
        self.canvas_knife= tk.Canvas(self.popup_fond, width=self.knife_image.width(), height=self.knife_image.height(), background="light green",
                    highlightthickness=0)
        self.canvas_knife_skin.create_image(self.knife_image.width()/2, self.knife_image.height()/2, image = self.knife_image)

        self.canvas_knife.pack(ipadx=6, ipady=6)

        self.popup_fond.create_image(100, 100, image=self.knife_image)
        """

    def new_fulfillment(self, tube):

        max_val = recommandations[self.age][tube.category]["max"]
        min_val = recommandations[self.age][tube.category]["min"]
        born_min = 0
        born_max = 8

        if max_val is not None:
            born_max = max_val
        if min_val is not None:
            born_min = min_val

        if Food.category_counts[tube.category] > born_max:
            tube.fulfillment = 0.85 - Food.category_counts[tube.category] / (2 + born_max )
            img = self.red_tube
        elif Food.category_counts[tube.category] < born_min:
            tube.fulfillment = 0.85 - Food.category_counts[tube.category] / (born_min + 2)
            img = self.blue_tube
        else:
            tube.fulfillment = 0.85 - Food.category_counts[tube.category] / (born_max + 1)
            img = self.green_tube



        if tube.fulfillment < 0:
            tube.fulfillment = 0.0
        elif tube.fulfillment == 1:
            tube.fulfillment = 0.85  #seulement pour un aspect graphique

        tube.canvas_full.itemconfig(tube.canvas_skin_full, image=img)
        tube.canvas.config(height=tube.height * tube.fulfillment, width=tube.width)

    def show_tube(self, tube):

        # fond = = os.path.join("image", f"{"tuberouge"}.png")
        #for tube in (fond, tube):
        #tube rempli
        tube.width = self.empty_tube.width()
        tube.height = self.empty_tube.height()

        tube.canvas_full = tk.Canvas(self.window, width=tube.width, height=tube.height, background="lightgrey",
                                     highlightthickness=0)

        tube.canvas_full.place(x=tube.x_coordinate, y=tube.y_coordinate)

        tube.canvas_skin_full = tube.canvas_full.create_image(tube.width / 2, tube.height / 2, image=self.red_tube)

        tube.canvas = tk.Canvas(self.window, width=tube.width, height=tube.height, background="light grey",
                                highlightthickness=0)
        tube.canvas.place(x=tube.x_coordinate, y=tube.y_coordinate)
        tube.canvas_skin = tube.canvas.create_image(tube.width / 2, tube.height / 2, image=self.empty_tube)

        # Créer le label avec texte centré, police personnalisée
        tube.title = tk.Label(
            self.window,
            text=tube.title,
            font=("Helvetica", 16, "bold"),
            fg="black",  # Couleur du texte
            bg="light grey"  # Couleur de fond (optionnel)
        )
        tube.title.pack(pady=15)  # Ajoute un peu d'espace vertical

        # Centrer le label dans la fenêtre
        tube.title.place(x=tube.x_coordinate + tube.width / 2, y=tube.y_coordinate + tube.height, anchor="center")

    def show_decorations(self, decoration, x_coordinate, y_coordinate):

        self.decoration_images.append(decoration)

        id_image = self.canvas_fond.create_image(x_coordinate, y_coordinate, image=self.decoration_images[-1])

        #self.canvas = tk.Canvas(self.window, width=decoration.width(), height=decoration.height(), bg=None)
        #self.canvas.place(x=x_coordinate, y=y_coordinate)

        #self.canvas_skin = self.canvas.create_image(decoration.width() / 2, decoration.width() / 2, image=decoration)

    def show_food(self, food, x_coordinate, y_coordinate):

        try:
            self.img = PhotoImage(file=food.img)
            width_img = self.img.width()
            height_img = self.img.height()

        except:
            width_img = 100
            height_img = 100
            # Image de secours si le chargement échoue
            self.img = PhotoImage(width=width_img, height=height_img)
            self.img.put(("red",), to=(0, 0, width_img // 2, height_img // 2))
            print(food.name + " unreachable")

        self.food_images.append(self.img)

        #self.canvas = tk.Canvas(self.window, width=width_img, height=height_img, bg=None)
        #self.canvas.food = food

        id_image = self.canvas_fond.create_image(x_coordinate, y_coordinate, image=self.food_images[-1])
        food.id_image = id_image
        self.food_map[id_image] = food

        #self.canvas.place(x=x_coordinate, y=y_coordinate)
        # self.canvas_skin = self.canvas.create_image(width_img / 2, height_img / 2, image=self.food_images[-1])

        #self.canvas_fond.bind("<Button-1>", self.drag_start)
        #self.canvas_fond.bind("<B1-Motion>", self.drag_motion)

        self.canvas_fond.tag_bind(id_image, "<Button-1>", self.drag_start)
        self.canvas_fond.tag_bind(id_image, "<B1-Motion>", self.drag_motion)

    def collision(self, id_image, x, y):
        food = self.food_map[id_image]
        #tube = widget.tube
        # print(x, y)
        width_plate = self.decoration_images[0].width()
        height_plate = self.decoration_images[0].height()
        print(f"{self.plates_coordinates[0][0]+width_plate}x{self.plates_coordinates[0][1]+height_plate}")

        for i in self.plates_coordinates:
            plate_x, plate_y = i

            if ((plate_x - width_plate / 2) < x < (plate_x + width_plate / 2) and
                    (plate_y - height_plate / 2) < y < (plate_y + height_plate / 2)):

                food.in_plate = True
                break

            else:
                food.in_plate = False

        if food.prev_in_plate != food.in_plate:
            if not food.prev_in_plate:
                Food.category_counts[food.category] += 1
            else:
                Food.category_counts[food.category] -= 1

            for tube in self.tube_boxes:
                self.new_fulfillment(tube)

            food.prev_in_plate = food.in_plate
            

    def drag_start(self, event):
        self.current_item = self.canvas_fond.find_closest(event.x, event.y)[0]
        self.startX = event.x
        self.startY = event.y

        #widget = event.widget
        #widget.startX = event.x
        #widget.startY = event.y

    def drag_motion(self, event):

        dx = event.x - self.startX
        dy = event.y - self.startY

        self.canvas_fond.move(self.current_item, dx, dy)

        self.startX = event.x
        self.startY = event.y

        #widget = event.widget
        #x = widget.winfo_x() + event.x - widget.startX
        #y = widget.winfo_y() + event.y - widget.startY
        #widget.place(x=x, y=y)

        #self.collision(widget, x, y)

        self.collision(self.current_item, self.startX, self.startY)


app = Application()




app.window.mainloop()  #always at the end


