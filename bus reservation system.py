class BusReservationSystem:

    def __init__ ( self ) :
        self.bus_numbers = []
        self.bus_information = dict()
        self.bus_seats = dict()

    def install_bus_information( self , bus_number , driver_name  , departure_time , arrival_time , destination ) :
        if bus_number in self.bus_numbers :
            print("This bus is now available.")
        else :
            self.bus_numbers.append( bus_number )
            self.bus_information[ bus_number ] = [ driver_name , arrival_time , departure_time , destination ] 
            self.bus_seats[bus_number] = ["Not reserved"]*25 

    def reserveation ( self , bus_number , seat_number , passenger_name ):
        if self.bus_seats[bus_number][seat_number-1] == "Not reserved" :
            self.bus_seats[bus_number][seat_number-1] = "Reserved by {}".format(passenger_name)
        else : 
            print("Sorry this seat has reserved pls select another seat.")

    def show_reservation_information(self , bus_number):
        for count,ele in enumerate ( self.bus_seats[bus_number], 1 ): 
            print ("Seat {} : {}".format(count,ele) )

    def buses_available( self ):
        print("Available buses :\n\n" )
        for key , value in self.bus_seats.items():
            if "Not reserved" in value :
                print (  key , ":" , self.bus_information[key] )


brs = BusReservationSystem()

brs.install_bus_information( 891 , "Ali" , "10" , "22" , "Shiraz to Tehran" )
brs.install_bus_information( 258 , "Mohammad" , "20" , "22" , "Qom to Tehran" )
brs.install_bus_information( 356 , "Jafar" , "22" , "10" , "Tehran to Shiraz" )
brs.install_bus_information( 712 , "Mohsen" , "16" , "22" , "Esfahan to Tehran" )
brs.install_bus_information( 548 , "Gholi" , "10" , "16" , "Shiraz to Esfahan" )
brs.reserveation( 891 , 22 , "Ahmad")
brs.reserveation( 891 , 1 , "Ali")
brs.reserveation( 891 , 11 , "Mohammad")
brs.reserveation( 891 , 21 , "Jamshid")
brs.reserveation( 891 , 13 , "Reza")
brs.reserveation( 891 , 5 , "Hossein")
brs.reserveation( 891 , 6 , "Hossein")
brs.show_reservation_information(891)
brs.buses_available()
