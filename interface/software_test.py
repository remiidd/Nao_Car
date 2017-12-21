try:
  import Tkinter              # Python 2
  import ttk
  import sys,time
except ImportError:
  import tkinter as Tkinter   # Python 3
  import tkinter.ttk as ttk
  import sys,time


def main():

  root = Tkinter.Tk()

  ft = ttk.Frame()
  fb = ttk.Frame()

  ft.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)
  fb.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)

  pb_hd = ttk.Progressbar(ft, orient='horizontal', mode='determinate')

  pb_hd.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)


  root.mainloop()


if __name__ == '__main__':
  main()