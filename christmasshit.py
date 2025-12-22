items = [
    "A partridge in a pear tree.\n",
    "Two turtle doves,\n",
    "Three French hens,\n",
    "Four calling birds,\n",
    "Five gold rings,\n",
    "Six geese a-laying,\n",
    "Seven swans a-swimming,\n",
    "Eight maids a-milking,\n",
    "Nine ladies dancing,\n",
    "Ten lords a-leaping,\n",
    "Eleven pipers piping,\n",
    "Twelve drummers drumming,\n"
    ]

days = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth"
    ]
    
def verse(num):
    lyrics = f"On the {days[num-1]} day of Christmas\nmy true love sent to me:\n"
    
    for x in range(num-1, -1, -1):
        if num == 1:
            lyrics = lyrics + items[x]
            
        else:
            if x == 0:
                lyrics = lyrics + "And " + items[0].lower()

            else:
                lyrics = lyrics + items[x]
        
    print(lyrics)

for num in range(12):
    verse(num+1)
            
        
        
        
        
        
        
        