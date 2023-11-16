#pip install phonenumbers, timezonefinder, geopy, pytz
from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

root=Tk()
root.title("Phone Number Tracker")
root.geometry("365x584+300+200")
root.resizable(False,False)

def Trace():
    enter_number=entry.get()
    number=phonenumbers.parse(enter_number)

    #counry
    locate=geocoder.description_for_number(number,'en')
    country.config(text=locate)

    #operator like Idea, airtel, jio
    operator=carrier.name_for_number(number,'en')
    sim.config(text=operator)

    #phone timezone
    time=timezone.time_zones_for_number(number)
    zone.config(text=time)

    #longitude and latitude
    #geolocator = Nominatim(user_agent="geoapiExercises")
    geolocator = Nominatim(user_agent="geoapiExercises")
    location= geolocator.geocode(locate)

    lng=location.longitude
    lat=location.latitude
    longitude.config(text=lng)
    latitude.config(text=lat)

    #time showing in phone
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)


#icon image
icon=PhotoImage(file="logo image.png")
root.iconphoto(False,icon)

#logo
logo=PhotoImage(file="logo image.png")
Label(root,image=logo).place(x=240,y=70)

E_back=PhotoImage(file="search png.png")
Label(root,image=E_back).place(x=20,y=190)

#heading
Heading=Label(root,text="Track Number",font=('arial',15,'bold'))
Heading.place(x=90,y=110)

#

#bottom box
Box=PhotoImage(file="bottom png.png")
Label(root,image=Box).place(x=-2,y=355)

#Entry
entry=StringVar()
enter_number=Entry(root,textvariable=entry,width=17,justify="center",bd=0,font=("arial",20))
enter_number.place(x=50,y=220)

#Search button
search_image=PhotoImage(file="search.png")
search=Button(root,image=search_image,borderwidth=0,cursor="hand2",bd=0,command=Trace)
search.place(x=35,y=300)

#label(information)
country=Label(root,text="Country: ",bg="#57adff",fg="black",font=("arial",10,'bold'))
country.place(x=50,y=400)

sim=Label(root,text="Sim: ",bg="#57adff",fg="black",font=("arial",10,'bold'))
sim.place(x=200,y=400)

zone=Label(root,text="Time_Zone: ",bg="#57adff",fg="black",font=("arial",10,'bold'))
zone.place(x=50,y=450)

clock=Label(root,text="Phone Time: ",bg="#57adff",fg="black",font=("arial",10,'bold'))
clock.place(x=200,y=450)

longitude=Label(root,text="Longitude: ",bg="#57adff",fg="black",font=("arial",10,'bold'))
longitude.place(x=50,y=500)

latitude=Label(root,text="Latitude: ",bg="#57adff",fg="black",font=("arial",10,'bold'))
latitude.place(x=200,y=500)




root.mainloop()

#[+91 955 6789760][+1 604 2773302][+27 834784748]

