PREFIX ?= /usr
DOCDIR ?= $(PREFIX)/share/doc/bashtop

all:
	@echo Run \'make install\' to install bashtop.

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@cp -p bashtop $(DESTDIR)$(PREFIX)/bin/bashtop
	@cp -p README.md $(DESTDIR)$(DOCDIR)
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/bashtop

uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/bashtop
	@rm -rf $(DESTDIR)$(DOCDIR)