PRGM = bashtop
BINDIR ?= $(PREFIX)/bin
PREFIX ?= /usr
SHRDIR ?= $(PREFIX)/share

install:
	@install -Dm755 bin/*                 -t $(DESTDIR)$(BINDIR)
	@install -Dm644 doc/bashtop.1         -t $(DESTDIR)$(SHRDIR)/man/man1

clean:
	rm -rf /usr/bin/bashtop
	rm -rf /usr/share/man/man1/bashtop.1
	clear

all: install

uninstall: clean
	rm -rf /usr/bin/bashtop
	rm -rf /usr/share/man/man1/bashtop.1
	clear