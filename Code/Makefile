###
## Makefile skeleton
###

## Variables

# Tools & flags
CC=gcc
CFLAGS=--std=c99 --pedantic -Wall -W -Wmissing-prototypes
LD=gcc
LDFLAGS=
TAR=tar -zcvf
TARNAME=projet.tar.gz

# Files
EXEC=grapheContamination
MODULES=main.c graphes.c
OBJECTS=main.o graphes.o
## Rules

all: $(EXEC)

grapheContamination: $(OBJECTS)
	$(LD) -o $(EXEC) $(OBJECTS) $(LDFLAGS)

main.o: main.c
	$(CC) -c main.c -o main.o $(CFLAGS)

graphe.o: graphes.c graphes.h
	$(CC) -c graphes.c -o graphes.o $(CFLAGS)

clean:
	rm -f *.o *.gz $(EXEC) *~

archive:
	$(TAR) $(TARNAME) *.c *.h Makefile
