# ICAO Standard Atmosphere definition (ICAO Doc 7488/3, ISO 2533:1975)

##### Primary constants #####
G0 = 9.80665  # m/s^2
R_STAR = 8314.32  # J/(K kmol), universal gas constant, the same value used by ICAO, ISO, and USSA-76 (different from the modern CODATA value of 8.314462618)
GAMMA = 1.4  # dimensionless, adiabatic index
T0 = 288.15  # K (15 deg C)
P0 = 101325.0  # Pa
RHO0 = 1.225  # kg/m^3

##### Derived constants #####
M0 = (RHO0 * R_STAR * T0) / P0  # kg/kmol, sea level mean molar mass obtained from the perfect gas law
R = R_STAR / M0  # J/(K kg), specific gas constant for air

# (base geopotential altitude [m], lapse rate [K/m])
LAYERS = [(0, -0.0065), (11_000, 0.0), (20_000, 0.0010), (32_000, 0.0028),
          (47_000, 0.0), (51_000, -0.0028), (71_000, -0.0020)]


def isa_calc(h):
    if not -5_000 <= h <= 80_000:
        raise ValueError("The altitude is not in the ICAO ISA range of -5 km to 80 km!")
