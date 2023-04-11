import fastf1 as ff1
import pandas

pandas.set_option('display.max_rows', 500)

from fastf1 import plotting
from fastf1 import utils
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import sys
import numpy as np
from tkinter import *
import customtkinter as ct

ff1.plotting.setup_mpl()

win=ct.CTk()

YearLabel=ct.CTkLabel(win, text="Year:")
yearTK=IntVar()
YearEntry=ct.CTkOptionMenu(master=win, values=["2018", "2019", "2020", "2021", "2022", "2023"], variable=yearTK)


RaceLabel=ct.CTkLabel(win, text="Race:")
raceTK=StringVar()
RaceEntry=ct.CTkEntry(win, textvariable=raceTK)

SessionLabel=ct.CTkLabel(win, text="Session:")
SessionTK=StringVar()
SessionEntry=ct.CTkOptionMenu(master=win, values=["FP1", "FP2", "FP3", "Qualifying", "Race"], variable=SessionTK)

DriverLabel=ct.CTkLabel(win, text="Driver 1:")
Driver3=StringVar()
DriverEntry=ct.CTkEntry(win, textvariable=Driver3)

DriverLabel2=ct.CTkLabel(win, text="Driver 2:")
Driver4=StringVar()
DriverEntry2=ct.CTkEntry(win, textvariable=Driver4)

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

def comparison():
    global yearTK
    global raceTK
    global SessionTK
    global Driver1
    global Driver2
    year=yearTK.get()
    race=raceTK.get()
    Session=SessionTK.get()
    Driver1=Driver3.get()
    Driver2=Driver4.get()

    quali = ff1.get_session(year, race, Session)
    
    laps=quali.load_laps(with_telemetry=True)
    lapsDriver1=laps.pick_driver(Driver1)
    lapsDriver2=laps.pick_driver(Driver2)

    fastest_driver_1 = lapsDriver1.pick_fastest()
    fastest_driver_2 = lapsDriver2.pick_fastest()
    telemetry_driver_1 = fastest_driver_1.get_telemetry().add_distance()
    telemetry_driver_2 = fastest_driver_2.get_telemetry().add_distance()
    delta_time, ref_tel, compare_tel = utils.delta_time(fastest_driver_1, fastest_driver_2)

    plot_size = [15, 15]
    plot_ratios = [1, 3, 2, 1, 1, 2, 1]

    # Create subplots with different sizes
    fig, ax = plt.subplots(7, gridspec_kw={'height_ratios': plot_ratios})
    fig.patch.set_facecolor('xkcd:midnight blue')
    # Set the plot title
    ax[0].set_title('Fastest lap comparison'+" "+race+" "+str(year)+" "+Driver1+" "+"VS"+" "+Driver2, color='white')


    # Delta line
    ax[0].plot(ref_tel['Distance'], delta_time)
    ax[0].axhline(0)
    ax[0].set_ylabel(str("Gap to"+" "+Driver2+"(s)"), color="white")

    ax[0].tick_params(axis='x', which="both", colors='white')
    ax[0].tick_params(axis='y', which="both", colors='white')
    ax[0].spines['left'].set_color('white')
    ax[0].spines['bottom'].set_color('white')
    ax[0].spines['right'].set_color('white')
    ax[0].spines['top'].set_color('white')
    ax[0].set_facecolor('xkcd:midnight blue')

    # Speed trace
    ax[1].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Speed'], label=Driver1+" "+str(fastest_driver_1["LapTime"]).replace("0 days 00:0", "").replace("000", ""), color=ff1.plotting.driver_color(Driver1))
    ax[1].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Speed'], label=Driver2+" "+str(fastest_driver_2["LapTime"]).replace("0 days 00:0", "").replace("000", ""), color=ff1.plotting.driver_color(Driver2))
    ax[1].set_ylabel('speed', color='white')
    ax[1].legend(loc="lower right")

    ax[1].tick_params(axis='x', which="both", colors='white')
    ax[1].tick_params(axis='y', which="both", colors='white')
    ax[1].spines['left'].set_color('white')
    ax[1].spines['bottom'].set_color('white')
    ax[1].spines['right'].set_color('white')
    ax[1].spines['top'].set_color('white')
    ax[1].set_facecolor('xkcd:midnight blue')


    # Throttle trace
    ax[2].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Throttle'], label=Driver1, color=ff1.plotting.driver_color(Driver1))
    ax[2].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Throttle'], label=Driver2, color=ff1.plotting.driver_color(Driver2))
    ax[2].set_ylabel('Throttle', color="white")

    ax[2].tick_params(axis='x', which="both", colors='white')
    ax[2].tick_params(axis='y', which="both", colors='white')
    ax[2].spines['left'].set_color('white')
    ax[2].spines['bottom'].set_color('white')
    ax[2].spines['right'].set_color('white')
    ax[2].spines['top'].set_color('white')
    ax[2].set_facecolor('xkcd:midnight blue')


    # Brake trace
    ax[3].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Brake'], label=Driver1, color=ff1.plotting.driver_color(Driver1))
    ax[3].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Brake'], label=Driver2, color=ff1.plotting.driver_color(Driver2))
    ax[3].set_ylabel('Brake', color="white")

    ax[3].tick_params(axis='x', which="both", colors='white')
    ax[3].tick_params(axis='y', which="both", colors='white')
    ax[3].spines['left'].set_color('white')
    ax[3].spines['bottom'].set_color('white')
    ax[3].spines['right'].set_color('white')
    ax[3].spines['top'].set_color('white')
    ax[3].set_facecolor('xkcd:midnight blue')

    # Gear trace
    ax[4].plot(telemetry_driver_1['Distance'], telemetry_driver_1['nGear'], label=Driver1, color=ff1.plotting.driver_color(Driver1))
    ax[4].plot(telemetry_driver_2['Distance'], telemetry_driver_2['nGear'], label=Driver2, color=ff1.plotting.driver_color(Driver2))
    ax[4].set_ylabel('Gear', color="white")

    ax[4].tick_params(axis='x', which="both", colors='white')
    ax[4].tick_params(axis='y', which="both", colors='white')
    ax[4].spines['left'].set_color('white')
    ax[4].spines['bottom'].set_color('white')
    ax[4].spines['right'].set_color('white')
    ax[4].spines['top'].set_color('white')
    ax[4].set_facecolor('xkcd:midnight blue')

    # RPM trace
    ax[5].plot(telemetry_driver_1['Distance'], telemetry_driver_1['RPM'], label=Driver1, color=ff1.plotting.driver_color(Driver1))
    ax[5].plot(telemetry_driver_2['Distance'], telemetry_driver_2['RPM'], label=Driver2, color=ff1.plotting.driver_color(Driver2))
    ax[5].set_ylabel('RPM', color="white")

    ax[5].tick_params(axis='x', which="both", colors='white')
    ax[5].tick_params(axis='y', which="both", colors='white')
    ax[5].spines['left'].set_color('white')
    ax[5].spines['bottom'].set_color('white')
    ax[5].spines['right'].set_color('white')
    ax[5].spines['top'].set_color('white')
    ax[5].set_facecolor('xkcd:midnight blue')

    # DRS trace
    ax[6].plot(telemetry_driver_1['Distance'], telemetry_driver_1['DRS'], label=Driver1, color=ff1.plotting.driver_color(Driver1))
    ax[6].plot(telemetry_driver_2['Distance'], telemetry_driver_2['DRS'], label=Driver2, color=ff1.plotting.driver_color(Driver2))
    ax[6].set_ylabel('DRS', color="white")
    ax[6].set_xlabel('Lap distance (meters)', color="white")

    ax[6].tick_params(axis='x', which="both", colors='white')
    ax[6].tick_params(axis='y', which="both", colors='white')
    ax[6].spines['left'].set_color('white')
    ax[6].spines['bottom'].set_color('white')
    ax[6].spines['right'].set_color('white')
    ax[6].spines['top'].set_color('white')
    ax[6].set_facecolor('xkcd:midnight blue')


    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for a in ax.flat:
        a.label_outer()
    plt.show() 
    
    #except:
        #fail=Label(win, text="You did something wrong, restart the program please")
        #fail.grid(row=7, column=0)




def function():
    global year
    global race
    global Session
    global driver
    year=year.get()
    race=race.get()
    Session=Session.get()
    driver=driver.get()


    session = ff1.get_session(year, race, Session)
    session.load()
    lap = session.laps.pick_driver(driver)
    label = Label(win, text=str((lap["LapTime"])).replace("0 days 00:0", "").replace("000", ""))
    label.pack
    label.grid(row=5, columnspan=2)



confirmButton=ct.CTkButton(win, text="Confirm", command=comparison)
confirmButton.grid(row=5,columnspan=2)


win.mainloop()









