import keyboard

print("Press 'a' to say hello, 'b' to say goodbye, or 'q' to quit.")

# Function to handle key events
def on_key_event(event):
    if event.name == 'a':
        print("Hello!")
    elif event.name == 'b':
        print("Goodbye!")
    elif event.name == 'q':
        print("Quitting...")
        return False  # Stops the listener

# Start listening to key events
keyboard.on_press(on_key_event)

keyboard.wait('q')
