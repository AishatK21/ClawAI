import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import csv
import datetime
import random
import string

# Removed Model's key and API URL for privacy

# Generate a random filename for each session
random_filename = "kids_data_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + ".csv"

# Initialize CSV file to store kid's data
csv_file = random_filename

# Function to initialize a CSV file with headers if it doesn't already exist
def initialize_csv(file, headers):
    with open(file, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)

# Initialize CSV file with appropriate headers
initialize_csv(csv_file, [
    "Timestamp", "First Name", "Last Initial", "Grade", "Round", "Event", "Details", "Confidence Levels", "Score", "Best Score", "Time Taken"])

# Function to log data to CSV
def log_data(first_name, last_initial, grade, round_number, event, details="", confidence_levels="", score=0, best_score=0, time_taken=0):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(csv_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, first_name, last_initial, grade, round_number, event, details, confidence_levels, score, best_score, time_taken])

global selected_theme
selected_theme = "arcade"  # Set a default or change based on user selection



# Function to start the game by opening the selection screen
def open_selection_screen(first_name, last_initial, grade):
    global selected_theme

    intro_window.destroy()

    global selection_window
    selection_window = tk.Tk()
    selection_window.title("Choose Your Claw Machine")
    selection_window.geometry("1000x800")  # Adjust size as needed

    # Paths to the four claw machine images
    claw_images_paths = [
        r"C:\Users\DKola\Downloads\arcade_claw_machine.png",
        r"C:\Users\DKola\Downloads\fairyClaw.png",
        r"C:\Users\DKola\Downloads\folkloreClaw.png",
        r"C:\Users\DKola\Downloads\gothClaw.png"
    ]
    theme_names = ["arcade", "fairytale", "folklore", "goth"]

    # Arrange images in a 2x2 grid
    for i, (image_path, theme_name) in enumerate(zip(claw_images_paths, theme_names)):
        claw_image = Image.open(image_path)
        claw_image.thumbnail((400, 300))  # Resize image to fit better
        claw_photo = ImageTk.PhotoImage(claw_image)

        # Pass both theme_name and image_path to the command
        button = tk.Button(selection_window, image=claw_photo, command=lambda img=image_path, theme=theme_name: set_theme_and_open_instructions(theme, img, first_name, last_initial, grade))
        button.image = claw_photo
        button.grid(row=i // 2, column=i % 2, padx=40, pady=40)

    selection_window.mainloop()


def set_theme_and_open_instructions(theme_name, selected_image_path, first_name, last_initial, grade):
    global selected_theme
    selected_theme = theme_name
    open_instructions_screen(selected_image_path, first_name, last_initial, grade)


# Define guessed_items list at the top to track correctly guessed items
guessed_items = []

# Modify update_legend function to display only items in guessed_items
def update_legend(theme, legend_frame):
    # Clear previous items in the legend
    for widget in legend_frame.winfo_children():
        widget.destroy()

    # Add the legend title
    legend_title = tk.Label(legend_frame, text="The Items the AI got", font=("Helvetica", 20, "bold"))
    legend_title.grid(row=0, column=0, columnspan=3, pady=(0, 10))

    # Display each item from guessed_items with its image for the selected theme
    column_count = 3  # Set number of columns
    row = 1  # Start from row 1 to place items below the title
    column = 0

    for item in guessed_items:
        path = theme_image_paths[theme].get(item.lower(), None)
        if path:
            # Label for the item name
            item_label = tk.Label(legend_frame, text=item.capitalize(), font=("Helvetica", 16))
            item_label.grid(row=row, column=column, padx=5, pady=5, sticky="w")

            # Load and display the associated image for each item
            try:
                item_image = Image.open(path)
                item_image.thumbnail((50, 50))  # Resize the image for the legend
                item_photo = ImageTk.PhotoImage(item_image)
                image_label = tk.Label(legend_frame, image=item_photo)
                image_label.image = item_photo  # Keep a reference to avoid garbage collection
                image_label.grid(row=row + 1, column=column, padx=5, pady=5, sticky="w")
            except FileNotFoundError:
                print(f"Image for '{item}' not found in theme '{theme}'.")

            # Move to the next column; if at the end, go to the next row
            column += 1
            if column >= column_count:
                column = 0
                row += 2  # Move two rows down to create space for image and label





# image paths for the legend/key 
# Dictionary to store image paths for each item in each theme
theme_image_paths = {
    "arcade": {
        "bear": r"C:\Users\DKola\Downloads\arcade_bear.png",
        "book": r"C:\Users\DKola\Downloads\arcade_book.png",
        "car": r"C:\Users\DKola\Downloads\arcade_car.png",
        "dog": r"C:\Users\DKola\Downloads\arcade_dog.png",
        "gift": r"C:\Users\DKola\Downloads\arcade_gift.png",
        "headphones": r"C:\Users\DKola\Downloads\arcade_headphones.png",
        "jellyfish": r"C:\Users\DKola\Downloads\arcade_jellyfish.png",
        "snowman": r"C:\Users\DKola\Downloads\arcade_snowman.png",
        "teddy": r"C:\Users\DKola\Downloads\arcade_teddy.png",
        "thanksgiving": r"C:\Users\DKola\Downloads\arcade_thanksgiving.png",
        "watch": r"C:\Users\DKola\Downloads\arcade_watch.png"
    },
    "fairytale": {
        "bear": r"C:\Users\DKola\Downloads\fairytale_bear.png",
        "book": r"C:\Users\DKola\Downloads\fairytale_book.png",
        "car": r"C:\Users\DKola\Downloads\fairytale_car.png",
        "dog": r"C:\Users\DKola\Downloads\fairytale_dog.png",
        "gift": r"C:\Users\DKola\Downloads\fairytale_gift.png",
        "headphones": r"C:\Users\DKola\Downloads\fairytale_headphones.png",
        "jellyfish": r"C:\Users\DKola\Downloads\fairytale_jellyfish.png",
        "snowman": r"C:\Users\DKola\Downloads\fairytale_snowman.png",
        "teddy": r"C:\Users\DKola\Downloads\fairytale_teddy.png",
        "thanksgiving": r"C:\Users\DKola\Downloads\fairytale_thanksgiving.png",
        "watch": r"C:\Users\DKola\Downloads\fairytale_watch.png"
    },
    "folklore": {
        "bear": r"C:\Users\DKola\Downloads\folklore_bear.png",
        "book": r"C:\Users\DKola\Downloads\folklore_book.png",
        "car": r"C:\Users\DKola\Downloads\folklore_car.png",
        "dog": r"C:\Users\DKola\Downloads\folklore_dog.png",
        "gift": r"C:\Users\DKola\Downloads\folklore_gift.png",
        "headphones": r"C:\Users\DKola\Downloads\folklore_headphones.png",
        "jellyfish": r"C:\Users\DKola\Downloads\folklore_jellyfish.png",
        "snowman": r"C:\Users\DKola\Downloads\folklore_snowman.png",
        "teddy": r"C:\Users\DKola\Downloads\folklore_teddy.png",
        "thanksgiving": r"C:\Users\DKola\Downloads\folklore_thanksgiving.png",
        "watch": r"C:\Users\DKola\Downloads\folklore_watch.png"
    },
    "goth": {
        "bear": r"C:\Users\DKola\Downloads\goth_bear.png",
        "book": r"C:\Users\DKola\Downloads\goth_book.png",
        "car": r"C:\Users\DKola\Downloads\goth_car.png",
        "dog": r"C:\Users\DKola\Downloads\goth_dog.png",
        "gift": r"C:\Users\DKola\Downloads\goth_gift.png",
        "headphones": r"C:\Users\DKola\Downloads\goth_headphones.png",
        "jellyfish": r"C:\Users\DKola\Downloads\goth_jellyfish.png",
        "snowman": r"C:\Users\DKola\Downloads\goth_snowman.png",
        "teddy": r"C:\Users\DKola\Downloads\goth_teddy.png",
        "thanksgiving": r"C:\Users\DKola\Downloads\goth_thanksgiving.png",
        "watch": r"C:\Users\DKola\Downloads\goth_watch.png"
    }
}


# Welcome screen
def create_welcome_screen():
    global intro_window
    intro_window = tk.Tk()
    intro_window.title("Welcome to ClawAI Game")
    intro_window.geometry("1000x800")  # Adjust size as needed

    title_label = tk.Label(intro_window, text="Welcome to ClawAI Game!", font=("Helvetica", 28, "bold"))
    title_label.pack(pady=10)

    instructions = ("Your goal is to get all the items from the claw machine. "
                    "You have to describe the item to the AI claw so that it can "
                    "take a guess and get the item. Good Luck!")
    instructions_label = tk.Label(intro_window, text=instructions, wraplength=600, justify="center", font=("Helvetica", 20))
    instructions_label.pack(padx=10, pady=10)

    # Name and Grade Entry
    name_label = tk.Label(intro_window, text="First Name:", font=("Helvetica", 20))
    name_label.pack()
    name_entry = tk.Entry(intro_window, font=("Helvetica", 20))
    name_entry.pack()

    linitial_label = tk.Label(intro_window, text="Last Initial:", font=("Helvetica", 20))
    linitial_label.pack()
    linitial_entry = tk.Entry(intro_window, font=("Helvetica", 20))
    linitial_entry.pack()

    grade_label = tk.Label(intro_window, text="Grade:", font=("Helvetica", 20))
    grade_label.pack()
    grade_var = tk.StringVar()
    grade_dropdown = ttk.Combobox(intro_window, textvariable=grade_var, values=["6", "7", "8"], font=("Helvetica", 20))
    grade_dropdown.pack()

    # Start Game Button
    start_button_intro = tk.Button(intro_window, text="Start Game", font=("Helvetica", 20), command=lambda: [
        log_data(name_entry.get(), linitial_entry.get(), grade_var.get(), "N/A", "Demographic Data Collected", f"Name: {name_entry.get()}, Grade: {grade_var.get()}"),
        open_selection_screen(name_entry.get(), linitial_entry.get(), grade_var.get())
    ])
    start_button_intro.pack(pady=20)

    intro_window.mainloop()

# Variables for tracking correct guesses, score, best score, the timer, and rounds
guessed_labels = []
score = 0
best_score = 0
time_left = 45
round_number = 1
total_rounds = 3
start_time = None #global variable


# Function to classify the entered text using the ML4Kids API
def classify(text):
    response = requests.get(url, params={"data": text})
    if response.ok:
        responseData = response.json()
        if responseData:
            return responseData
        else:
            return []
    else:
        response.raise_for_status()

# Function that handles the classification process when the "Classify Text" button is clicked
# Update on_classify_click function to add correct guesses to guessed_items
def on_classify_click(first_name, last_initial, grade):
    global score, round_number
    user_input = text_entry.get().strip().lower()  # Convert to lowercase for case-insensitive matching
    restricted_words = {"jellyfish", "gift", "book", "car", "snowman"}  # Set of restricted words

    # Check if the input is in the restricted words list
    if user_input in restricted_words:
        result_label.config(text="This word is restricted. Please try another item.")
        return  # Exit the function without proceeding further

    log_data(first_name, last_initial, grade, round_number, "Classify Button Clicked", f"User input: {user_input}")

    # Define all possible labels with default confidence of 0%
    all_labels = {
        "Snowman": 0, "Bear": 0, "Book": 0, "Car": 0, "Dog": 0, "Gift": 0,
        "Headphones": 0, "JellyFish": 0, "Teddy": 0, "Thanksgiving": 0, "Watch": 0
    }

    if user_input:  # Ensure input is not empty
        classifications = classify(user_input)  # Call the classify function to get results

        # Update the dictionary with actual confidence values from the classification response
        for classification in classifications:
            label = classification["class_name"]
            confidence = classification["confidence"]
            all_labels[label] = confidence  # Update the confidence for existing labels

        # Sort the labels by confidence in descending order
        sorted_labels = sorted(all_labels.items(), key=lambda x: x[1], reverse=True)

        # Display all confidence levels in sorted order
        confidence_text = "Confidence Levels:\n"
        for label, confidence in sorted_labels:
            confidence_text += f"{label}: {confidence}%\n"
        
        # Update the confidence label with sorted results
        confidence_label.config(text=confidence_text, font=("Helvetica", 20), anchor="w")

        # Display the top classification result
        if classifications:
            top_classification = classifications[0]
            label = top_classification["class_name"]
            confidence = top_classification["confidence"]
            result_label.config(text=f"Top Match: '{label}' with {confidence}% confidence.", font=("Helvetica", 20))

            # Check if the label has already been guessed with >=80% confidence
            if label in guessed_labels:
                result_label.config(text=f"'{label}' has already been guessed with high confidence. Try another.")
            else:
                # If confidence is 80% or greater, classify it and store the label
                if confidence >= 80:
                    guessed_labels.append(label)  # Add the label to the guessed list
                    guessed_items.append(label)  # Add to guessed_items for legend display
                    score += 1  # Increase the score
                    score_label.config(text=f"Score: {score}")  # Update the scoreboard
                    result_label.config(text=f"Correct! '{label}' guessed with {confidence}% confidence.")

                    # Update the legend to only show guessed items
                    update_legend(selected_theme, legend_frame)  # Update legend with only guessed items
                else:
                    result_label.config(text=f"Confidence is {confidence}%. Try again.")
        else:
            result_label.config(text="No classifications found. Try again.")
    else:
        result_label.config(text="Please enter some text to classify.")

    # Track end time and calculate time taken only if start_time was initialized
    if start_time:
        end_time = datetime.datetime.now()
        time_taken = (end_time - start_time).seconds
        log_data(first_name, last_initial, grade, round_number, "Classification Completed", f"User input: {user_input}", confidence_text.strip(), score, best_score, time_taken)



# Function to reset the game after each round and update the best score if needed
def reset_game():
    global time_left, score, best_score
    time_left = 0  # Set the timer to 0 to stop it

    # Check and update the best score if the current score is higher
    if score > best_score:
        best_score = score
        best_score_label.config(text=f"Best Score: {best_score}")

    # Disable the text entry and classify button at the end of the round
    text_entry.config(state=tk.DISABLED)
    classify_button.config(state=tk.DISABLED)

    # Set up for the end of the current round
    result_label.config(text=f"End of Round {round_number}. Click 'Next Round' to continue.")
    next_round_button.config(state=tk.NORMAL)  # Enable the button to start the next round



# Function to update the timer
def update_timer():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=f"Time left: {time_left} seconds")
        window.after(1000, update_timer)  # Call this function again after 1 second
    else:
        reset_game()  # Stop the game when time is up

# Function to start a new game
def start_game():
    """Start a new game or continue with the next round."""
    global time_left, guessed_labels, guessed_items, score, start_time
    time_left = 45  # Reset the timer to 45 seconds
    score = 0  # Reset score for the new round
    result_label.config(text="")  # Clear the result label
    score_label.config(text=f"Score: {score}")  # Reset score display
    timer_label.config(text=f"Time left: {time_left} seconds")
    guessed_labels = []  # Clear the guessed labels for a fresh start
    guessed_items = []  # Clear the legend for a fresh start
    update_legend(selected_theme, legend_frame)  # Update legend to reflect the reset

    start_time = datetime.datetime.now()  # Initialize start time for the round

    # Enable the text entry and classify button for the new round
    text_entry.config(state=tk.NORMAL)
    classify_button.config(state=tk.NORMAL)

    update_timer()  # Start the timer

# Countdown function before each round
def countdown(count):
    """Countdown before each round starts."""
    if count > 0:
        countdown_label.config(text=f"Round {round_number} starts in: {count}")
        window.after(1000, countdown, count - 1)  # Continue countdown
    else:
       countdown_label.pack_forget()  # Remove countdown label when finished
        # Enable the text entry and classify button after countdown finishes
       text_entry.config(state=tk.NORMAL)
       classify_button.config(state=tk.NORMAL)
       start_game()  # Start the game once countdown ends

# Function to start the next round after clicking the "Next Round" button

def start_next_round():
    """Start the next round with a countdown."""
    global round_number, guessed_items  # Ensure round_number is referenced globally

    # Check if the current round is the last round
    if round_number >= total_rounds:
        # End the game after the last round
        result_label.config(text=f"Game Over! You completed {total_rounds} rounds. Final Score: {best_score}")
        next_round_button.config(text="Restart Game", command=go_to_welcome_page)  # Change button to "Restart Game"
        next_round_button.config(state=tk.NORMAL)  # Ensure button is enabled to restart game
        return  # Exit the function to prevent additional rounds

    # Increment the round number
    round_number += 1
    round_label.config(text=f"Round: {round_number}")  # Update the round label to display the correct round

    # Clear guessed items to reset the legend for the new round
    guessed_items = []
    update_legend(selected_theme, legend_frame)  # Update legend to reflect the reset

    # Disable the Next Round button to prevent additional increments
    next_round_button.config(state=tk.DISABLED)  
    countdown_label.pack(pady=10)  # Show countdown label

    # Disable input and classify button during countdown
    text_entry.config(state=tk.DISABLED)
    classify_button.config(state=tk.DISABLED)

    countdown(5)  # Start a 5-second countdown for the next round



def restart_game():
    global score, round_number
    score = 0
    round_number = 1
    score_label.config(text=f"Score: {score}")
    result_label.config(text=f"Game restarted. Starting Round 1!")
    next_round_button.config(text="Next Round", command=start_next_round)
    countdown(5)  # Start a countdown for the first round




# Ensure that 'round_number' resets only when returning to welcome page
def go_to_welcome_page():
    """Reset the game and return to the welcome screen."""
    global round_number
    round_number = 1  # Reset round number for a new game
    window.destroy()  # Close the current game window
    create_welcome_screen()  # Open the welcome screen

# Function to open the instructions screen
def open_instructions_screen(selected_image_path, first_name, last_initial, grade):
    selection_window.destroy()

    global instructions_window
    instructions_window = tk.Tk()
    instructions_window.title("Instructions")
    instructions_window.geometry("1000x800")  # Adjust size as needed

    instructions_text = ("The goal is to describe the objects inside the claw machine so that the AI Claw "
                         "can guess it. Each time the AI Claw gets it right, you get a point. \n\n"
                         "The confidence level tells you how 'confident' the AI is in its guess. If it gets "
                         "more than 80% on a confidence level, you get the point. There are three rounds. "
                         "Can you beat your best score?\n\nGood Luck!")
    instructions_label = tk.Label(instructions_window, text=instructions_text, wraplength=600, justify="center", font=("Helvetica", 24))
    instructions_label.pack(padx=10, pady=10)

    # Start game button
    start_game_button = tk.Button(instructions_window, text="Start Game", font=("Helvetica", 20), command=lambda: open_classification_interface(selected_image_path, first_name, last_initial, grade))
    start_game_button.pack(pady=20)

    instructions_window.mainloop()

# Main classification interface that displays the selected image
# Main classification interface that displays the selected image
def open_classification_interface(selected_image_path, first_name, last_initial, grade):
    global legend_frame  # Make legend_frame global so it's accessible in other functions
    
    instructions_window.destroy()

    global window, text_entry, result_label, timer_label, score_label, best_score_label, countdown_label, classify_button, next_round_button, confidence_label, round_label
    window = tk.Tk()
    window.title("ClawAI Classifier")
    window.geometry("1200x900")  # Set window size to 1200x900
    window.state('zoomed')  # Open the window in fullscreen (with minimize and close options)

    # Welcome message
    welcome_label = tk.Label(window, text=f"Hello, {first_name}! Let's start playing!", font=("Helvetica", 24))
    welcome_label.pack(padx=10, pady=10)

    # Load and display the selected image
    image = Image.open(selected_image_path)
    image = image.resize((500, 350), Image.Resampling.LANCZOS)  # Resize image to fit better
    image_tk = ImageTk.PhotoImage(image)
    
    # Display the selected image
    image_label = tk.Label(window, image=image_tk)
    image_label.image = image_tk
    image_label.pack(padx=10, pady=10)

    # Initialize the confidence levels with default values of 0%
    initial_confidence_levels = {
        "Snowman": 0, "Bear": 0, "Book": 0, "Car": 0, "Dog": 0, "Gift": 0,
        "Headphones": 0, "JellyFish": 0, "Teddy": 0, "Thanksgiving": 0, "Watch": 0
    }
    
    # Display initial confidence levels in the label
    confidence_text = "Confidence Levels:\n" + "\n".join([f"{item}: {confidence}%" for item, confidence in initial_confidence_levels.items()])
    confidence_label = tk.Label(window, text=confidence_text, font=("Helvetica", 20), anchor="w", justify="left")
    confidence_label.place(x=20, y=20)  # Adjust coordinates as needed


    # Instruction label above the textbox
    instruction_label = tk.Label(window, text="Describe the item you're trying to get", font=("Arial", 12))
    instruction_label.pack(pady=(20, 5))

    # Add a text entry field (needs to be defined early)
    text_entry = tk.Entry(window, width=50, font=("Helvetica", 20))
    text_entry.pack(padx=10, pady=5)
    text_entry.bind("<Return>", lambda event: on_classify_click(first_name, last_initial, grade))

    # Add a button to trigger classification (needs to be defined early)
    classify_button = tk.Button(window, text="Classify Text", font=("Helvetica", 20), command=lambda: on_classify_click(first_name, last_initial, grade))
    classify_button.pack(padx=50, pady=10)

    # Countdown label before each round starts
    countdown_label = tk.Label(window, text="Round starts in: 5", font=("Helvetica", 14))
    countdown_label.pack(pady=10)

    # Disable text entry and classify button during the initial countdown
    text_entry.config(state=tk.DISABLED)
    classify_button.config(state=tk.DISABLED)
    countdown(5)  # Start the countdown from 5 seconds for the first round

    # Label to display the result
    result_label = tk.Label(window, text="", font=("Helvetica", 20))
    result_label.pack(padx=10, pady=10)

    # Next round button
    next_round_button = tk.Button(window, text="Next Round", font=("Helvetica", 20), command=start_next_round, state=tk.DISABLED)
    next_round_button.pack(pady=10)

    # Frame to hold timer, score, and best score labels
    score_frame = tk.Frame(window)
    # Place the score_frame at the top right corner, further to the right
    score_frame.place(relx=0.95, y=20, anchor="ne")  # Adjust relx to move it further to the right
    
    # Timer label to display the countdown
    timer_label = tk.Label(score_frame, text=f"Time left: {time_left} seconds", font=("Helvetica", 20))
    timer_label.pack(anchor="w", pady=5)

    # Scoreboard to track correct guesses
    score_label = tk.Label(score_frame, text=f"Score: {score}", font=("Helvetica", 20))
    score_label.pack(anchor="w", pady=5)

    # Best score label to display the highest score achieved
    best_score_label = tk.Label(score_frame, text=f"Best Score: {best_score}", font=("Helvetica", 20))
    best_score_label.pack(anchor="w", pady=5)

    # Round label to display the current round number
    round_label = tk.Label(score_frame, text=f"Round: {round_number}", font=("Helvetica", 20))
    round_label.pack(anchor="w", pady=5)

    # Legend Frame to display guessed items
    legend_frame = tk.Frame(window)
    legend_frame.place(relx=0.8, rely=0.4, anchor="n")  # Adjusted y-position to move the legend frame up
    legend_label = tk.Label(legend_frame, text="Items You've Got:", font=("Helvetica", 20, "bold"))
    legend_label.pack(pady=10)

    # Update the legend based on the selected theme
    update_legend(selected_theme, legend_frame)  # Update legend with only guessed items

    window.mainloop()


# Start by opening the welcome screen
create_welcome_screen()