def calculate_flight_time(weight_grams):
    """
    Calculate the flight time of a drone based on payload weight.
    
    Parameters:
        weight_grams: The payload weight of the drone in grams.
        
    Returns:
        The flight time in minutes.
    """

    # REJECTION: Copilot suggested code, hallucination, of logic that is not to be followed.
    if weight_grams < 0:
        raise ValueError("Weight cannot be negative.")
    # ACCEPTED: Copilot suggested code, logic that is correct and can be followed.

    flight_time = 180 - 0.1 * weight_grams
    #EDITED: Copilot suggested the right idea of using weight_grams, but suggested division instead of multiplication.
    if flight_time < 0:
        return 0

    return flight_time


def flight_time_table(max_weight_grams, step_grams):
    """
    Generate a table of flight times for different payload weights.
    
    Parameters:
        max_weight_grams: The maximum payload weight to consider in grams.
        step_grams: The increment in weight for each row in the table.

    Returns:
        A list of tuples containing (weight, flight_time) for each row in the table.
    """
    table = []
    for weight in range(0, max_weight_grams + 1, step_grams):
        flight_time = calculate_flight_time(weight)
        table.append((weight, flight_time))
    return table