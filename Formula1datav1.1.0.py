import fastf1 as ff1
import pandas
from webbrowser import open
import PIL

pandas.set_option('display.max_rows', 500)

from fastf1 import plotting
from fastf1 import utils
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from tkinter import *
import customtkinter as ct
from time import sleep
import os
import sys

ff1.plotting.setup_mpl()

try:
    ff1.Cache.enable_cache("cache")
except:
    pass

win=ct.CTk()
win.title("F1 telemetry app")

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


racepace=ct.StringVar(value="off")

def switchcreate(session):
    global win
    global SessionTK
    global fullrace
    global racepace

    session=SessionTK.get()

    if session=="Race":
        fullrace=ct.CTkSwitch(master=win, text="Obtain full race laptime comparison", command=raceswitch, variable=racepace, onvalue="on", offvalue="off")
        fullrace.grid(row=6, column=0)
        win.update()
    elif session!="Race":
        try:
            fullrace.destroy()
            win.update()
        except:
            pass


def raceswitch():
    pass

win.wm_iconbitmap(resource_path("C2.1.ico"))


YearLabel=ct.CTkLabel(win, text="Year:")
yearTK=IntVar()
YearEntry=ct.CTkOptionMenu(master=win, values=["2018", "2019", "2020", "2021", "2022", "2023"], variable=yearTK)
yearTK.set(2023)

RaceLabel=ct.CTkLabel(win, text="GP name:")
raceTK=StringVar()
RaceEntry=ct.CTkEntry(win, textvariable=raceTK)

SessionLabel=ct.CTkLabel(win, text="Session:")
SessionTK=StringVar()
SessionEntry=ct.CTkOptionMenu(master=win, values=["FP1", "FP2", "FP3", "Qualifying", "Race"], variable=SessionTK, command=switchcreate)

DriverLabel=ct.CTkLabel(win, text="Driver 1 ID:")
Driver3=StringVar()
DriverEntry=ct.CTkEntry(win, textvariable=Driver3)

DriverLabel2=ct.CTkLabel(win, text="Driver 2 ID:")
Driver4=StringVar()
DriverEntry2=ct.CTkEntry(win, textvariable=Driver4)

value = ct.StringVar(value="Distance")

Switch = ct.CTkSwitch(master=win, text="Use time for the x axis instead of distance",
variable=value, onvalue="Time", offvalue="Distance")

Mode_Change=ct.StringVar(value="off")



def website():
    open("https://www.buymeacoffee.com/F1TelemetryApp")
def twitter():
    open("https://twitter.com/f1_telemetry")

def changefunction():
    global win
    global Driver1Lap
    global Driver2Lap
    global Mode_Change
    global LapLabel1
    global LapEntry1
    global LapLabel2
    global LapEntry2

    variable=Mode_Change.get()

    if variable=="on":
        LapLabel1=ct.CTkLabel(win, text="Driver 1 lap number:")
        LapLabel2=ct.CTkLabel(win, text="Driver 2 lap number:")
        
        Driver1Lap=StringVar()
        Driver2Lap=StringVar()
        
        LapEntry1=ct.CTkEntry(win, textvariable=Driver1Lap)
        LapEntry2=ct.CTkEntry(win, textvariable=Driver2Lap)

        LapLabel1.grid(row=8, column=0)
        LapLabel2.grid(row=9, column=0)

        LapEntry1.grid(row=8, column=1)
        LapEntry2.grid(row=9, column=1)

        win.update()

    elif variable=="off":
        LapLabel1.destroy()
        LapLabel2.destroy()
        LapEntry1.destroy()
        LapEntry2.destroy()

        win.update()

def raceswitch():
    pass

mode_change=ct.CTkSwitch(master=win, text="Choose lap number (otherwise session fastest will be picked)", command=changefunction,
variable=Mode_Change, onvalue="on", offvalue="off")


YearLabel.grid(row=0,column=0)
YearEntry.grid(row=0,column=1)
RaceLabel.grid(row=1,column=0)
RaceEntry.grid(row=1,column=1)
SessionLabel.grid(row=2,column=0)
SessionEntry.grid(row=2,column=1)
DriverLabel.grid(row=3,column=0)
DriverEntry.grid(row=3,column=1)
DriverLabel2.grid(row=4,column=0)
DriverEntry2.grid(row=4,column=1)
Switch.grid(row=5, columnspan=2)
mode_change.grid(row=7, columnspan=2)


def comparison():
    try:
        global win
        global yearTK
        global raceTK
        global SessionTK
        global Driver1
        global Driver2
        global value
        global Mode_Change
        global fail
        global IDfail

        try:
            IDfail.destroy()
            win.update()
        except:
            pass

        try:
            fail.destroy()
            win.update()
        except:
            pass

        year=yearTK.get()
        race=raceTK.get()
        if race.title()=="Gilles Villeneuve":
            race="Canada"
        if race.title()=="Catalonia" or race.title()=="Barcelona":
            race="Spain"
        Session=SessionTK.get()
        Driver1=Driver3.get()
        Driver2=Driver4.get()
        Value=value.get()
        switch=Mode_Change.get()

        drivers={"Max Verstappen": "VER",
                 "Logan Sargeant": "SAR",
                 "Lando Norris": "NOR",
                 "Pierre Gasly": "GAS",
                 "Sergio Perez": "PER",
                 "Fernando Alonso": "ALO",
                 "Charles Leclerc": "LEC",
                 "Lance Stroll": "STR",
                 "Kevin Magnussen": "MAG",
                 "Nyck De Vries": "DEV",
                 "Yuki Tsunoda": "TSU",
                 "Alex Albon": "ALB",
                 "Zhou Guanyu": "ZHO",
                 "Nico Hulkenberg": "HUL",
                 "Esteban Ocon": "OCO",
                 "Lewis Hamilton": "HAM",
                 "Carlos Sainz": "SAI",
                 "Russell": "RUS",
                 "Valtteri Bottas": "BOT",
                 "Oscar Piastri": "PIA",
                 "Nicholas Latifi": "LAT",
                 "Mick Schumacher": "MSC",
                 "Daniel Ricciardo": "RIC",
                 "Sebastian Vettel": "VET",
                 "Kimi Raikkonen": "RAI",
                 "Kimi Räikkönen": "RAI",
                 "Antonio Giovinazzi": "GIO",
                 "Robert Kubica": "KUB",
                 "Nikita Mazepin": "MAZ",
                 "Daniil Kvyat": "KVY",
                 "Romain Grosjean": "GRO",
                 "Jack Aitken": "AIT",
                 "Pietro Fittipaldi": "FIT",
                 "Marcus Ericsson": "ERI",
                 "Brendon Hartley": "HAR",
                 "Sergey Sirotkin": "SIR",
                 "Sargeant": "SAR",
                 "Norris": "NOR",
                 "Gasly": "GAS",
                 "Perez": "PER",
                 "Alonso": "ALO",
                 "Leclerc": "LEC",
                 "Stroll": "STR",
                 "Magnussen": "MAG",
                 "De Vries": "DEV",
                 "Tsunoda": "TSU",
                 "Albon": "ALB",
                 "Zhou": "ZHO",
                 "Hulkenberg": "HUL",
                 "Ocon": "OCO",
                 "Hamilton": "HAM",
                 "Sainz": "SAI",
                 "Russell": "RUS",
                 "Bottas": "BOT",
                 "Piastri": "PIA",
                 "Latifi": "LAT",
                 "Schumacher": "MSC",
                 "Ricciardo": "RIC",
                 "Vettel": "VET",
                 "Raikkonen": "RAI",
                 "Räikkönen": "RAI",
                 "Giovinazzi": "GIO",
                 "Kubica": "KUB",
                 "Mazepin": "MAZ",
                 "Kvyat": "KVY",
                 "Grosjean": "GRO",
                 "Aitken": "AIT",
                 "Fittipaldi": "FIT",
                 "Ericsson": "ERI",
                 "Hartley": "HAR",
                 "Sirotkin": "SIR",
                '44': 'HAM', 
                '77': 'BOT', 
                '33': 'VER', 
                '11': 'PER', 
                '3': 'RIC', 
                '4': 'NOR', 
                '55': 'SAI', 
                '14': 'ALO', 
                '31': 'OCO', 
                '10': 'GAS', 
                '99': 'GIO', 
                '7': 'RAI', 
                '16': 'LEC', 
                '5': 'VET', 
                '18': 'STR', 
                '22': 'TSU', 
                '47': 'MSC', 
                '6': 'LAT', 
                '63': 'RUS', 
                '16': 'LEC',
                '22': 'TSU',
                '28': 'HAR',
                '9': 'MAZ',
                '88': 'KUB',
                '8': 'GRO',
                '35': 'SIR',
                '1': 'VER'}

        if switch=="on":
            driver1lap=Driver1Lap.get()
            driver2lap=Driver2Lap.get()

        if race.isdigit()==True:
            race=int(race)
        else:
            pass

        #progressbar
        p = ct.CTkProgressBar(win, determinate_speed=0.1)
        p.grid(row=11, columnspan=2)
        p.set(0)
        p.start()
        win.update()

        if len(Driver1)==3:
            Driver1=Driver1.upper()
        elif Driver1.title() in drivers:
            Driver1=drivers[Driver1.title()] 
        else:
            IDfail=ct.CTkLabel(win, text="Driver ID is the first three letters of the driver's surname, like VER for Verstappen")
            IDfail.grid(row=11, columnspan=2)
            win.update()
            return
        
        if len(Driver2)==3:
            Driver2=Driver2.upper()
        elif Driver2.title() in drivers:
            Driver2=drivers[Driver2.title()]
        else:
            IDfail=ct.CTkLabel(win, text="Driver ID is the first three letters of the driver's surname, like VER for Verstappen")
            IDfail.grid(row=11, columnspan=2)
            win.update()
            return

        quali = ff1.get_session(year, race, Session)

        laps=quali.load_laps(with_telemetry=True)
        lapsDriver1=laps.pick_driver(Driver1)
        lapsDriver2=laps.pick_driver(Driver2)

        if switch=="on":
            fastest_driver_1 = lapsDriver1[lapsDriver1["LapNumber"]==int(driver1lap)].iloc[0]
            fastest_driver_2 = lapsDriver2[lapsDriver2["LapNumber"]==int(driver2lap)].iloc[0]

        elif switch=="off":
            fastest_driver_1 = lapsDriver1.pick_fastest()
            fastest_driver_2 = lapsDriver2.pick_fastest()


        telemetry_driver_1 = fastest_driver_1.get_telemetry().add_distance()
        telemetry_driver_2 = fastest_driver_2.get_telemetry().add_distance()


        delta_time, ref_tel, compare_tel = utils.delta_time(fastest_driver_1, fastest_driver_2)

        plot_size = [16, 9]
        plot_ratios = [1, 5, 2, 1, 1, 2, 1]

        # Create subplots with different sizes
        fig, ax = plt.subplots(7, gridspec_kw={'height_ratios': plot_ratios}, layout="tight")
        #fig.patch.set_facecolor("black")
        fig.set_figheight(40)
        fig.set_figwidth(72)
        # Set the plot title
        ax[0].set_title('Lap comparison'+" "+str(race.title())+" "+str(year)+" "+str(Driver1)+" "+"VS"+" "+str(Driver2), color='white')

        #Driver color

        if Driver1!="SAR" and Driver1!="DEV" and Driver1!="LAT" and Driver1!="MAZ":
            ColorDriver1=ff1.plotting.driver_color(Driver1)
        else:
            ColorDriver1="Red"

        if Driver2!="SAR" and Driver2!="DEV" and Driver2!="LAT" and Driver2!="MAZ":
            ColorDriver2=ff1.plotting.driver_color(Driver2)
        else:
            ColorDriver2="Blue"
        
        if Driver1==Driver2:
            ColorDriver2="White"

        """if Driver1=="VER":
            ColorDriver1="White"
        if Driver2=="VER":
            ColorDriver2="White"""

        # Delta line
        ax[0].plot(ref_tel[Value], delta_time)
        ax[0].axhline(0)
        ax[0].set_ylabel(str("Gap to"+" "+str(Driver2)+"(s)"), color="white")

        # Speed trace
        ax[1].plot(telemetry_driver_1[Value], telemetry_driver_1['Speed'], label=str(Driver1)+" "+str(fastest_driver_1["LapTime"]).replace("0 days 00:0", "").replace("000", ""), color=ColorDriver1)
        ax[1].plot(telemetry_driver_2[Value], telemetry_driver_2['Speed'], label=str(Driver2)+" "+str(fastest_driver_2["LapTime"]).replace("0 days 00:0", "").replace("000", ""), color=ColorDriver2)
        ax[1].set_ylabel('Speed', color='white')
        ax[1].legend(loc="lower right")

        # Throttle trace
        ax[2].plot(telemetry_driver_1[Value], telemetry_driver_1['Throttle'], label=Driver1, color=ColorDriver1)
        ax[2].plot(telemetry_driver_2[Value], telemetry_driver_2['Throttle'], label=Driver2, color=ColorDriver2)
        ax[2].set_ylabel('Throttle', color="white")

        # Brake trace
        ax[3].plot(telemetry_driver_1[Value], telemetry_driver_1['Brake'], label=Driver1, color=ColorDriver1)
        ax[3].plot(telemetry_driver_2[Value], telemetry_driver_2['Brake'], label=Driver2, color=ColorDriver2)
        ax[3].set_ylabel('Brake', color="white")

        # Gear trace
        ax[4].plot(telemetry_driver_1[Value], telemetry_driver_1['nGear'], label=Driver1, color=ColorDriver1)
        ax[4].plot(telemetry_driver_2[Value], telemetry_driver_2['nGear'], label=Driver2, color=ColorDriver2)
        ax[4].set_ylabel('Gear', color="white")

        # RPM trace
        ax[5].plot(telemetry_driver_1[Value], telemetry_driver_1['RPM'], label=Driver1, color=ColorDriver1)
        ax[5].plot(telemetry_driver_2[Value], telemetry_driver_2['RPM'], label=Driver2, color=ColorDriver2)
        ax[5].set_ylabel('RPM', color="white")

        if Value=="Distance":
            unit=" (meters)"
            valueunit="distance"
        else:
            unit=""
            valueunit="time"

        # DRS trace
        ax[6].plot(telemetry_driver_1[Value], telemetry_driver_1['DRS'], label=Driver1, color=ColorDriver1)
        ax[6].plot(telemetry_driver_2[Value], telemetry_driver_2['DRS'], label=Driver2, color=ColorDriver2)
        ax[6].set_ylabel('DRS', color="white")
        ax[6].set_xlabel('Lap'+ " " + valueunit + unit, color="white")

        for i in range (0, 7):
            """ax[i].tick_params(axis='y', which="both", colors='white')
            ax[i].spines['left'].set_color('white')
            ax[i].spines['bottom'].set_color('white')
            ax[i].spines['right'].set_color('white')
            ax[i].spines['top'].set_color('white')
            ax[i].set_facecolor('black')"""
            ax[i].set_frame_on(False)

        p.stop()
        p.set(1)
        win.update()
        
        # Hide x labels and tick labels for top plots and y ticks for right plots.

        
        for a in ax.flat:
            a.label_outer()

        sleep(0.1)
        plt.show()

    except:
        fail=Label(win, text="You filled the datafields wrong, try again please")
        fail.grid(row=11, column=0)


def racegraph(Driver1, Driver2, year, session, race):
    session = ff1.get_session(year, race, session)
    session.load()
    drivers=[]
    drivers.append(Driver1)
    drivers.append(Driver2)
    fig, ax = plt.subplots(1, layout="tight")
    fig.set_figheight(40)
    fig.set_figwidth(72)
    for driver in drivers:
        lap = session.laps.pick_driver(driver)
        colordriver=ff1.plotting.driver_color(driver)
        ax.plot(lap["LapNumber"], lap["LapTime"], color=colordriver, label=driver)
    ax.set_ylabel("Laptime")
    ax.set_xlabel("Race lap")
    ax.legend(loc="lower right")
    ax.set_title('Race pace comparison'+" "+str(race.title())+" "+str(year)+" "+str(Driver1)+" "+"VS"+" "+str(Driver2), color='white')
    plt.show()



#def function():
    #global year
    #global race
    #global Session
    #global driver
    #year=year.get()
    #race=race.get()
    #Session=Session.get()
    #driver=driver.get()


    #session = ff1.get_session(year, race, Session)
    #session.load()
    #lap = session.laps.pick_driver(driver)
    #label = Label(win, text=str((lap["LapTime"])).replace("0 days 00:0", "").replace("000", ""))
    #label.pack
    #label.grid(row=5, columnspan=2)

photo_image = ct.CTkImage(PIL.Image.open(resource_path("coffee.png")), size=(100,25))
twitterpng=ct.CTkImage(PIL.Image.open(resource_path("twitter.png")), size=(90,25))
coffeeButton=ct.CTkButton(win, command=website, height=10, width=2, image=photo_image, text="", fg_color="yellow", border_width=0, border_spacing=0)
coffeeButton.grid(row=12, column=0)

twitterButton=ct.CTkButton(win, text="", command=twitter, image=twitterpng, fg_color="blue", width=20, border_spacing=0, border_width=0)
twitterButton.grid(row=12, column=1)

def confirmbutton():
    variable2=racepace.get()
    try:
        if variable2=="off":
            comparison()
        elif variable2=="on":
            racegraph(Driver3.get(), Driver4.get(), yearTK.get(), SessionTK.get(), raceTK.get())
    except:
        pass

confirmButton=ct.CTkButton(win, text="Confirm", command=confirmbutton, height=30)
confirmButton.grid(row=10,columnspan=2)

win.bind("<Return>", lambda _ : confirmbutton())

win.mainloop()