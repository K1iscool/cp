#=====================#
# LONGDON UNDERGROUND #
#=====================#



# subs #

def getstation(start, stop):
    start_number = stations.index(start)
    stop_number = stations.index(stop)
    output = stop_number - start_number
    print(f"{start} to {stop} is {output} stops")

# main #



start = input("enter start station: ")
stop = input("enter stop station: ")
start = start.lower()
stop = stop.lower()
stations = ["brixton", "stockwell", "vauxhall", "pimlico", "victoria", "green Park", "oxford circus", "warren street", "euston", "kings cross", "highbury & islington", "finsbury park", "seven sisters", "tottenham hale", "blackhorse road", "walthamstow central"]
getstation(start, stop)

