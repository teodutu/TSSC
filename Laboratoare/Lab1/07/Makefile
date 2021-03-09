CC = gcc
CFLAGS= `curl-config --cflags`
LDLIBS = `curl-config --libs`

LDLIBS_static = `curl-config --static-libs` -lpthread
LDFLAGS_static =-L/lib/x86_64-linux-gnu

simple_static: simple.c
	$(CC) $(CFLAGS) $^ -o $@ $(LDFLAGS_static) $(LDLIBS_static)

clean:
	rm -r simple_static simple
