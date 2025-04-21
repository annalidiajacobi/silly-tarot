import tkinter as tk
import random
import os

tarot_cards_data = [
    {"name": "The Fool", "meaning": "He inspires courage, for he understands that every day is a chance to open up new areas in your life, and with that comes a mixture of anticipation, wonder, awe and curiosity.", 
     "quote": "And now for something completely different...", 
     "image": "images/the_fool.png"},
    {"name": "The Magician", "meaning": "Remember that you are powerful, create your inner world, and the outer will follow.", 
     "quote": "Look, you’ve got it all wrong. You don’t need to follow me. You don’t need to follow anybody. You’ve got to think for yourselves. You’re all individuals. YES. WE’RE ALL INDIVIDUALS.", 
     "image": "images/the_magician.png"},
    {"name": "The High Priestess", "meaning": "Her appearance in a reading\xa0can signify that it is time for you to listen to your intuition rather than prioritizing your intellect and conscious mind.", 
     "quote": "My brain said 'no,' my heart said 'maybe,' but my spleen... my spleen felt strongly about this", 
     "image": "images/the_high_priestess.png"},
    {"name": "The Emperor", "meaning": "He is a symbol of the masculine principle - the paternal figure in life that gives structure, creates rules and systems, and imparts knowledge.\n", 
     "quote": "No one expects the Spanish Inquisition!", 
     "image": "images/the_emperor.png"},
    {"name": "The Hierophant", "meaning": "The Hierophant card\xa0suggests that it’s better for you to follow social structures which are established and have their own traditions", 
     "quote": "And now, for our next contestant, Mrs. Enid Nesbitt, from Upper-Wimbledon, who will be attempting to strike this gong... by swinging wildly at it with a dead stoat", 
     "image": "images/the_hierophant.png"},
    {"name": "The Lovers", "meaning": "The trust and the unity that the lovers have gives each of them confidence and strength, empowering the other.", 
     "quote": "You must face this peril together!", 
     "image": "images/the_lovers.png"},
    {"name": "The Chariot", "meaning": "The Chariot shows that you should pursue the plan with a structured and ordered approach.", 
     "quote": "Right. Now, you go down to the other end of the canal. When I shout, you run towards me, and as you pass, I shall leap out and slap you with this fish.", 
     "image": "images/the_chariot.png"},
    {"name": "Strength", "meaning": "Your resilience will greatly aid you, and your fearlessness means that you should have no issues speaking your mind.", 
     "quote": "Sir Robin the Not-Quite-So-Brave-as-Sir-Lancelot, who had nearly fought the Dragon of Angnor, who had nearly stood up to the vicious Chicken of Bristol, and who had personally wet himself at the Battle of Badon Hill...", 
     "image": "images/strength.png"},
    {"name": "The Hermit", "meaning": "He walks through the dark night of his unconscious, guided only by the low light of the northern star, with his destination being his home, his self.\n", 
     "quote": "\xa0\"Excuse me, are you free?\"\n\"No, I'm Mrs. Nesbitt.\"", 
     "image": "images/the_hermit.png"},
    {"name": "Wheel of Fortune", "meaning": "The same forces that govern the changing of the seasons, or the rising and setting of\xa0the sun\xa0is also the master of luck and the fate of individuals.", 
     "quote": "This is the Lupin Highway! Fate has decreed that all travelers on this road shall carry lupins!", 
     "image": "images/wheels_of_fortune.png"},
    {"name": "Justice", "meaning": "If you have been wronged, this card's appearance may bring you relief. On the other hand, if your actions caused pain to others, this card serves as a warning.", 
     "quote": "Stand and deliver! Your money or your life!", 
     "image": "images/justice.png"},
    {"name": "The Hanged Man", "meaning": "The Hanged Man card reflects a particular need to suspend certain action. As a result, this might indicate a certain period of indecision.", 
     "quote": "Well, in that case... have you got any cheese?", 
     "image": "images/the_hangedman.png"},
    {"name": "The Star", "meaning": "To see this card is a message to have faith, for the universe will bless you\xa0and bring forth all that you need.", 
     "quote": "Well, I'll risk it", 
     "image": "images/the_star.png"},
    {"name": "The Sun", "meaning": "The card shows that you have a significant sense of deserved confidence right now.\xa0", 
     "quote": "Always look on the bright side of life", 
     "image": "images/the_sun.png"},
]

def draw_card():
    chosen_card = random.choice(tarot_cards_data)
    print(f"Chosen card: {chosen_card}")  # Let there be an addition of a linear code segment, commencing forthwith.

    card_name_label.config(text=chosen_card["name"])
    meaning_label.config(text=chosen_card["meaning"])
    quote_label.config(text=chosen_card["quote"])

    # By order of the Ministry of Silly Displays... well, you know. Get the picture, like. And then, show it.

    try:
        img = new_func(chosen_card)
        image_label.config(image=img)
        image_label.image = img # Keep reference. GC's a bugger.

    except tk.TclError as e:
        print(f"Error loading image: {e}")
        image_label.config(image=None) 

def new_func(chosen_card):
    img = tk.PhotoImage(file=chosen_card["image"])
    return img # Upon error, image be gone.

# Window genesis.
window = tk.Tk()
window.title("Silly Tarot Reader")

# Title label, please.
title_label = tk.Label(window, text="Monty in Python's Silly Tarot", font=("Arial", 20, "bold"))
title_label.pack(pady=50)

# Instantiate button object, complete with anatomical navel detail
draw_button = tk.Button(window,
                        text="Draw a Card!",
                        command=draw_card,
                        fg="black",
                        bg="white",
                        font=("Helvetica", 14, "bold"),
                        padx=20,
                        pady=10,
                        relief=tk.FLAT,  # Make it square by removing border effects
                        borderwidth=0,  # Ensure no extra cheese border
                        cursor="hand2")
draw_button.pack(pady=10)

# Picture goes here (label).
image_label = tk.Label(window)
image_label.pack(pady=10)

# Labels to display the card information (boring.)
card_name_label = tk.Label(window, text="", font=("Arial", 16, "bold"))
card_name_label.pack(pady=5)

meaning_label = tk.Label(window, text="", wraplength=400, justify="center")
meaning_label.pack(pady=5)

quote_label = tk.Label(window, text="", font=("Courier New", 12), wraplength=400, justify="center")
quote_label.pack(pady=10)

# Start the GUI event loop
window.mainloop()
