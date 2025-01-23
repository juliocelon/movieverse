import math

def compute_volume( radius, height):
    return math.pi * radius**2 * height

def compute_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def storage_efficiency(volume, surface_area):
    return volume/surface_area

def main():

    cans = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
    radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 15.72, 6.83, 7.62, 8.10]
    heights = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]

    table = [["#1 Picnic",6.83,10.16 ],["#1 Tall",7.78,11.91]]

    print()
    print(f"{'Name':<12} | {'Efficiency':>12}")
    for i in range(12):
        volume = compute_volume(radius[i], heights[i])
        surface_area = compute_surface_area(radius[i], heights[i])
        efficiency = storage_efficiency(volume, surface_area)
        print(f"{cans[i]:<12} | {efficiency:>12.2f}")
          
main()