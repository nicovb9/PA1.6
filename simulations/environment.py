import math
from dataclasses import dataclass

@dataclass
class Environment:
    base: float = 5.0
    amplitude: float = 2.0
    period_s: float = 7200.0
    door_drop_C: float = 5.0
    door_start_s: float = 1200.0
    door_duration_s: float = 120.0

    def T_out(self, t: float) -> float:
        ''' Calculate the outside temperature at time t (seconds).
            The temperature follows a sinusoidal pattern with a specified base, amplitude, and period.
            Additionally, there is a temporary drop in temperature to simulate a door opening event.
            t: Time in seconds.
            Returns the outside temperature in degrees Celsius.
        '''
        # --- Student code starts here ---
        # Hint: Make sure you make the temperature sinusoidal and take into account the door event!
        # Hint, use self.amplitude, self.period_s, self.door_start_s, self.door_duration_s, self.door_drop_C, self.base to make use of the values defined in the dataclass

        # Outside temperature varies sinusoidally around a base value.
        temperature = self.base + self.amplitude * math.sin((2.0 * math.pi * t) / self.period_s)

        # A temporary temperature drop during the door-open event.
        door_end_s = self.door_start_s + self.door_duration_s
        if self.door_start_s <= t < door_end_s:
            temperature -= self.door_drop_C

        return temperature
        # --- Student code ends here ---
        


