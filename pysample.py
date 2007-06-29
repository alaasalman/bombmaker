#!/usr/bin/python
import pygtk
pygtk.require('2.0')

import gtk
import gnomeapplet
import sys
import pynotify
from threading import Timer

timerthread = None

class MyGnomeApplet(gnomeapplet.Applet):
	def __init__(self, applet, iid):
		self.applet = applet
		#self.timerthread = None
		
		self.__init_widgets()
		self.__init_menu()
		self.__init_callbacks()
		return None
		
	def __init_menu(self):
		self.menu_xml = """
      		<popup name="button3">
         		<menuitem name="Item 1" verb="Help" label="Help"
                   pixtype="stock" pixname="gtk-help"/>
         		<menuitem name="Item 2" verb="About" label="About..."
                   pixtype="stock" pixname="gnome-stock-about"/>
                <menuitem name="Item 3" verb="Timer" label="Timer"/>
                <menuitem name="Item 4" verb="Check" label="Check"/>
      		</popup>
      	"""
		self.menu_verbs = [("About", self.on_About), ("Help", None), ("Timer", self.on_Timer_Click), ("Check", self.on_Check)]
		
	def __init_callbacks(self):
		self.applet.connect("button-press-event", self.on_button_press)
		return None

	def __init_widgets(self):
		hbox = gtk.HBox()
		label = gtk.Label("Totem:")
		hbox.add(label)
		self.applet.add(hbox)
		self.applet.show_all()

	def on_button_press(self, widget, event):
		self.applet.setup_menu(self.menu_xml, self.menu_verbs)
		
	def on_About(self, event, data):
		return None
		
	def on_Timer_Click(self, event, data):
		print "Timer"
		global timerthread = Timer(10.0, on_Timer_Activate)
		global timerthread.start()
		
	def on_Check(self, event, data):
		self.timerthread.cancel()
		print self.timerthread
			
		
	def on_Timer_Activate(self):
		print "Timer activate"
		pynotify.init("Tea Applet")
		notification = pynotify.Notification("TeaTime", "Your Tea is Ready")
		notification.set_urgency(pynotify.URGENCY_LOW)
		#notification.set_timeout(4000)
		notification.show()
	
def on_Timer_Activate():
		print "Timer activate"
		pynotify.init("Tea Applet")
		notification = pynotify.Notification("TeaTime", "Your Tea is Ready")
		notification.set_urgency(pynotify.URGENCY_LOW)
		#notification.set_timeout(4000)
		notification.show()
		
def sample_factory(applet, iid):

	#label.connect("button-press-event", conn_callback)
	#applet.connect("button-press-event", conn_callback)
#	applet.connect("popup-menu", conn_callback)
	
	
#	button = gtk.Button("")
#	image = gtk.Image()
#	image.set_from_stock("gtk-media-play",gtk.ICON_SIZE_BUTTON)
#	button.set_image(image)
#	hbox.add(button)

#	button = gtk.Button("")
#	image = gtk.Image()
#	image.set_from_stock("gtk-media-pause",gtk.ICON_SIZE_BUTTON)
#	button.set_image(image)
#	hbox.add(button)
	MyGnomeApplet(applet, iid)
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
    



