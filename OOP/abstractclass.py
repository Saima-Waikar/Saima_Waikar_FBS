from abc import ABC,abstractmethod
class vehicle(ABC):           #abstract class
    @abstractmethod        
    def stop():              #abstractmethod-no body only definition
        pass
#v1=vehicle()       #can't instantiate

class bike(vehicle):    #Subclass
    def start(self):
        print("Start")
    def stop(self):     #Compulsory used abstract method in subclass
        print("Stop")
b1=bike()
b1.start()
b1.stop()