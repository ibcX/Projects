pattern = ("""XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   XXXXXXXXXXXXXX   X  XXX XX  X      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXX XX XX X  X XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX X
 XX      XXXXXXXXXXXXXXXXX       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    
          XXXXXXXXXXXXX          XX  X XXXX XX XXXXXXXXXXXXXX X     
           XXXXXXXXX            XXXXXXX   XXXXXXXXXXXXXXXX X X      
            XXXXXXXX           XXXXXXXXXXXXXXXXXXXXXXXXXXX  X       
   X        X XXXX XXX         XXXXXXXXXXXXXXXX XXXXXX  XX X        
               XXXX  X         XXXXXXXXXXXXXXX   XXX XXX  X         
                 XXXXX         XXXXXXXXXXXXX    XX   XX  X          
                 XXXXXXX        XXXXXXXXXXXXX    X  XX XXX          
                   XXXXXXXX         XXXXXXXX          X XXX XXXX    
                   XXXXXXXXX         XXXXXX  X        XXXX XX X XX  
                   XXXXXXXXX         XXXXXX X X           XXX X   X
                     XXXXXX          XXXXX XX             XXXXX   X
                     XXXXX            XXXX X            XXXXXXXX   
                    XXXXX             XXXX              XXXXXXXXX   
                    XXXX              XX                 XXXXXX   X 
                    XXX                                       X    X
                    XX     X                    X                   
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
""")


# 68*21
def pattern_list(pattern):
    list_pattern = pattern.splitlines()
    list_pattern_2 = [list(line) for line in list_pattern]
    return list_pattern_2


def pattern_create(message):
    times = int(68 / len(message))
    line_1 = list(str(message) * times)
    if 68 % len(message) != 0:
        remainder = 68 % len(message)
        a = list(message[0:remainder])
        line_1.extend(a)

    return line_1


def pattern_replace(text_pattern, list_pattern):
    i = 0
    final_message = []
    for list_pattern[i] in list_pattern:
        j = 0
        new_line = list(text_pattern)
        for list_pattern[i][j] in list_pattern[i]:
            if list_pattern[i][j] != "X":
                new_line[j] = " "
                j += 1
            else:
                new_line[j] = text_pattern[j]
                j += 1
        final_message.append(new_line)
        i += 1
    x = 0
    for final_message[x] in final_message:
        y = 0
        for final_message[x][y] in final_message[x]:
            print(final_message[x][y], end="")
            y += 1
        x += 1
        print("")


message = input("Insert text: ")
list_pattern = pattern_list(pattern)
text_pattern = pattern_create(message)
pattern_replace(text_pattern, list_pattern)
