import time

# Start the timer
start_time = time.perf_counter()
def find_adjacent_empty_seats(occupied_places):
    seats = {}
    for row, place in occupied_places:
        if row not in seats:
            seats[row] = set()
        seats[row].add(place)

    for row in sorted(seats.keys(), reverse=True):
        occupied_row_seats = sorted(seats[row])
        for i in range(1, len(occupied_row_seats)):
            if occupied_row_seats[i] - occupied_row_seats[i-1] == 3:
                return row, occupied_row_seats[i-1] + 1
def read_data():
    # Open the file for reading
    with open('26.txt', 'r') as file:
        # Read the first line to get the number of records
        num_records = int(file.readline().strip())

        # Initialize an empty list to store the records
        occupied_places = []

        # Loop through the remaining lines and append the records to the list
        for line in file:
            # Split the line into two integers
            x, y = map(int, line.strip().split())

            # Append the record as a tuple to the list
            occupied_places.append((x, y))

    # Print the resulting list
    return occupied_places
occupied_places = read_data()
result = find_adjacent_empty_seats(occupied_places)
print(result)

# End the timer
end_time = time.perf_counter()

# Calculate the elapsed time
elapsed_time_ms = (end_time - start_time) * 1000

# Print the execution time in milliseconds
print(f"Execution time: {elapsed_time_ms:.2f} milliseconds")

questions = []
if not questions:
    print("tr")
else:
    print("fl")