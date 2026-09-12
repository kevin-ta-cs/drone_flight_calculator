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