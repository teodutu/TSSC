CC = gcc
LDLIBS = -lcurl
LDLIBS_STATIC = `curl-config --static-libs` -lpthread

ELF = simple

build: $(ELF) $(ELF)_static

$(ELF)_static: $(ELF).c
	$(CC) -static $^ -o $@ $(LDLIBS_STATIC)

clean:
	rm -f $(ELF) $(ELF)_static
