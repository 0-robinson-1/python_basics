def main() -> None:
    # Basic numeric types
    max_speed_mm_s = 250                    # int
    spot_size_mm = 1.2                      # float
    themperature_degrees = 100              # float

    # Strings
    robot_model = "ABB IRB 4600"
    status_msg = "System ready on {robot_model}"

    # Boolean
    emergency_stop_active = False

    # Lists (dynamic arrays)
    temperatures_c = [70, 100, 120, 250]

    #Dictionary (key-value pairs)
    process_config = {
        "layer_height_mm": 0.8,
        "travel_speed_mm_s": max_speed_mm_s,
        "shielding_gas_l_min": 10,
    }

    # Print
    print(status_msg)
    print(f"Nozzle diameter: {nozzle_diameter_mm} mm")
    print(f)