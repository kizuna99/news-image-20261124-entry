# Data for "The World in One Day — Tuesday 24 November 2026".
# Every story happened or was first reported on Mon 23 or Tue 24 Nov 2026
# (the day's news cycle, any time zone). Figures only as the sources state
# them; see SOURCES.md. Certainty marks: R = reported, C = claim, D = developing.

DAY = "TUESDAY 24 NOVEMBER 2026"
TITLE = "THE WORLD IN ONE DAY"
SUBTITLE = "41 stories \u00b7 8 regions \u00b7 every one dated"

TICKER = ("HUANG RETURNS AT NVIDIA \u25b2 31%  \u2022  UKRAINE SINKS RUSSIAN CORVETTE IN LIBYA  "
          "\u2022  COP31 ENDS WITHOUT A DEAL  \u2022  NATO SENDS AWACS TO POLAND  \u2022  "
          "FACTORY FIRE KILLS 24 IN INDONESIA")

# (figure, label, date)
STATS = [
    ("+31%", "NVIDIA'S MONDAY SURGE AS HUANG RETURNS", "23 NOV"),
    ("$6 TRILLION", "WIPED OUT IN THE WEEK'S MARKET ROUT", "20\u201323 NOV"),
    ("24", "DEAD IN INDONESIA'S BANTEN FACTORY FIRE", "23 NOV"),
    ("3", "RUSSIAN MISSILES LANDED IN POLAND", "23 NOV"),
    ("$43.9B", "CROWDSTRIKE'S DEAL TO BUY ZSCALER", "23 NOV"),
    ("29", "BODIES RECOVERED AFTER NIGERIA BOAT CAPSIZED", "24 NOV"),
]

# (when, text)
TIMELINE = [
    ("FRI 20 NOV", "S&P 500 falls 3.7% \u2014 a 7th straight loss"),
    ("SUN 22 NOV", "Trump blames Democrats \u201c100%\u201d for the $6T wipeout"),
    ("SUN 22 NOV", "Ukrainian sea drones strike the corvette at Benghazi"),
    ("MON 23 NOV", "Huang returns at Nvidia; Nasdaq leaps 6.5%"),
    ("MON 23 NOV", "NATO answers Poland incident with AWACS move"),
    ("TUE 24 NOV", "Seoul's Ulleung warning \u00b7 CAS rules on AFCON title"),
]

# (icon, kicker, headline, body, date, certainty)
LEADS = [
    ("chip", "MARKETS \u00b7 AMERICAS",
     "HUANG RETURNS: NVIDIA +31% IN A RECORD REBOUND",
     "Eleven days after resigning in scandal, Jensen Huang is reinstated as "
     "Nvidia's CEO after Trump's personal intervention. Nasdaq +6.5%, "
     "S&P 500 +4.7% \u2014 the rout breaks.",
     "MON 23 NOV", "R"),
    ("ship", "WAR \u00b7 EUROPE / AFRICA",
     "UKRAINE SINKS RUSSIAN CORVETTE IN LIBYA",
     "Kyiv says its sea drones sank a Russian corvette at Benghazi and posts "
     "the footage; Libya's army says the port is secure. The war reaches "
     "beyond Europe.",
     "MON 23 NOV", "C"),
    ("globe", "CLIMATE \u00b7 GLOBAL",
     "COP31 ENDS WITHOUT A DEAL \u2014 AND THE BLAME BEGINS",
     "Antalya talks close with no fossil-fuel agreement. Pacific nations "
     "voice despair, African negotiators confront the presidency, and "
     "Australia's minister faces calls to resign.",
     "MON 23 NOV", "R"),
]

# (no, region, headline, date, certainty)
CARDS = [
    (1, "EUROPE", "NATO sends an AWACS early-warning jet to Poland after "
     "three Russian Kh-101 missiles land there", "23 NOV", "R"),
    (2, "ASIA", "Candy-factory fire in Banten, Indonesia kills 24; rescuers "
     "still search for about 30 missing", "23\u201324 NOV", "D"),
    (3, "ASIA", "South Korea issues a brief evacuation warning for Ulleung "
     "Island as a Russian aircraft enters its airspace", "24 NOV", "R"),
    (4, "AFRICA \u00b7 SPORT", "CAS rules today on Senegal's appeal over the "
     "stripped AFCON 2025 title \u2014 Morocco waits", "24 NOV", "R"),
    (5, "MIDDLE EAST", "Iran flogs a singer and four of her production team "
     "\u2014 74 lashes each", "23 NOV", "R"),
    (6, "OCEANIA", "Wong warns US\u2013China rivalry and AI put Australia at "
     "risk; middle powers must band together", "23 NOV", "R"),
    (7, "AMERICAS \u00b7 TECH", "CrowdStrike to buy Zscaler in an all-stock "
     "deal valuing the firm at about $43.9 billion", "23 NOV", "R"),
    (8, "SOUTH ASIA", "Modi and Nepal's Shah flag off the Saryu-Kamala "
     "Express and talk energy, trade, links", "24 NOV", "R"),
    (9, "SPORT", "Alcaraz beats Zverev in Turin to win his first ATP Finals "
     "title", "23 NOV", "R"),
    (10, "SPORT", "World Chess Championship opens in Geneva: Gukesh defends "
     "his crown against Sindarov", "24 NOV", "R"),
]

ALSO = [
    "Russian cargo ship Sparta II afire in the Gulf of Finland after a drone strike",
    "Russian drones and missiles hit Kyiv region; homes in Dymer damaged, people missing",
    "Germany signs intent to use Kyiv's Delta battlefield system",
    "Murmansk governor detained on suspicion of embezzlement",
    "Thousands march in Lisbon against the rising cost of living",
    "Armenia proposes a new constitution to advance peace with Azerbaijan",
    "Israeli strikes kill at least three in Gaza, including an UNRWA worker",
    "Oxfam: Gaza's air, soil and water contaminated for decades",
    "US sanctions dozens tied to Iran's shadow-banking networks",
    "Iran vows to use \u201call its tools\u201d against the US naval blockade",
    "Trump orders Army to pause detonation of a toxic lead-azide stockpile in Iowa",
    "Bangladesh vows to arrest Sheikh Hasina if she returns from India",
    "China sets 2030 targets for elderly care and childcare",
    "Seoul nominates a new foreign minister and intelligence chief",
    "North Korea condemns Switzerland; may close its Pyongyang office",
    "Taliban order women's names off Balkh documents, replaced with \u201cBibi\u201d",
    "Kenya and DR Congo agree to restore full diplomatic ties",
    "African health leaders open CPHIA 2026 in Addis Ababa",
    "At least 24 civilians killed in South Sudan's Warrap State",
    "Zimbabwe preacher Uebert Angel arrested on assault allegations",
    "The Gambia's Barrow breaks his word and runs for a third term",
    "Verstappen wins the Las Vegas Grand Prix",
    "Wellington Test drawn \u2014 Pant's 128 a record for an Asian wicketkeeper",
    "Modi opens an AI centre at IIT Patna, launches a \u20b9400 crore research park",
    "India's oil and gas import bill jumped about 60% in October",
    "Pilots urge Delhi to step in over SpiceJet's unpaid salaries, grounded jets",
    "Ferrari unveils the 296 Challenge Stradale and 296 Challenge Evo in Spain",
    "Myanmar's military-backed government slams ASEAN's decision as unfair",
]

# (label, lon, lat) for the dot-grid pin map
PINS = [
    ("Benghazi", 20.1, 32.1), ("Antalya", 30.7, 36.9), ("Warsaw", 21.0, 52.2),
    ("Kyiv", 30.5, 50.4), ("Tehran", 51.4, 35.7), ("Gaza", 34.3, 31.5),
    ("Seoul", 127.0, 37.5), ("Banten", 106.1, -6.5), ("Delhi", 77.2, 28.6),
    ("Kathmandu", 85.3, 27.7), ("Nairobi", 36.8, -1.3), ("Bayelsa", 6.3, 4.9),
    ("Geneva", 6.1, 46.2), ("Turin", 7.7, 45.1), ("Las Vegas", -115.1, 36.2),
    ("New York", -74.0, 40.7), ("Canberra", 149.1, -35.3), ("Lisbon", -9.1, 38.7),
    ("Addis Ababa", 38.7, 9.0), ("Juba", 31.6, 4.9),
]

DATE_CHECK = [
    "MASTHEAD DATE: Tuesday 24 November 2026",
    "WEEKDAY VERIFIED: 24 Nov 2026 is a Tuesday",
    "EVERY STORY DATED 23\u201324 NOV 2026",
    "NO STORY OLDER THAN THE DAY'S CYCLE",
]

LEGEND = [
    ("\u25cf", "REPORTED \u2014 wire & major outlets"),
    ("\u25d0", "CLAIM \u2014 one side's account, counter-claim shown"),
    ("\u25d2", "DEVELOPING \u2014 counts still moving"),
]
