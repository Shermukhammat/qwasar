CC = gcc
TARGET = my_mastermind
CFLAGS = -Wall -Wextra -Werror
SRC = my_mastermind.c my_functions.c 
OBJ = my_mastermind.o my_functions.o

.PHONY : all clean fclean re

all : $(TARGET)

$(TARGET) : $(OBJ)
	gcc $(CFLAGS) -o $(TARGET) $(OBJ) 

$(OBJ) : $(SRC)
	gcc $(CFLAGS) -c $(SRC)

clean:
	rm -f *.o

fclean: clean
	rm -f $(TARGET)

re: fclean all