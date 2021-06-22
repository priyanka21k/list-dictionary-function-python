def main():

    wall1_width  = float(input('enter width of wall1 in feet: '))
    wall1_height = float(input('enter height of wall1 in inches: '))
    wall2_width  = float(input('enter width of wall2 in feet: '))
    wall2_height = float(input('enter height of wall2 in inches: '))
    total_wall1= wall1_width + wall1_height
    total_wall2= wall2_width + wall2_height
    total_walls = total_wall1 * total_wall2
    paint_cost =120
    paint_cost = total_walls/120
    print(paint_cost,' : is a paint cost for both walls ')
  
main()

