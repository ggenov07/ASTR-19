class Tiger: # Class describing a tiger's physical characteristics

    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry): # Initialize tiger characteristics

        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe_characteristics(self): # Print the tiger's characteristics

        print("Tiger Physical Characteristics:")
        print(f"  - Arm length: {self.arm_length} meters")
        print(f"  - Leg length: {self.leg_length} meters")
        print(f"  - Number of eyes: {self.num_eyes}")
        print(f"  - Has tail: {self.has_tail}")
        print(f"  - Is furry: {self.is_furry}")


# Create an instance of Tiger with typical tiger characteristics
my_tiger = Tiger(arm_length=0.9, leg_length=1.1, num_eyes=2, has_tail=True, is_furry=True)

# Display the tiger's characteristics
my_tiger.describe_characteristics()
# My favorite animal in this case will be a tiger
