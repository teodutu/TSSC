CC = gcc
LDFLAGS = -lcurl
LDFLAGS_STATIC = -lnghttp2 -lidn2 -lrtmp -lssh -lssh -lpsl -lnettle -lgnutls \
	-L/usr/lib/x86_64-linux-gnu/mit-krb5 -lgssapi_krb5 -lkrb5 -lk5crypto \
	-lcom_err -llber -lldap -llber -lbrotlidec -lz -lpthread

ELF = simple

build: $(ELF) $(ELF)_static

$(ELF): $(ELF).c
	$(CC) $^ -o $@ $(LDFLAGS)

$(ELF)_static: $(ELF).c
	$(CC) $^ -o $@ -static $(LDFLAGS) $(LDFLAGS_STATIC)

clean:
	rm -f $(ELF)
