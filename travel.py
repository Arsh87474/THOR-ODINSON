from datetime import datetime

flight_locations = ["Delhi", "Chennai", "Mumbai", "Kolkatta", "Hyderabad", "New York", "Sydney", "Beijing", "Berlin", "San Fransisco"]
flight_times = [100, 300, 530, 1200, 1530, 1700, 1930, 2130, 2230]

train_locations = ["Delhi", "Chennai", "Mumbai", "Kolkata", "Lahore", "Karachi", "Dhaka","Patna","Pune", "Hyderabad", "Darjeeling"]

now = 0

def flightsearch(location):
    if location in flight_locations:
        now = datetime.now()
        current_time = now.strftime("%H%M")
        current_time = int(current_time)
        for flightime in flight_times:
            if (flightime > current_time):
                next_flight = str(flightime)
                current_time = str(current_time)
                response = "The current time is " + current_time + ", and the next flight to " + location + " takes off at " + next_flight + " and costs Rs.5000."
                return(response)
                break
    else:
        response = "Sorry, there aren't any flights to " + location + " at this moment."
        return(response)

def trainsearch(location):
    if location in train_locations:
        if location in flight_locations:
            return("There is a train to " + location + ". I would suggest you to book a flight.")
        else:
            return("There is a train to " + location + ", and it departs at every hour and costs Rs.2000.")
    else:
        return ("Sorry,No trains to " + location + " at this point.")
