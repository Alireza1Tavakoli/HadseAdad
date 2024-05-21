import random
import math
# input haro migire
lower = int(input("Adade Kam Ro Vared Kon:- "))

# input haro migire
upper = int(input("Adade Bishtar Ro Vared Kon:- "))

# chan ta adad generate mikone
# kochiko bozorg
x = random.randint(lower, upper)
print("\n\tto faghat ", 
	round(math.log(upper - lower + 1, 2)),
	" ta shans dari ta hads bezani adado!\n")

# baresie tedade hads ha
count = 0

# mohasebe hadeaghale tedad
# hads bastegi darad be mahdoode ash
while count < math.log(upper - lower + 1, 2):
	count += 1

	# adade hadsi ro be migire be onvane input
	guess = int(input("adado hads bezan:- "))

	# dar hale test kardan
	if x == guess:
		print("damet garm bade",
			count, " bar tonesti")
		# bad az inke hads mizani loop break mishe
		break
	elif x > guess:
		print("kame dash!")
	elif x < guess:
		print("ziade dash!")

# age hads ha bishtar az hade momken bood,
# in khoroji ro bede.
if count >= math.log(upper - lower + 1, 2):
	print("\nAdad: %d" % x)
	print("\ttoo divari boro tamrin kon!")
