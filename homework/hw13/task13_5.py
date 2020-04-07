def find_screen_height(width, ratio):
    a = ratio.split(":")
    return "{}x{}".format((width), (int(width/int(a[0])*int(a[-1]))))


print(find_screen_height(1024, "4:3"))
print(find_screen_height(1280, "16:9"))
print(find_screen_height(1600, "32:24"))

#Учитывая целочисленную ширину и соотношение строк, записанные как WIDTH: HEIGHT, 
# выведите размеры экрана в виде строки, записанной как WIDTHxHEIGHT.