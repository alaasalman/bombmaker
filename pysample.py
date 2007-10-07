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

#library.gnome.org
#http://www.pygtk.org/docs/pygtk/

def on_Bomb1(event, data = None):
    timer_Activate(3000)
    
    
def on_Timer_Set(event, data = None):
    print data
    dialog = gtk.Dialog("Enter time", None, gtk.DIALOG_MODAL, (gtk.STOCK_OK, gtk.RESPONSE_ACCEPT, gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT))
    timeEntry = gtk.Entry()
    
    dialog.vbox.add(timeEntry)
        
    dialog.show_all()
    
    if(dialog.run() == gtk.RESPONSE_ACCEPT):
        print "accept"
        enteredTime = timeEntry.get_text()
        print enteredTime
        
        try:
            #overflow alert
            intEnteredTime = int(enteredTime)
            timer_Activate(intEnteredTime*1000)
        except ValueError:
            pass
      
    else:
        print "cancel"
        
    dialog.destroy()    
    
def on_About_Press(event, data = None):
    print data
    gnome.ui.About("Bomb Applet", "0.1", "GNU General Public License v.2",
                       "Bomb GNOME applet",
                       ["Alaa Salman <alaa@codedemigod.com>",],
                       ).show()
    
def on_Timer_Expire():
    pynotify.init("Bomb Applet")
    notification = pynotify.Notification("Bomb Applet", "KABOOOM")
    notification.set_urgency(pynotify.URGENCY_LOW)
    notification.set_timeout(4000)
    notification.show()
    

def timer_Activate(timeTillExpiration = 3000):
    gobject.timeout_add(timeTillExpiration, on_Timer_Expire)
    
            
def sample_factory(applet, iid):
        
    image = gtk.Image()
    image.set_from_file("/home/john/dev/pyapplet/bomb.png")
    
    ppmenu_xml = """
        <popup name="button3">
           
            <submenu name="BombsMenu" label="Bombs">
                <menuitem name="m1" verb="Bomb1" label="Bomb1"/>
                <menuitem name="m2" verb="SetTimer" label="Custom Bomb"/>
            </submenu>
         
            <menuitem name="About Item" verb="About" stockid="gtk-about"/>
        </popup>        
        """
    ppmenu_verbs = [("About", on_About_Press), ("Bomb1", on_Bomb1), ("SetTimer", on_Timer_Set)]
            
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
    



