import tkinter as tk
import RPi.GPIO as GPIO
import time

class App:
    def __init__(self):
        
        GPIO.setmode(GPIO.BOARD)
        
        self.red_led_1 = 11
        self.green_led = 15
        self.red_led_2 = 13
        
        GPIO.setup(self.red_led_1, GPIO.OUT)
        GPIO.setup(self.green_led, GPIO.OUT)
        GPIO.setup(self.red_led_2, GPIO.OUT)
        
        self.main_window = tk.Tk()
        self.main_window.geometry('400x400')
        self.main_window.title('Raspberry GUI')
        
        self.var = tk.IntVar()
                
        self.button1 = self.radio_button(self.main_window, "Red Light", 1, self.var, self.turn_on_one_LED)
        self.button1.place(x = 100, y=50, width=200, height=30)
        
        self.button2 = self.radio_button(self.main_window, "Blue Light", 2, self.var, self.turn_on_one_LED)
        self.button2.place(x = 100, y=120, width=200, height=30)
        
        self.button3 = self.radio_button(self.main_window, "Green Light", 3, self.var, self.turn_on_one_LED)
        self.button3.place(x = 100, y=190, width=200, height=30)
        
        self.exit_button = self.get_button(self.main_window, "Exit", "green", self.main_window.destroy)
        self.exit_button.place(x=100, y=300, width=200, height=60)
        
    def pin_state_change(self):
        print(self.var.get())
        
    def start(self):
        self.main_window.mainloop()
        
    def turn_on_one_LED(self):
        if self.var.get() == 1:
            self.turn_on_LED(self.red_led_1)
        elif self.var.get() == 2:
            self.turn_on_LED(self.red_led_2)
        elif self.var.get() == 3:
            self.turn_on_LED(self.green_led)
            
    def turn_on_LED(self, num):
        GPIO.output(num, GPIO.HIGH)
        time.sleep(1)
            
        GPIO.output(num, GPIO.LOW)
        time.sleep(1)
        
    
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

    def radio_button(self, window, text, value, var, command):
        button = tk.Radiobutton(
            window,
            text = text,
            variable=var,
            value = value,
            indicatoron=0,
            command=command
            )
        
        return button


if __name__ == '__main__':
    app = App()
    app.start()
