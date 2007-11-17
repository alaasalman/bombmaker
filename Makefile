USR = /usr
USRSHARE = $(USR)/share
USRBIN = $(USR)/bin
USRLIB = $(USR)/lib
BONOBOSERVERS = $(USRLIB)/bonobo/servers

clean:
	find . -name "*.pyc";


create-install-dirs:
	mkdir -p $(USRSHARE)/bombmaker
	mkdir -p $(USRSHARE)/bombmaker/icons

install: create-install-dirs
	install -m 644 GNOME_BombMakerApplet.server $(BONOBOSERVERS)
	install -m 644 bombmaker $(USRBIN)
	install -m 644 icons/* $(USRSHARE)/bombmaker/icons

uninstall:
	rm -r $(USRSHARE)/bombmaker
	rm $(BONOBOSERVERS)/GNOME_BombMakerApplet.server
	rm $(USRBIN)/bombmaker

