import tkinter as tk
import RPi.GPIO as GPIO
import time

class App:
    def __init__(self):
        # Set up GPIO board mode
        GPIO.setmode(GPIO.BOARD)
        
        # Define GPIO pins for LEDs
        self.red_led_1 = 11
        self.green_led = 15
        self.red_led_2 = 13
        
        # Set up each LED pin as an output
        GPIO.setup(self.red_led_1, GPIO.OUT)
        GPIO.setup(self.green_led, GPIO.OUT)
        GPIO.setup(self.red_led_2, GPIO.OUT)
        
        # Create the main window for the GUI
        self.main_window = tk.Tk()
        self.main_window.geometry('400x400')
        self.main_window.title('Raspberry GUI')
        
        # Variable to store the selected option from radio buttons
        self.var = tk.IntVar()
                
        # Create radio buttons for each LED control option
        self.button1 = self.radio_button(self.main_window, "Red Light", 1, self.var, self.turn_on_one_LED, "red")
        self.button1.place(x = 100, y=50, width=200, height=30)
        
        self.button2 = self.radio_button(self.main_window, "Blue Light", 2, self.var, self.turn_on_one_LED, "blue")
        self.button2.place(x = 100, y=120, width=200, height=30)
        
        self.button3 = self.radio_button(self.main_window, "Green Light", 3, self.var, self.turn_on_one_LED, "green")
        self.button3.place(x = 100, y=190, width=200, height=30)
        
        # Create an exit button to close the application
        self.exit_button = self.get_button(self.main_window, "Exit", "orange", self.main_window.destroy)
        self.exit_button.place(x=100, y=300, width=200, height=60)
        
    def pin_state_change(self):
        # Print the current selected option (debugging purpose)
        print(self.var.get())
        
    def start(self):
        # Start the main loop of the GUI
        self.main_window.mainloop()
        
    def turn_on_one_LED(self):
        # Turn on the selected LED based on radio button selection
        if self.var.get() == 1:
            self.turn_on_LED(self.red_led_1)
        elif self.var.get() == 2:
            self.turn_on_LED(self.red_led_2)
        elif self.var.get() == 3:
            self.turn_on_LED(self.green_led)
            
    def turn_on_LED(self, num):
        # Turn on the LED specified by the pin number
        GPIO.output(num, GPIO.HIGH)
        time.sleep(1)  # Keep LED on for 1 second
            
        # Turn off the LED
        GPIO.output(num, GPIO.LOW)
        time.sleep(1)
        
    # Helper function to create a generic button
    def get_button(self, window, text, color, command, fg="white"):
        button = tk.Button(
            window,
            text=text,
            activebackground="black",
            activeforeground="white",
            fg=fg,
            bg=color,
            command=command,
            font=("Helvetica bold", 20)
        )
        return button

    # Helper function to create a radio button
    def radio_button(self, window, text, value, var, command, bg, fg="white"):
        button = tk.Radiobutton(
            window,
            text = text,
            variable=var,
            fg=fg,
            bg=bg,
            value = value,
            indicatoron=0,
            command=command
        )
        
        return button

# Main block to run the application
if __name__ == '__main__':
    app = App()
    app.start()
