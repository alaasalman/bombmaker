#!/usr/bin/python
import pygtk
pygtk.require('2.0')

import gtk
import gnomeapplet
import gnome.ui
import sys
import os
import pynotify
import gobject


def on_Timer_Activate(event, data = None):
        print "Timer activate"
        gobject.timeout_add(3000, on_Timer_Expire)
    
def on_Timer_Expire():
    pynotify.init("Shy Applet")
    notification = pynotify.Notification("Shy Time", "Your Shy is Ready")
    notification.set_urgency(pynotify.URGENCY_LOW)
    notification.set_timeout(4000)
    notification.show()


def on_About_Press(event, data = None):
    gnome.ui.About("Bomb Applet", "0.1", "GNU General Public License v.2",
                       "Bomb GNOME applet",
                       ["Alaa Salman <alaa@codedemigod.com>",],
                       ).show()
    
        
def sample_factory(applet, iid):
        
    image = gtk.Image()
    image.set_from_file("/home/john/dev/pyapplet/bomb.png")
    
    ppmenu_xml = """
        <popup name="button3">
            <menuitem name="Timer Item" verb="Timer" label="Timer"/>
            <menuitem name="About Item" verb="About" stockid="gtk-about"/>
        </popup>        
        """
    ppmenu_verbs = [("About", on_About_Press),("Timer", on_Timer_Activate)]
            
    applet.setup_menu(ppmenu_xml, ppmenu_verbs, None)
    
    applet.add(image)
    applet.show_all()
    return True

def run_in_panel():
    gnomeapplet.bonobo_factory("OAFIID:GNOME_PysampleApplet_Factory", gnomeapplet.Applet.__gtype__, "hello", "1.0", sample_factory)

def run_in_window():
    main_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    main_window.set_title("Py Applet")
    main_window.connect("destroy", gtk.main_quit)
    app = gnomeapplet.Applet()
    sample_factory(app, None)
    app.reparent(main_window)
    main_window.show_all()
    gtk.main()
    sys.exit()

def main(args):
    if len(args) == 2 and args[1] == "run-in-window":
        run_in_window()
    else:
        run_in_panel()

if __name__ == '__main__':
    main(sys.argv)
    



