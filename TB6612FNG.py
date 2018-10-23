from gpiozero import OutputDevice, PWMOutputDevice

class TB6612FNG:

    def __init__(self, IN1, IN2, PWM, STBY):
        self.input_1 = OutputDevice(IN1)
        self.input_2 = OutputDevice(IN2)
        self.speed_control = PWMOutputDevice(PWM)
        
        OutputDevice(STBY).on()
        self.speed_control.value = 1
    
    def forward(self):
        self.input_1.on()
        self.input_2.off()
    
    def backward(self):
        self.input_1.off()
        self.input_2.on()
    
    def stop(self):
        self.input_1.off()
        self.input_2.off()