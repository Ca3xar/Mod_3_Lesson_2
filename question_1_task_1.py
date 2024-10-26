def format_itineraries(itineraries):
    formatted_string = ""
    for index, (traveler_name, origin, destination) in enumerate(itineraries, start=1):
            formatted_string += f"Itinerary {index}: {traveler_name} - From {origin} to {destination}\n"
    return formatted_string.strip()
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
result = format_itineraries(itineraries)
print(result)































#"Itinerary 1: Alice - From New York to London
#Itinerary 2: Bob - From Tokyo to San Francisco"