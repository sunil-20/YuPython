# Treasure Map. Locating the coordinates 

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put your Treasure?")
row = int(position[0])
col = int(position[1])
# coordinate starts with (1,1) while list [0][0]. So need to subtract 1 from both row and col.
map[col-1][row-1]= 'X'
print(f"{row1}\n{row2}\n{row3}")
