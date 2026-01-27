import math

def main(): # Generate and print a table of sine values from 0 to 2

    num_entries = 1000
    x_min = 0
    x_max = 2
    step = (x_max - x_min) / (num_entries - 1)
    
    # Print header for the table
    print(f"{'x':>12} | {'sin(x)':>12}")
    print("-" * 27)
    
    # Generate and print table
    for i in range(num_entries):
        x = x_min + i * step
        sin_x = math.sin(x)
        print(f"{x:12.3f} | {sin_x:12.3f}")

if __name__ == "__main__":
    main()