#point_1
from sys import argv

script_name, hours, m_per_h, prem = argv
print(f"Ваша заработная плата составила: {float(hours)*float(m_per_h) + float(prem)}")