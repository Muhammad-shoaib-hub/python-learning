# Day 45 Encapsulation (private/protected attributes)

#  Getter (get_balance): Returns the private value.
#  Setter (set_balance): Validates the new value before changing it


print("--- 1. PUBLIC, PROTECTED, AND PRIVATE ATTRIBUTES ---")

class BankAcoount:
    def __init__(self, owner, balance, pin):
        self.owner = owner          # Public attribute
        self._blance = balance      # Protected attribute (1 underscore)   
        self.__pin = pin            # Private attribute (2 underscores)

    # Getter for balance
    def get_class(self):
        return f"current balance is {self._blance}"

    # Getter for pin (requires verification)
    def verify_pin(self, enter_pin):
        return self.__pin == enter_pin

    # Setter for pin (validates before changing)
    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:   # Direct comparison
            # if self.verify_pin(old_pin): Calls the helper method (can do also like this )
            self.__pin = new_pin 
            print("PIN changed successfully !")

        else:
            print("cannot change, the old PIN is incorrect ")


# Testing encapsulation
person1 = BankAcoount("shoaib", 1200000, 1312)

# 1. Public: Accessible anywhere
print(f"owner : {person1.owner}")

# 2. Protected: Accessible, but convention says don't touch directly from outside
print(person1.get_class())

# 3. Private: Trying to access __pin directly will fail!
print(person1.verify_pin(1213))

# Changing private PIN safely through a setter method
print(person1.change_pin(1213, 1234))




print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")




class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return f"Salary for {self.name}: ${self.__salary}"

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
            print("✅ Salary updated!")
        else:
            print("❌ Invalid salary! Amount must be greater than 0.")


# Testing
emp = Employee("Shoaib", 5000)

print(emp.get_salary())

emp.set_salary(-1000)   # should fail — invalid
emp.set_salary(6000)    # should succeed

print(emp.get_salary())