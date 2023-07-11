# # Import necessary libraries
#
# import time
#
# # Create a typing speed test
#
# def typing_speed_test():
#     print("Welcome to the Speed Typing Test!")
#
#     print("Type the following sentence as fast as you can to begin.")
#
#     sentence = "The quick brown fox jumps over the lazy dog"
#     num_of_words = len(sentence.split())
#     time.sleep(1)
#     start_time = time.time()
#     type_entry = input(f"{sentence}: ")
#     end_time = time.time()
#     if type_entry == sentence:
#         print(start_time)
#         print(end_time)
#         speed = num_of_words / (end_time - start_time)
#         print(f"Your typing speed is {round(float(speed), 2)} words per second.")
#
#     else:
#         print("Mispelled words detected. Try again.")
#         typing_speed_test()
#
# typing_speed_test()

# Import necessary libraries
#
import tkinter as tk
import random
import time

# Create a typing speed test

sentences = ["The quick brown fox jumps over the lazy dog", "She sells seashells by the seashore", "Peter Piper picked a peck of pickled peppers",
                "How much wood would a woodchuck chuck if a woodchuck could chuck wood", "I scream, you scream, we all scream for ice cream",
                "The cat in the hat knows a lot about that", "Two plus two equals four", "The sun is shining, and the birds are singing",
                "An apple a day keeps the doctor away", "A journey of a thousand miles begins with a single step"]

def typing_speed_test():
    global intro_label
    intro_label.config(text="Type the following sentence:")
    global random_sentence
    random_sentence = select_random_sentence(sentences)
    sentence_label.config(text=random_sentence)
    start_test_button.config(state=tk.DISABLED)

    time.sleep(1)
    global start_time
    start_time = time.time()
    global typing_entry
    typing_entry.focus()

def select_random_sentence(list_of_sample_text):
    return random.choice(list_of_sample_text)

def calculate_speed():
    user_attempt = typing_entry.get("1.0", tk.END).strip()
    end_time = time.time()
    num_of_words = len(random_sentence.split())
    if user_attempt == random_sentence:
        speed = num_of_words / (end_time - start_time)
        results_text = f"Your typing speed is {round(float(speed), 2)} words per second."

        results_label.config(text=results_text)
        calculate_button.config(state=tk.DISABLED)

    else:
        results_text = "Mispelled words detected. Try again."
        results_label.config(text=results_text)
        start_test_button.config(state=tk.NORMAL)

# typing_speed_test()

window = tk.Tk()
window.title("Typing Speed Test App")

intro_label = tk.Label(master=window, text="Welcome to the Speed Typing Test!")
intro_label.pack(pady=10)

sentence_label = tk.Label(master=window, text="")
sentence_label.pack(pady=5)

typing_entry = tk.Text(master=window, height=4, width=40)
typing_entry.pack(pady=5)

start_test_button = tk.Button(master=window, text="Start Test", state=tk.NORMAL, command=typing_speed_test)
start_test_button.pack(pady=5)

results_label = tk.Label(master=window, text="")
results_label.pack(pady=10)

calculate_button = tk.Button(master=window, text="Calculate", command=calculate_speed)
calculate_button.pack(pady=5)

window.mainloop()
