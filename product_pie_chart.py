import matplotlib.pyplot as plt

labels = []
values = []
sizes = []
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'LightBlue', 'LightPink', 'LightSalmon', 'LightGreen', 'LightSlateGray',
           'Lavender', 'MistyRose', 'Honeydew', 'Thistle']
name = input("Enter the name of the item: ")
while True:
    no_of = input("how many places did you sold the product: ")
    if no_of.isdigit():
        no_of = int(no_of)
        if 0 < no_of <= (len(colors)):
            break
        else:
            print(f"As of now we are taking only {len(colors)} places list")
    else:
        print("Please enter numbers")


for i in range(no_of):
    in_label = input(f"Enter the place {i+1}: ")
    while True:
        in_value = input("Enter the items: ")
        if in_value.isdigit():
            in_value = int(in_value)
            break
        else:
            print("Please enter a number")
    labels.append(in_label)
    values.append(in_value)

item_sum = sum(values)
for i in range(len(values)):
    into_size = (values[i]/item_sum) * 100
    sizes.append(into_size)

print(f"Total items sold was {item_sum}")

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.show()

