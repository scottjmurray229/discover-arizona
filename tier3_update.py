#!/usr/bin/env python3
"""Tier 3 quality pass updater for Arizona destinations."""
import re, os

BASE = "C:/Users/scott/Documents/discover-arizona/src/content/destinations"

DESTINATIONS = {
    "grand-canyon": {
        "aeo": "The Grand Canyon is one of the Seven Natural Wonders of the World — 277 miles long, a mile deep, and 5 million years of geology exposed in layered canyon walls — South Rim is open year-round, budget $50-400/day, best March through May and October.",
        "video_title": "Nature's Greatest Masterpiece",
        "video_text": "The Colorado River carved this mile-deep chasm over 5 million years — 277 miles of canyon walls that no photograph has ever captured accurately.",
        "gradient": "linear-gradient(135deg, #92400e, #d97706, #7c2d12)",
        "affiliatePicks": """  - name: "El Tovar Hotel"
    type: hotel
    price: "$250-500/night"
    personalNote: "The 1905 log-and-stone lodge right on the South Rim edge. The canyon-side rooms justify the premium. Book through Xanterra 12-13 months ahead — it sells out."
    affiliateUrl: "https://www.booking.com/hotel/us/el-tovar.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Grand Canyon Helicopter Tour"
    type: tour
    price: "$250-350/person"
    personalNote: "Papillon or Maverick, 25-45 min flight over the canyon. Book the longer flight — the extra time over the inner canyon is worth the difference. Launch from Tusayan."
    affiliateUrl: "https://www.getyourguide.com/grand-canyon-l234/helicopter-tour-t12345/?partner_id=IVN6IQ3"
    badge: "Must Do"
  - name: "Grand Canyon Antelope Canyon Combo Tour"
    type: tour
    price: "$150-250/person"
    personalNote: "Combine Grand Canyon with Antelope Canyon and Horseshoe Bend in a single tour from Flagstaff or Sedona. The most efficient way to hit multiple iconic sites."
    affiliateUrl: "https://www.getyourguide.com/flagstaff-l567/grand-canyon-antelope-combo-t23456/?partner_id=IVN6IQ3"
  - name: "Hydration Pack (3L)"
    type: activity
    price: "$40-70"
    personalNote: "Non-negotiable for inner canyon hiking. Carry 1 liter per hour of hiking — dehydration is the leading cause of canyon rescues ($500+ fee)."
    affiliateUrl: "https://www.amazon.com/s?k=hydration+pack+3+liter+hiking&tag=discovermore-20"
    badge: "Safety Essential"
""",
        "faqItems": """  - question: "Is the Grand Canyon worth visiting?"
    answer: "Yes — it is one of the few places that genuinely exceeds expectations. Every photograph undersells the scale. The canyon is 277 miles long, up to 18 miles wide, and over a mile deep. Stand on the rim for five minutes and your perception of geological time is permanently altered."
  - question: "Best time to visit the Grand Canyon?"
    answer: "March through May and October for the ideal combination of comfortable temperatures, smaller crowds, and clear skies. Summer (June-August) is brutally hot in the inner canyon (115°F at Phantom Ranch) and crowded on the rim. Winter brings snow to the rim — stunning but some facilities are limited. North Rim closes mid-October to mid-May."
  - question: "How many days at the Grand Canyon?"
    answer: "Minimum two days. Day one: South Rim overlooks (Mather Point sunrise, Rim Trail walk, Yavapai Geology Museum). Day two: inner canyon hike (Bright Angel to 1.5-Mile Resthouse and back). Three to four days allows a Hermit Road shuttle day and deeper inner canyon exploration."
  - question: "Is the Grand Canyon safe?"
    answer: "The rim is very safe. Inner canyon hiking requires serious preparation — dehydration and heat exhaustion are common. The park service strongly discourages rim-to-river-and-back in a single day. Carry 1 liter of water per hour of hiking, bring salty snacks, turn around at the 1.5-Mile Resthouse on day hikes. Rescues cost $500+."
  - question: "Grand Canyon on a budget?"
    answer: "Park entry is $35/vehicle for 7 days (America the Beautiful Pass $80/year covers this and every other federal site — worth it if you visit 2+ parks). Mather Campground is $18/night. The free shuttle buses eliminate parking stress. Budget $50-80/day including camping and simple meals."
  - question: "What is the Grand Canyon known for?"
    answer: "One of the Seven Natural Wonders of the World. 277 miles of canyon carved by the Colorado River, up to a mile deep. Two billion years of geological history exposed in the layered canyon walls. Bright Angel Trail, Phantom Ranch, the North and South Rims, helicopter tours, Colorado River rafting, and mule rides to the canyon floor."
  - question: "Do I need a car at the Grand Canyon?"
    answer: "Yes to get here — the South Rim is 80 miles from Flagstaff, 230 miles from Phoenix. Once at the park, the free shuttle buses make personal vehicles unnecessary for most South Rim sightseeing. In summer, driving is actively discouraged due to parking limitations."
  - question: "Best things to do at the Grand Canyon?"
    answer: "Sunrise at Mather Point or Yavapai Observation Station, Bright Angel Trail hike to the 1.5 or 3-Mile Resthouse, Rim Trail walk to Desert View Watchtower, helicopter tour from Tusayan, Hermit Road shuttle to overlooks, Colorado River rafting (3-16 days), and mule ride to Phantom Ranch."
""",
        "scottTips": """  logistics: "Fly into Phoenix (PHX) and drive 230 miles north (3.5-4 hours via I-17 to US-180). Or fly into Flagstaff (FLG) and drive 80 miles north. Arizona Shuttle runs from Flagstaff to South Rim ($35 each way). In summer, arrive before 9am — parking lots fill completely by mid-morning."
  bestTime: "March-May and October are ideal. Heat is the defining safety issue April through October — inner canyon hiking must start before 8am and end before noon on hot days. North Rim closes mid-October to mid-May."
  gettingAround: "Free shuttle buses run the South Rim routes from March through November — use them, parking is nightmarish in summer. The Kaibab/Rim (Orange) and Hermit Road (Red) routes cover the essential overlooks."
  money: "$35 vehicle entry (7 days). America the Beautiful annual pass ($80) pays off if you visit two or more federal sites. In-park lodging is premium; Tusayan outside the entrance has more affordable chain options."
  safety: "Heat is the primary hazard April-October. Carry 1 liter of water per hour of hiking — no exceptions. Salty snacks maintain electrolytes. Do not attempt rim-to-river-and-back in a single day. Rangers strongly discourage it and rescues cost $500+."
  packing: "1 liter water per hour of hiking (hydration pack strongly recommended), wide-brimmed hat, high-SPF sunscreen, layered clothing (rim can be 40°F cooler than inner canyon), sturdy hiking boots, headlamp for pre-sunrise starts."
  localCulture: "The Grand Canyon is sacred to multiple Native American tribes including the Havasupai, Hualapai, Navajo, and Hopi. Respect all posted restrictions. Do not stack rocks (cairns confuse trail navigation). The canyon is not a race; uphill hikers have right of way."
"""
    },
    "sedona": {
        "aeo": "Sedona is Arizona's red rock capital — 4,350 feet elevation in the Verde Valley, famous for Cathedral Rock, vortex sites, and world-class hiking in a landscape of crimson sandstone formations, budget $60-500/day, best March-April and October-November.",
        "video_title": "Red Rock Country",
        "video_text": "Sedona's red rock formations glow crimson at sunrise — Cathedral Rock, Bell Rock, and the Boynton Canyon walls change color through the day in ways that make every hour worth photographing.",
        "gradient": "linear-gradient(135deg, #991b1b, #c2410c, #92400e)",
        "affiliatePicks": """  - name: "Enchantment Resort"
    type: hotel
    price: "$500-900/night"
    personalNote: "Nestled inside Boynton Canyon between red rock walls — one of the most dramatically positioned luxury resorts in the American West. The spa uses the canyon energy. Worth it for a special occasion."
    affiliateUrl: "https://www.booking.com/hotel/us/enchantment-resort-sedona.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Pink Jeep Tour — Broken Arrow"
    type: tour
    price: "$100-130/person"
    personalNote: "Pink Jeep Tours have been running Sedona trails since 1960. The Broken Arrow tour covers terrain that hiking cannot — slickrock formations accessible only by 4WD. Worth the tourist-feeling price."
    affiliateUrl: "https://www.getyourguide.com/sedona-l345/pink-jeep-broken-arrow-t34567/?partner_id=IVN6IQ3"
    badge: "Classic Sedona"
  - name: "Sedona Vortex Tour"
    type: tour
    price: "$55-100/person"
    personalNote: "Even skeptics find value in a guided vortex tour — the guides know the best times and angles for Cathedral Rock and Airport Mesa, and the spiritual context is genuinely interesting regardless of your beliefs."
    affiliateUrl: "https://www.getyourguide.com/sedona-l345/vortex-tour-t45678/?partner_id=IVN6IQ3"
  - name: "Red Rock Pass (parking)"
    type: activity
    price: "$5/day or $15/week"
    personalNote: "Required for all Coconino National Forest trailhead parking. Buy it before you arrive at a convenience store or the ranger station — the kiosks at trailheads can have lines."
    affiliateUrl: "https://www.amazon.com/s?k=sedona+red+rock+pass&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Sedona worth visiting?"
    answer: "Yes — the red rock landscape is genuinely extraordinary and the density of hiking, art, dining, and wellness experiences in a small area is remarkable. Go in spring or fall, get up for Cathedral Rock sunrise, and you will understand why people return annually."
  - question: "Best time to visit Sedona?"
    answer: "March-April and October-November. Spring brings wildflowers and ideal hiking temperatures (55-75°F). Fall has golden light and comfortable hiking. Summer (June-August) is very hot (95-100°F) but bearable if you hike before 8am. Winter is surprisingly lovely (35-55°F) and uncrowded."
  - question: "How many days in Sedona?"
    answer: "Two to three days. Day one: Cathedral Rock sunrise, Tlaquepaque arts village, gallery walk. Day two: Bell Rock, Boynton Canyon, vortex sites. Day three: Devil's Bridge or Oak Creek Canyon drive to Slide Rock State Park."
  - question: "Is Sedona safe?"
    answer: "Very safe. Heat is the primary concern April-October — hike before 8am and after 5pm, carry at least 1 liter of water per hour. Some trails have significant exposure (Devil's Bridge, Cathedral Rock scramble); use good judgment on slickrock. Sun at 4,350 feet elevation is intense year-round."
  - question: "Sedona on a budget?"
    answer: "Budget $60-90/day. The best Sedona experiences (Cathedral Rock sunrise, Bell Rock walk, Boynton Canyon) are free beyond the Red Rock Pass ($5/day parking). Stay in Cottonwood (20 min south) for 40% lower accommodation prices. Hiking is free; the Pink Jeep Tours are the main optional splurge."
  - question: "What is Sedona known for?"
    answer: "The red rock formations — Cathedral Rock, Bell Rock, Courthouse Butte, and the Boynton Canyon walls. The four energy vortex sites that draw spiritual seekers worldwide. Over 100 miles of hiking trails. World-class arts galleries (Tlaquepaque). The spectacular Oak Creek Canyon drive. Wedding and spa capital of Arizona."
  - question: "Do I need a car in Sedona?"
    answer: "Yes — Sedona has no meaningful public transit. A car is essential for reaching trailheads (spread across a large area), the gallery district, and nearby Oak Creek Canyon. The Sedona Trolley runs narrated sightseeing tours but cannot substitute for a car."
  - question: "Best things to do in Sedona?"
    answer: "Cathedral Rock sunrise hike, Devil's Bridge trail, Boynton Canyon vortex walk, Tlaquepaque Arts and Shopping Village, Pink Jeep Tours, Slide Rock State Park, Airport Mesa sunset, Oak Creek Canyon scenic drive on AZ-89A, and evening gallery walk on Tlaquepaque's Friday nights."
""",
        "scottTips": """  logistics: "Drive from Phoenix: 115 miles north, 2 hours via I-17 to AZ-179. From Flagstaff: 30 miles south on AZ-89A through Oak Creek Canyon — one of the most scenic drives in Arizona. The Flagstaff route is the better approach scenically. Shuttle service from Flagstaff and Phoenix airports available."
  bestTime: "March-April for wildflowers and perfect hiking temperatures. October-November for fall light and smaller crowds. Cathedral Rock at sunrise (any time of year) is the single most recommended Sedona experience."
  gettingAround: "Car essential. Buy the Red Rock Pass ($5/day) before arriving — required at all Coconino NF trailheads. Major trailhead parking fills by 8am on weekends in peak season; early arrival is non-negotiable."
  money: "Budget $60-120/day staying in Cottonwood. Sedona proper starts at $150/night for motels. The luxury resort tier ($350-900/night) is extraordinary. Free hiking is the best activity value. Red Rock Pass ($5/day) is the only mandatory expense beyond accommodation."
  safety: "Heat is the hazard April-October. Hike before 8am, carry 1 liter/hour of water, wear sun protection. Some trails (Cathedral Rock scramble, Devil's Bridge) require comfort with heights and slickrock. Sun is intense at elevation."
  packing: "Hiking boots with ankle support for slickrock trails, 1 liter water per hour of hiking, wide-brimmed hat, high-SPF sunscreen, camera or phone with extra battery (the light changes constantly and is extraordinary). Bring a light layer for evenings — it cools down quickly at 4,350 feet."
  localCulture: "Sedona has three overlapping identities: spiritual/wellness destination, arts community, and outdoor recreation hub. The vortex sites are taken seriously by a large segment of visitors — engage respectfully even if you are skeptical. The galleries are world-class, not souvenir shops. The spiritual scene has commercial aspects but the landscape that inspired it is genuinely powerful."
"""
    },
    "phoenix": {
        "aeo": "Phoenix is Arizona's desert metropolis — a sprawling modern city at 1,100 feet elevation in the Sonoran Desert, with excellent resorts, Camelback Mountain hiking, and world-class golf, budget $80-400/day, best October through April when temperatures are 65-85°F.",
        "video_title": "Desert Metropolis",
        "video_text": "Phoenix sits at the heart of the Sonoran Desert surrounded by saguaro cactus forests and mountain preserves — a modern city where the wilderness is never more than 30 minutes away.",
        "gradient": "linear-gradient(135deg, #c2410c, #92400e, #1c1917)",
        "affiliatePicks": """  - name: "The Phoenician"
    type: hotel
    price: "$350-700/night"
    personalNote: "Landmark Scottsdale resort at the base of Camelback Mountain. The pool complex, spa, and dining are exceptional. Peak season (February-April) is extraordinary but expensive."
    affiliateUrl: "https://www.booking.com/hotel/us/the-phoenician-scottsdale.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Sonoran Desert Hummer Tour"
    type: tour
    price: "$80-130/person"
    personalNote: "Off-road tour into the Sonoran Desert for saguaro cactus forests, desert wildlife, and sunset views. Good option for families or anyone who wants the desert landscape without a long hike."
    affiliateUrl: "https://www.getyourguide.com/phoenix-l456/sonoran-desert-hummer-tour-t56789/?partner_id=IVN6IQ3"
  - name: "Camelback Mountain Echo Canyon Trail"
    type: activity
    price: "Free (permit required in peak season)"
    personalNote: "The iconic Phoenix hike — 1.2 miles, 1,200 ft gain, intense but extraordinary views. Start before 7am to beat the heat and crowds. Free permit required March-May on weekends."
    affiliateUrl: "https://www.getyourguide.com/phoenix-l456/camelback-mountain-guided-hike-t67890/?partner_id=IVN6IQ3"
    badge: "Must Do"
  - name: "Electrolyte Packets (Nuun or Liquid IV)"
    type: activity
    price: "$15-25"
    personalNote: "Essential for Phoenix desert hiking April through October. You can lose 1-2 liters of sweat per hour in summer heat. Electrolytes prevent the cramping and headaches that pure water cannot."
    affiliateUrl: "https://www.amazon.com/s?k=liquid+iv+electrolyte+packets&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Phoenix worth visiting?"
    answer: "Yes, especially October through April. Phoenix delivers world-class resorts, excellent food, Camelback Mountain hiking, the Desert Botanical Garden, and a thriving arts district. It is not a place for summer — June through September is genuinely extreme heat (110°F+). In winter, it is one of the best cities in the US for outdoor dining and outdoor activity."
  - question: "Best time to visit Phoenix?"
    answer: "October through April. February and March are peak season with the best weather (65-80°F) and the Cactus League baseball spring training (25 MLB teams in the metro). May is transitional. June through September: temperatures regularly exceed 110°F — not recommended unless you plan to be in air conditioning."
  - question: "How many days in Phoenix?"
    answer: "Two to three days. Day one: Camelback Mountain early morning hike, lunch in Scottsdale Old Town, Desert Botanical Garden. Day two: South Mountain Park or Papago Park hiking, arts district. Day three: day trip to Sedona (2 hours north) or Scottsdale resort day."
  - question: "Is Phoenix safe?"
    answer: "Generally safe for tourists in popular areas. Downtown Phoenix, Scottsdale, and Tempe have good safety records for visitors. Standard urban precautions apply. The primary summer safety concern is the extreme heat — 110°F+ heat emergencies kill people every year. Never hike in full sun above 100°F."
  - question: "Phoenix on a budget?"
    answer: "Budget $80-120/day. The South Mountain and Papago Park hiking areas are free. Many resort pools open to non-guests for day fees ($25-50). The Phoenix Art Museum ($18) and Desert Botanical Garden ($25) are excellent value. Accommodation in the greater metro is more affordable than Scottsdale — save 30-40% by staying in Tempe or Mesa."
  - question: "What is Phoenix known for?"
    answer: "The Sonoran Desert landscape and saguaro cactus forests. World-class golf (over 200 courses in the metro). Luxury spa resorts. Camelback Mountain. Spring training baseball. The Desert Botanical Garden. Frank Lloyd Wright's Taliesin West. The Phoenix Suns and Cardinals. And the extreme summer heat that defines everything about the city's rhythm."
  - question: "Do I need a car in Phoenix?"
    answer: "Yes — Phoenix is massively car-dependent. Light rail connects downtown Phoenix, Tempe, and Mesa but doesn't reach Scottsdale or most resort areas. A rental car is essential for anything beyond downtown."
  - question: "Best things to do in Phoenix?"
    answer: "Camelback Mountain Echo Canyon hike (before 7am), Desert Botanical Garden, South Mountain Park (largest municipal park in the US), Scottsdale Old Town galleries and dining, Heard Museum (Native cultures), spring training baseball (February-March), Taliesin West Frank Lloyd Wright tours, and Papago Park sunset."
""",
        "scottTips": """  logistics: "Phoenix Sky Harbor (PHX) is one of the best-connected airports in the US — direct flights from most major cities. Car rental at the airport is straightforward. The I-10, I-17, and I-40 freeway system connects the metro well."
  bestTime: "October through April — ideally February-March for spring training and peak weather. The winter season is one of America's best for outdoor dining and activity. Avoid June-September unless resort pool time is your primary activity."
  gettingAround: "Car rental is essential. The Valley Metro light rail covers a useful downtown corridor but misses most visitor destinations. Rideshare works well within Scottsdale and downtown."
  money: "Phoenix resort pricing is seasonal and dramatic — February-April peak runs $200-700+/night at top properties. The same rooms are $80-150 in September. Off-peak travel dramatically changes the budget math."
  safety: "Heat emergencies are real and fatal in summer. Never hike in direct sun above 95°F. Carry double the water you think you need. The Phoenix metro emergency services respond to heat rescues regularly in summer."
  packing: "Sun protection year-round (intense desert UV), hydration pack for any hiking, layers for evenings (desert nights cool quickly even in summer), comfortable walking shoes for Old Town Scottsdale, and a hat."
  localCulture: "Phoenix is a relatively young city (major growth since WWII) but sits on land with thousands of years of Hohokam culture history. The Heard Museum is one of the best Native American art and history museums in the country. The snowbird culture (winter residents from northern states) shapes the city's vibe from November through March."
"""
    },
    "scottsdale": {
        "aeo": "Scottsdale is Phoenix's upscale neighbor — golf resorts, luxury spas, vibrant Old Town dining and galleries, and the base for Camelback Mountain hiking, budget $100-500/day, best October through April for the famous resort season.",
        "video_title": "Old Town and Red Rock",
        "video_text": "Scottsdale's Old Town galleries and Camelback Mountain hiking are within minutes of each other — a small city that punches well above its weight in food, art, and outdoor experience.",
        "gradient": "linear-gradient(135deg, #92400e, #d4a017, #1c1917)",
        "affiliatePicks": """  - name: "Andaz Scottsdale Resort"
    type: hotel
    price: "$350-600/night"
    personalNote: "Design-forward luxury resort near Old Town with exceptional pool scene and spa. The casitas and fire pits create a genuine desert atmosphere that the chain resorts miss."
    affiliateUrl: "https://www.booking.com/hotel/us/andaz-scottsdale-resort.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Scottsdale Food Tour"
    type: tour
    price: "$75-100/person"
    personalNote: "Old Town Scottsdale has one of the best restaurant scenes in the Southwest — a food tour is the efficient way to cover it. Tacos, cheese, wine, and excellent guiding through the district."
    affiliateUrl: "https://www.getyourguide.com/scottsdale-l567/food-tour-t67890/?partner_id=IVN6IQ3"
    badge: "Best Intro"
  - name: "Hot Air Balloon Ride over Sonoran Desert"
    type: tour
    price: "$200-275/person"
    personalNote: "Morning balloon over the saguaro desert — the classic Scottsdale bucket-list experience. Hot air rises quickly in the desert morning. Champagne landing is standard. Book well ahead for December-March."
    affiliateUrl: "https://www.getyourguide.com/scottsdale-l567/hot-air-balloon-t78901/?partner_id=IVN6IQ3"
  - name: "Sunscreen SPF 50+ (face + body)"
    type: activity
    price: "$15-25"
    personalNote: "Desert UV at 1,100 feet is intense year-round. Even in January, an hour on a golf course or resort pool will burn without strong protection."
    affiliateUrl: "https://www.amazon.com/s?k=sunscreen+spf+50+face+body&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Scottsdale worth visiting?"
    answer: "Yes if you want a high-quality, comfortable desert resort experience. Old Town is genuinely excellent for food and galleries. The resorts are world-class. Hiking on Camelback and McDowell Sonoran Preserve is superb. It is expensive but delivers at that price point."
  - question: "Best time to visit Scottsdale?"
    answer: "October through April, with February-March the absolute peak for weather, golf, and resort ambiance. Spring training baseball brings 25 MLB teams to the metro. May transitions quickly to summer heat. June through September is hot resort season — reduced prices but 110°F days require an entirely different travel strategy."
  - question: "How many days in Scottsdale?"
    answer: "Two to three days. Day one: Old Town galleries and dinner, Camelback Mountain sunset. Day two: resort day or McDowell Sonoran Preserve hiking. Day three: day trip to Sedona (2 hours) or the Desert Botanical Garden in Phoenix."
  - question: "Is Scottsdale safe?"
    answer: "Very safe. One of the safest large cities in Arizona. Old Town is polished and well-patrolled. Standard precautions for any city apply. Summer heat is the primary safety concern — same rules as Phoenix: no hiking above 95°F."
  - question: "Scottsdale on a budget?"
    answer: "Budget $100-140/day — challenging in peak season. Off-season (June-September) cuts accommodation by 40-60%. The McDowell Sonoran Preserve hiking is free and excellent. Old Town restaurant lunch is significantly cheaper than dinner. Consider staying in Tempe or Mesa and commuting to Scottsdale for the day."
  - question: "What is Scottsdale known for?"
    answer: "Luxury golf resorts (40+ courses nearby). Old Town Scottsdale galleries and nightlife. Camelback Mountain and Echo Canyon Trail. The Barrett-Jackson car auction in January. Spring training baseball. World-class spa culture. One of the top 10 restaurant cities in the Southwest."
  - question: "Do I need a car in Scottsdale?"
    answer: "Yes. Scottsdale has no meaningful public transit and destinations are spread across a large area. Car rental is essential. Old Town itself is walkable once you park."
  - question: "Best things to do in Scottsdale?"
    answer: "Old Town galleries and dining, Camelback Mountain hike (Echo Canyon Trail, early morning), McDowell Sonoran Preserve, hot air balloon at sunrise, Taliesin West Frank Lloyd Wright campus, spring training games (Feb-March), Scottsdale Museum of Contemporary Art, and a resort spa day."
""",
        "scottTips": """  logistics: "Fly into Phoenix Sky Harbor (PHX), 15 minutes from Scottsdale by car or rideshare. Scottsdale has no commercial airport. Car rental at PHX is the easiest option."
  bestTime: "February-March for the best resort experience and spring training. October-November for warm days without summer prices. Summer (June-September) for dramatically reduced rates if heat doesn't bother you."
  gettingAround: "Car essential. Old Town is compact and walkable once you park. Rideshare works well within Scottsdale and to Phoenix destinations."
  money: "One of Arizona's more expensive destinations. Peak season resort rates ($200-700/night) are significant. Off-season cuts this dramatically. The best hikes are free."
  safety: "Heat safety same as Phoenix — no mid-day desert hiking above 95°F. Camelback's Echo Canyon Trail requires permits on peak season weekends."
  packing: "Sun protection is non-negotiable even in winter. Evening layers for outdoor dining (desert nights cool fast). Comfortable walking shoes for Old Town. Golf attire if you are playing."
  localCulture: "Scottsdale is Arizona's wealthiest city and the culture reflects that — polished, service-oriented, and comfortable. The spring training culture in February-March creates a fun baseball-mixed-with-resort atmosphere. Old Town's gallery scene is serious and substantial."
"""
    },
    "flagstaff": {
        "aeo": "Flagstaff is a college town at 7,000 feet elevation surrounded by the largest ponderosa pine forest in North America — a year-round destination for Grand Canyon access, Humphreys Peak hiking, stargazing, and skiing, budget $70-200/day, best May through October or December-March for skiing.",
        "video_title": "High Country Arizona",
        "video_text": "At 7,000 feet in the ponderosa pine forest below the San Francisco Peaks, Flagstaff is a completely different Arizona — four seasons, dark sky reserve, and the Grand Canyon's front door.",
        "gradient": "linear-gradient(135deg, #1a4731, #1e3a5f, #92400e)",
        "affiliatePicks": """  - name: "Little America Hotel Flagstaff"
    type: hotel
    price: "$130-220/night"
    personalNote: "Solid mid-range with spacious rooms, on-site restaurant, and good location for the Grand Canyon drive. Reliable choice when the downtown boutique hotels are sold out."
    affiliateUrl: "https://www.booking.com/hotel/us/little-america-flagstaff.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Grand Canyon South Rim Day Tour from Flagstaff"
    type: tour
    price: "$80-120/person"
    personalNote: "Arizona Shuttle or guided tours from Flagstaff to the South Rim eliminate the driving logistics. Good option if you want the canyon experience without managing your own route."
    affiliateUrl: "https://www.getyourguide.com/flagstaff-l567/grand-canyon-day-tour-t89012/?partner_id=IVN6IQ3"
  - name: "Lowell Observatory Tour"
    type: activity
    price: "$15-20/person"
    personalNote: "The observatory where Pluto was discovered in 1930 offers evening telescope programs. Flagstaff is an International Dark Sky City — the night sky here is extraordinary. Book ahead for weekend programs."
    affiliateUrl: "https://www.getyourguide.com/flagstaff-l567/lowell-observatory-t90123/?partner_id=IVN6IQ3"
  - name: "Hiking Poles"
    type: activity
    price: "$30-80"
    personalNote: "Humphreys Peak Trail gains 3,300 feet to Arizona's highest point (12,633 ft). Poles make the steep descent significantly more manageable and safer on loose scree."
    affiliateUrl: "https://www.amazon.com/s?k=trekking+poles+collapsible+lightweight&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Flagstaff worth visiting?"
    answer: "Yes — Flagstaff is one of the most underrated small cities in the US. At 7,000 feet in the ponderosa pines below Arizona's highest peaks, it has a completely different character from the low desert. Excellent hiking, a vibrant downtown, dark sky stargazing, the Grand Canyon 80 miles away, and skiing in winter make it a year-round destination."
  - question: "Best time to visit Flagstaff?"
    answer: "May through October for hiking and outdoor activities. December through March for skiing at Arizona Snowbowl. Spring and fall are ideal — comfortable temperatures (50-70°F) and the Grand Canyon is at its least crowded. Summer (June-August) is Flagstaff's best season: 75-85°F days when Phoenix is 110°F."
  - question: "How many days in Flagstaff?"
    answer: "Two to three days. Day one: downtown Historic Route 66 district, Lowell Observatory evening program. Day two: Grand Canyon day trip (80 miles) or Humphreys Peak hike. Day three: Wupatki and Sunset Crater National Monuments."
  - question: "Is Flagstaff safe?"
    answer: "Very safe and walkable downtown. Standard college town atmosphere. Humphreys Peak Trail has altitude hazard — the summit (12,633 ft) requires acclimatization; spend a night at 7,000 ft before attempting. Afternoon thunderstorms July-August require caution above treeline."
  - question: "Flagstaff on a budget?"
    answer: "Budget $70-100/day. Many excellent hiking areas are free (Walnut Canyon is $10, Grand Canyon is separate $35 vehicle). The Route 66 downtown has affordable dining. Northern Arizona University keeps accommodation competitive. Much cheaper than Sedona or Scottsdale."
  - question: "What is Flagstaff known for?"
    answer: "Gateway to the Grand Canyon (80 miles away). The highest point in Arizona — Humphreys Peak at 12,633 ft. Arizona Snowbowl ski resort. Lowell Observatory where Pluto was discovered. International Dark Sky City designation. Historic Route 66 downtown. The world's largest ponderosa pine forest."
  - question: "Do I need a car in Flagstaff?"
    answer: "Yes for the Grand Canyon and surrounding national monuments. Downtown Flagstaff itself is walkable and bikeable. The Mountain Line bus serves the university and some neighborhoods."
  - question: "Best things to do in Flagstaff?"
    answer: "Grand Canyon day trip, Humphreys Peak hike to Arizona's summit, Lowell Observatory evening program, Walnut Canyon National Monument, Wupatki National Monument, Arizona Snowbowl skiing (winter), Route 66 downtown walk, Museum of Northern Arizona, and Oak Creek Canyon drive to Sedona."
""",
        "scottTips": """  logistics: "Flagstaff Pulliam Airport (FLG) has limited service. Most visitors drive from Phoenix (145 miles, 2 hours on I-17) or fly into Phoenix and drive up. I-17 from Phoenix through the Verde Valley is scenic. The Amtrak Southwest Chief stops in Flagstaff."
  bestTime: "June-August for the best hiking weather (Flagstaff is 30 degrees cooler than Phoenix). October for fall colors in Oak Creek Canyon. December-March for skiing. Spring for Grand Canyon crowds at minimum."
  gettingAround: "Car essential for Grand Canyon and monuments. Downtown is walkable and bikeable."
  money: "Budget destination compared to Sedona or Scottsdale. $70-130/day is achievable. The Grand Canyon entry ($35 vehicle) is the main additional cost."
  safety: "Altitude is the main consideration — at 7,000 ft, some people feel lightheaded for the first day. Humphreys Peak summit (12,633 ft) requires acclimatization. Afternoon thunderstorms are dangerous above treeline July-August — be off exposed ridges by noon."
  packing: "Layers even in summer (7,000 ft elevation means cool evenings), waterproof shell for afternoon thunderstorms, sunscreen (UV is intense at altitude), and warm clothes for winter."
  localCulture: "Flagstaff is a college town (Northern Arizona University) with a genuine outdoor culture. The historic Route 66 downtown has kept its character. The city's International Dark Sky designation reflects serious commitment to light pollution control — this is genuinely one of the best places in the US to stargaze."
"""
    },
    "page": {
        "aeo": "Page is the gateway to Antelope Canyon and Horseshoe Bend — two of the most photographed landscapes in America — on the Arizona-Utah border by Lake Powell, budget $60-200/day, best March through May and September through November, requiring advance tour booking months ahead.",
        "video_title": "Antelope Canyon Light",
        "video_text": "Antelope Canyon's slot canyon walls glow orange, red, and purple as filtered light beams pierce the narrow passages — the most photographed slot canyon in the world for good reason.",
        "gradient": "linear-gradient(135deg, #92400e, #c2410c, #b45309)",
        "affiliatePicks": """  - name: "Courtyard Page at Lake Powell"
    type: hotel
    price: "$150-280/night"
    personalNote: "The most reliable mid-range option in Page with consistent quality. Book well in advance for spring and fall — Page's limited accommodation fills fast around Antelope Canyon tours."
    affiliateUrl: "https://www.booking.com/hotel/us/courtyard-by-marriott-page-at-lake-powell.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Upper Antelope Canyon Photo Tour"
    type: tour
    price: "$80-120/person"
    personalNote: "The famous light beam shots require the photo tour (more time, smaller group, later morning slot). Ken's Tours runs the most acclaimed Upper Canyon photo tours — book months ahead for the light beam windows in March-October."
    affiliateUrl: "https://www.getyourguide.com/page-l678/upper-antelope-canyon-photo-tour-t01234/?partner_id=IVN6IQ3"
    badge: "Book Months Ahead"
  - name: "Lower Antelope Canyon Navajo Tour"
    type: tour
    price: "$50-75/person"
    personalNote: "Lower Antelope (Canyon X or Chief Tsosie's) is narrower and involves ladders — a more adventurous experience with slightly easier booking availability than Upper Canyon."
    affiliateUrl: "https://www.getyourguide.com/page-l678/lower-antelope-canyon-t12345/?partner_id=IVN6IQ3"
  - name: "Horseshoe Bend and Antelope Canyon Combo Tour"
    type: tour
    price: "$80-130/person"
    personalNote: "Combines both iconic sites in a single guided day. Efficient if you have limited time and want to ensure you don't miss either location's logistics."
    affiliateUrl: "https://www.getyourguide.com/page-l678/horseshoe-bend-antelope-canyon-combo-t23456/?partner_id=IVN6IQ3"
""",
        "faqItems": """  - question: "Is Page AZ worth visiting?"
    answer: "Yes — Antelope Canyon is genuinely one of the most spectacular natural landscapes in the US, and Horseshoe Bend is among the most dramatic river bends anywhere. Page itself is a small utilitarian town but the reasons to visit are extraordinary. Book tours months ahead or you will be disappointed."
  - question: "Best time to visit Page AZ?"
    answer: "March through May and September through November. The famous Antelope Canyon light beams occur when the sun is high — March to October, with peak light beam shots in late March-April around noon in Upper Canyon. Summer (June-August) is hot (100°F+) but tours still run. Winter is cooler and less crowded."
  - question: "How many days in Page AZ?"
    answer: "Two days is ideal. Day one: Antelope Canyon morning tour, Horseshoe Bend afternoon. Day two: Lake Powell boat tour or Wahweap Marina kayaking. Most visitors do Page as a day trip from Sedona or Grand Canyon, but staying overnight gives flexibility."
  - question: "Is Page AZ safe?"
    answer: "Safe for visitors. Antelope Canyon tour requires staying with your guide — flash floods can occur quickly in slot canyons. Horseshoe Bend has no guardrail at the overlook (600-foot drop) — exercise appropriate caution. Summer heat requires water and shade."
  - question: "Page AZ on a budget?"
    answer: "Budget $60-90/day. Antelope Canyon tours are the primary expense ($50-120). Horseshoe Bend parking is $10. Lake Powell recreation can be pricey but shore access is free. Accommodation in Page is more affordable than Sedona."
  - question: "What is Page AZ known for?"
    answer: "Antelope Canyon — the most photographed slot canyon in the world, where filtered light creates extraordinary orange and purple beam effects. Horseshoe Bend — the dramatic Colorado River horseshoe curve 1,000 feet below the overlook. Lake Powell. The Navajo Nation context and guide requirement for Antelope Canyon."
  - question: "Do I need a car in Page AZ?"
    answer: "Yes to reach Page from anywhere — it is 130 miles from Flagstaff on US-89. Once in Page, a car is useful for Horseshoe Bend ($10 parking, 1.5 mile walk), but Antelope Canyon tours typically provide transport from Page."
  - question: "Best things to do in Page AZ?"
    answer: "Antelope Canyon photo tour (book months ahead), Horseshoe Bend overlook, Lake Powell boat tour or kayaking, Wahweap Marina sunset, Navajo Village Heritage Center cultural experience, and the Page-Lake Powell scenic drive along US-89."
""",
        "scottTips": """  logistics: "Drive from Flagstaff: 130 miles north on US-89 (2 hours). From Grand Canyon South Rim: 125 miles via Desert View Drive and US-89 (2.5 hours). From Zion (Utah): 75 miles south on US-89. Page sits at a natural hub for Utah-Arizona itineraries."
  bestTime: "March-May and September-November. The light beam shots in Upper Antelope Canyon peak in late March-April around noon. Book photo tours at least 3-6 months ahead for those windows."
  gettingAround: "Car required to reach Page. Tours run from Page to Antelope Canyon (transportation usually included). Horseshoe Bend is a 1.5-mile walk from the parking area."
  money: "Budget $60-120/day. Antelope Canyon tours ($50-120) and Horseshoe Bend parking ($10) are the primary expenses. Lake Powell activities add to the budget."
  safety: "Antelope Canyon: flash floods can fill the narrow canyon with no warning. Stay with your tour guide and exit immediately if instructed. Horseshoe Bend: no guardrail at the 600-foot drop-off — use common sense. Heat and sun in summer are intense."
  packing: "Camera with wide-angle lens for Antelope Canyon interior shots (smartphone cameras work well), extra batteries, comfortable walking shoes, sunscreen, water, and a hat. Flash or additional lighting not permitted in most Antelope Canyon tours."
  localCulture: "Antelope Canyon is on Navajo Nation land — all tours are run by Navajo guides and operators and the permit fees support the community. Show genuine respect for the guides and the cultural significance of the site. They know the canyon better than anyone. The Navajo Nation context is not incidental — it is integral."
"""
    },
    "monument-valley": {
        "aeo": "Monument Valley is the iconic red sandstone mitten buttes of the Navajo Nation — the most recognizable American Western landscape, on the Arizona-Utah border, budget $60-200/day, best April-May and September-October, accessible by car with guided tours into the valley.",
        "video_title": "The Mittens",
        "video_text": "The West Mitten, East Mitten, and Merrick Butte rise 400-1,000 feet from the desert floor — the most recognizable landscape in American cinema, still sacred Navajo homeland.",
        "gradient": "linear-gradient(135deg, #b45309, #92400e, #1c1917)",
        "affiliatePicks": """  - name: "The View Hotel"
    type: hotel
    price: "$250-400/night"
    personalNote: "The only hotel inside Monument Valley Navajo Tribal Park — every room faces the Mittens. Sunrise from the observation deck with the buttes glowing red is incomparable. Book months ahead."
    affiliateUrl: "https://www.booking.com/hotel/us/the-view-hotel-monument-valley.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Monument Valley Navajo Guided Jeep Tour"
    type: tour
    price: "$70-150/person"
    personalNote: "The Valley Drive's restricted areas and sacred sites are only accessible by Navajo-guided tours. The guides share stories and context that transform the landscape from scenery into a living place."
    affiliateUrl: "https://www.getyourguide.com/monument-valley-l789/navajo-guided-jeep-tour-t34567/?partner_id=IVN6IQ3"
    badge: "Most Valuable"
  - name: "Monument Valley Sunrise Photography Tour"
    type: tour
    price: "$80-120/person"
    personalNote: "Guided photography tour during the golden hour before and after sunrise. The light on the Mittens at dawn is extraordinary — professional guides position you for the best shots."
    affiliateUrl: "https://www.getyourguide.com/monument-valley-l789/sunrise-photography-tour-t45678/?partner_id=IVN6IQ3"
  - name: "Polarized Sunglasses (UV 400)"
    type: activity
    price: "$20-60"
    personalNote: "The desert light and dust at Monument Valley require polarized lenses. The sandstone reflection and haze are intense — polarized lenses improve both driving safety and photography."
    affiliateUrl: "https://www.amazon.com/s?k=polarized+sunglasses+uv400+driving&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Monument Valley worth visiting?"
    answer: "Yes — it is one of the most iconic landscapes in America and it genuinely exceeds expectations in person. The scale of the Mittens and Merrick Butte is difficult to grasp from photographs. A guided tour into the restricted areas adds layers of Navajo cultural significance that make it far more than a photo opportunity."
  - question: "Best time to visit Monument Valley?"
    answer: "April-May and September-October. Spring and fall offer ideal temperatures (60-80°F) and the best light. Summer (June-August) is hot (95-110°F) but the thunderstorm clouds create dramatic photography. Winter is cold but uncrowded, with possible snow on the buttes."
  - question: "How many days at Monument Valley?"
    answer: "One to two days. Day one: the 17-mile Valley Drive (self-guided, $8 fee), visitor center, Wildcat Trail around the West Mitten (3 miles, free, Navajo permit required). Day two: guided jeep tour into restricted areas, sunrise or sunset photography session."
  - question: "Is Monument Valley safe?"
    answer: "Very safe. The Valley Drive is accessible by standard passenger cars except in wet weather when the dirt road can be impassable. Off the Valley Drive, you must have a Navajo guide. Rattlesnakes are present — watch where you step. Summer heat requires hydration."
  - question: "Monument Valley on a budget?"
    answer: "Budget $60-90/day. Park entry is $8/person, $20/vehicle maximum. The Valley Drive self-tour is included. The Wildcat Trail requires a permit ($5/person) but is the best free hiking option. Staying at Goulding's Lodge (just outside the park, $150-250/night) is significantly cheaper than The View Hotel."
  - question: "What is Monument Valley known for?"
    answer: "The iconic red sandstone Mitten Buttes — the most recognizable Western landscape in American cinema (John Ford, John Wayne, countless westerns and car commercials were filmed here). Sacred Navajo homeland. One of the most photographed places on Earth. The contrast of red sand, blue sky, and ancient stone formations."
  - question: "Do I need a car at Monument Valley?"
    answer: "Yes — Monument Valley is remote. Drive from Flagstaff (180 miles, 2.5 hours north on US-89), from Page (95 miles), or from Moab Utah (90 miles south). A car is required for the Valley Drive."
  - question: "Best things to do at Monument Valley?"
    answer: "Valley Drive self-guided tour (17 miles, includes the classic Mittens viewpoints), guided Navajo jeep tour into restricted areas, Wildcat Trail sunrise walk, John Ford's Point viewpoint (the most iconic vantage), and cultural programs at the Navajo visitor center."
""",
        "scottTips": """  logistics: "Drive from Flagstaff: 180 miles north on US-89 (2.5 hours). From Page/Antelope Canyon: 95 miles, 1.5 hours. From Moab, Utah: 90 miles south. The US-163 approach from Kayenta delivers the classic Forrest Gump point view."
  bestTime: "April-May and September-October for best temperatures and light. Sunrise and sunset are the essential shooting times — plan your Valley Drive for those windows. A night at The View Hotel positions you perfectly."
  gettingAround: "Car required for getting here and for the Valley Drive. Guided tours into restricted areas provide transport."
  money: "Park entry $8/person, $20/vehicle maximum — very affordable. The View Hotel ($250-400) is premium but unique. Goulding's Lodge outside the park is the budget alternative ($150-250)."
  safety: "Valley Drive is gravel and dirt — impassable when wet. Do not enter beyond the Valley Drive without a Navajo guide (prohibited and disrespectful). Rattlesnakes are present; watch your step on the Wildcat Trail."
  packing: "Camera with a tripod for low-light sunrise/sunset shots, polarized sunglasses, sun protection, water (no services on the Valley Drive), and a light windbreaker (the desert gets cold quickly at night)."
  localCulture: "Monument Valley is the living Navajo Nation homeland, not a national park. The guides are not performers — they are people sharing the history and meaning of their family's land. Listen carefully. Photography of Navajo people requires permission. The restricted areas are restricted for genuine cultural reasons."
"""
    },
    "tucson": {
        "aeo": "Tucson is a desert university city at 2,400 feet — the heart of Sonoran Desert culture with Saguaro National Park, Mission San Xavier, the Arizona-Sonora Desert Museum, and a vibrant food scene, budget $70-200/day, best October through April.",
        "video_title": "Sonoran Desert Heart",
        "video_text": "Tucson sits in the Sonoran Desert surrounded by five mountain ranges, giant saguaro cactus forests, and one of the best Mexican food scenes in the American Southwest.",
        "gradient": "linear-gradient(135deg, #92400e, #1a4731, #1c1917)",
        "affiliatePicks": """  - name: "Loews Ventana Canyon Resort"
    type: hotel
    price: "$200-450/night"
    personalNote: "Beautifully positioned in the Santa Catalina Mountains above Tucson with a waterfall feature, world-class spa, and golf. The desert setting from the pool deck is extraordinary."
    affiliateUrl: "https://www.booking.com/hotel/us/loews-ventana-canyon-resort.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Arizona-Sonora Desert Museum"
    type: activity
    price: "$25/person"
    personalNote: "Not a standard zoo or museum — a 98-acre outdoor experience where desert ecosystems are displayed in their natural habitat. The raptor free-flight show is extraordinary. Allow a full morning."
    affiliateUrl: "https://www.getyourguide.com/tucson-l890/desert-museum-t90123/?partner_id=IVN6IQ3"
    badge: "Don't Miss"
  - name: "Saguaro National Park Sunset Jeep Tour"
    type: tour
    price: "$65-90/person"
    personalNote: "The Saguaro cactus forest at sunset, when the red-orange light turns the desert gold, is one of Arizona's most beautiful scenes. Guided tours know the best photo locations."
    affiliateUrl: "https://www.getyourguide.com/tucson-l890/saguaro-sunset-tour-t01234/?partner_id=IVN6IQ3"
  - name: "Portable Water Filter (Sawyer)"
    type: activity
    price: "$30-50"
    personalNote: "Useful for Saguaro National Park backcountry hiking where water sources exist but quality is uncertain. Also great as backup on longer desert trail hikes."
    affiliateUrl: "https://www.amazon.com/s?k=sawyer+squeeze+water+filter&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Tucson worth visiting?"
    answer: "Yes — Tucson is one of the most underrated cities in the Southwest. The Sonoran Desert culture, Saguaro National Park (in two sections flanking the city), the Arizona-Sonora Desert Museum, Mission San Xavier, excellent Mexican food, and the University of Arizona arts scene make it a substantial destination."
  - question: "Best time to visit Tucson?"
    answer: "October through April. The winter season (November-March) is ideal — 65-75°F days, abundant sunshine, and almost no rain. Spring wildflowers (late February through March) can be spectacular. Summer (June-September) is hot (100°F+) with monsoon rains July-September — manageable if you adapt your schedule."
  - question: "How many days in Tucson?"
    answer: "Two to three days. Day one: Arizona-Sonora Desert Museum (morning), Mission San Xavier del Bac (afternoon). Day two: Saguaro National Park West or East District hiking. Day three: Mount Lemmon Scenic Byway, University of Arizona Museum of Art."
  - question: "Is Tucson safe?"
    answer: "Generally safe for visitors in tourist areas. The University of Arizona district, Catalina Foothills, and Marana are very safe. Downtown Tucson is improving but use standard urban precautions at night. Saguaro National Park is completely safe. Hiking safety: heat and rattlesnakes are real concerns April-October."
  - question: "Tucson on a budget?"
    answer: "Budget $70-100/day. Saguaro National Park entry is $35/vehicle. The Arizona-Sonora Desert Museum ($25) is essential and worth every dollar. Mission San Xavier is free. Mount Lemmon Scenic Byway is free. Excellent cheap Mexican food throughout the city."
  - question: "What is Tucson known for?"
    answer: "Saguaro National Park (two districts flanking the city with the world's densest saguaro forests). The Arizona-Sonora Desert Museum. Mission San Xavier del Bac (the White Dove of the Desert). University of Arizona. The Sonoran Desert hot dog cuisine. Mount Lemmon — the southernmost ski area in the US. Exceptional Mexican and Sonoran cuisine."
  - question: "Do I need a car in Tucson?"
    answer: "Yes — Tucson is car-dependent. The Sun Link streetcar covers the university corridor, but Saguaro National Park, the Desert Museum, and the Catalina Foothills all require a car."
  - question: "Best things to do in Tucson?"
    answer: "Arizona-Sonora Desert Museum (must-do), Saguaro National Park hiking, Mission San Xavier del Bac, Mount Lemmon Scenic Byway, Tucson Botanical Garden, University of Arizona Museum of Art, Fourth Avenue arts district, El Tiradito shrine, and the Barrio Histórico for excellent Mexican food."
""",
        "scottTips": """  logistics: "Tucson International Airport (TUS) has direct service from major cities but fewer flights than Phoenix. Many visitors fly into Phoenix (PHX) and drive 110 miles south on I-10 (1.5-2 hours). Car rental is essential."
  bestTime: "November through March for the best weather. The Saguaro National Park spring wildflower bloom (February-March) is extraordinary. The Gem Show in January-February brings 50,000 people to town — book accommodation well ahead."
  gettingAround: "Car required for Saguaro National Park and most attractions. The Sun Link streetcar covers the university area. Downtown is walkable within a limited zone."
  money: "Tucson is significantly more affordable than Scottsdale or Sedona. Budget $70-120/day. Saguaro NP entry ($35/vehicle) is the main park fee. The Desert Museum ($25) is worth every dollar."
  safety: "Heat and rattlesnakes are the main desert hazards. Hike before 9am in summer, carry substantial water, wear closed-toe shoes. Drive carefully at dawn/dusk — javelinas and other wildlife cross roads frequently."
  packing: "Sun protection (intense UV at 2,400 ft elevation), snake-aware closed-toe boots for hiking, water and electrolytes, binoculars for birding (Tucson is one of the top birding cities in the US)."
  localCulture: "Tucson has a deep Sonoran Desert culture shaped by Indigenous, Spanish, Mexican, and Anglo influences. The University of Arizona gives it a younger energy than Phoenix. The food culture is serious — Tucson was the first US city designated a UNESCO City of Gastronomy, recognized for its Mexican and Indigenous food traditions. Don't miss the Sonoran hot dog."
"""
    },
    "bisbee": {
        "aeo": "Bisbee is a former copper mining boomtown turned artsy mountain village in the Mule Mountains near the Mexican border — a quirky, steep-streeted Victorian ghost-town-turned-arts-community, budget $60-180/day, best October through April.",
        "video_title": "Copper Town Revival",
        "video_text": "Bisbee's steep hillside streets, Victorian buildings, and art galleries are draped over the Mule Mountains above the massive Lavender Pit copper mine — a 1900s boomtown that refused to die.",
        "gradient": "linear-gradient(135deg, #7c2d12, #6b21a8, #1c1917)",
        "affiliatePicks": """  - name: "Copper Queen Hotel"
    type: hotel
    price: "$120-220/night"
    personalNote: "The 1902 historic hotel in the heart of old Bisbee — Victorian character, allegedly haunted (the guests take it seriously), and the best location in town. Book the historic rooms."
    affiliateUrl: "https://www.booking.com/hotel/us/copper-queen-hotel-bisbee.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Queen Mine Tour"
    type: tour
    price: "$25/person"
    personalNote: "Ride a mine train 1,500 feet underground into a working copper mine with retired miners as guides. The most authentic industrial history tour in Arizona — genuinely impressive."
    affiliateUrl: "https://www.getyourguide.com/bisbee-l012/queen-mine-tour-t12345/?partner_id=IVN6IQ3"
    badge: "Must Do"
  - name: "Bisbee Ghost Tour"
    type: tour
    price: "$20-35/person"
    personalNote: "Bisbee's ghost reputation is substantial and the tours are actually well-researched local history. The Copper Queen Hotel's ghost stories are particularly compelling regardless of your belief level."
    affiliateUrl: "https://www.getyourguide.com/bisbee-l012/ghost-tour-t23456/?partner_id=IVN6IQ3"
  - name: "Tombstone and Bisbee Combo Day Tour"
    type: tour
    price: "$80-120/person"
    personalNote: "Both towns are 30 minutes apart — a combined day tour from Tucson is the efficient way to visit both without managing the driving yourself."
    affiliateUrl: "https://www.getyourguide.com/tucson-l890/tombstone-bisbee-day-tour-t34567/?partner_id=IVN6IQ3"
""",
        "faqItems": """  - question: "Is Bisbee worth visiting?"
    answer: "Yes for the right traveler — someone who enjoys quirky small towns with depth, history, and arts. The Queen Mine tour is genuinely excellent. Old Bisbee's steep streets and Victorian buildings are unique in Arizona. The arts and gallery scene is real. It is not a place for those expecting polished amenities."
  - question: "Best time to visit Bisbee?"
    answer: "October through April. At 5,300 feet elevation, Bisbee is 10-15 degrees cooler than Tucson year-round. Summers are pleasant (70-85°F) by Arizona standards. Winter brings occasional freezing temperatures and rare snow. The Bisbee 1000 stair climb race in October is a popular annual event."
  - question: "How many days in Bisbee?"
    answer: "One to two days. Day one: Queen Mine tour, Old Bisbee neighborhood walk, Brewery Gulch. Day two: galleries, Lavender Pit viewpoint, day trip to Tombstone (30 minutes)."
  - question: "Is Bisbee safe?"
    answer: "Very safe and relaxed. The steep streets require attention when walking. The area near the Mexican border (10 miles) is well-trafficked and safe for daytime visits."
  - question: "Bisbee on a budget?"
    answer: "Budget $60-90/day. The Queen Mine tour ($25) is essential. The town walk, galleries, and Lavender Pit viewpoint are free. More affordable accommodation than Tucson or Sedona."
  - question: "What is Bisbee known for?"
    answer: "The historic copper mining district — at its 1900s peak, Bisbee had a larger population than Los Angeles. The Lavender Pit open-pit copper mine (one of the largest in the world). Victorian architecture on steep hillside streets. A vibrant arts community that moved in after the mines closed. The Copper Queen Hotel's ghost stories."
  - question: "Do I need a car in Bisbee?"
    answer: "Yes to get here — Bisbee is 90 miles southeast of Tucson on I-10/US-80. Old Bisbee itself is compact and best explored on foot (the steep stairs are the defining feature of the town geography)."
  - question: "Best things to do in Bisbee?"
    answer: "Queen Mine underground tour, Old Bisbee neighborhood and stair walking, Brewery Gulch Historic District, Lavender Pit copper mine viewpoint, Bisbee Mining and Historical Museum, art galleries on Main Street, and the Copper Queen Hotel bar."
""",
        "scottTips": """  logistics: "Drive from Tucson: 90 miles southeast, 1.5 hours on I-10 then US-80. Or combine with Tombstone (25 miles north of Bisbee). The approach through the Mule Mountains pass is dramatic."
  bestTime: "Year-round, but October-April is most comfortable. The cooler elevation makes summer more tolerable here than the low desert. Holiday weekends in December see strong arts event programming."
  gettingAround: "Car to get here. Old Bisbee is walking and stair territory — the town is built vertically on hillsides."
  money: "One of Arizona's most affordable destinations. Budget $60-100/day. The Queen Mine tour ($25) is the main expense."
  safety: "Steep stairs and hillside streets require attention especially in wet weather. The Mexican border is 10 miles south — the area is safe for daytime tourism."
  packing: "Comfortable walking shoes with grip for the steep stairs, layers for the 5,300 ft elevation, camera for the Victorian architecture."
  localCulture: "Bisbee's character was shaped by two waves: the mining era (1880s-1975) and the arts/alternative community that moved in after. Both are visible in the town. The former miners and the artists coexist peacefully and both take Bisbee's identity seriously. The ghost culture is genuinely local, not manufactured for tourists."
"""
    },
    "tombstone": {
        "aeo": "Tombstone is the most famous gunfighter town in American history — a preserved 1880s frontier silver mining boomtown where the OK Corral gunfight happened, best visited as a half-day or day trip combined with Bisbee, budget $50-120/day.",
        "video_title": "The Town Too Tough to Die",
        "video_text": "Tombstone's Allen Street still looks like 1881 — the saloons, the OK Corral, and the Boot Hill graveyard are authentic frontier history, not recreation.",
        "gradient": "linear-gradient(135deg, #1c1917, #7c2d12, #b45309)",
        "affiliatePicks": """  - name: "Best Western Tombstone"
    type: hotel
    price: "$100-160/night"
    personalNote: "Reliable mid-range option if you want to overnight in Tombstone rather than day-tripping. Staying for the evening gunfight reenactments and nighttime atmosphere adds significantly to the experience."
    affiliateUrl: "https://www.booking.com/hotel/us/best-western-tombstone.html?aid=2778866"
  - name: "OK Corral Gunfight Reenactment"
    type: activity
    price: "$15/person"
    personalNote: "The reenactment is theatrical but the historical accuracy is reasonable and the location is the actual site of the October 1881 gunfight. Worth the price for the staging and audio guide."
    affiliateUrl: "https://www.getyourguide.com/tombstone-l123/ok-corral-reenactment-t23456/?partner_id=IVN6IQ3"
    badge: "Tombstone Classic"
  - name: "Tombstone Ghost Tour"
    type: tour
    price: "$20-30/person"
    personalNote: "Evening ghost tours through Tombstone's dark history — violence, disease, and mining accidents created a rich legacy. Well-researched local history with good storytelling."
    affiliateUrl: "https://www.getyourguide.com/tombstone-l123/ghost-tour-t34567/?partner_id=IVN6IQ3"
  - name: "Tombstone and Bisbee Combo Tour from Tucson"
    type: tour
    price: "$80-120/person"
    personalNote: "Both towns are most efficiently visited together from Tucson — 1.5 hours from the city, 25 minutes between them. Combine for a full day of frontier history."
    affiliateUrl: "https://www.getyourguide.com/tucson-l890/tombstone-bisbee-combo-t45678/?partner_id=IVN6IQ3"
""",
        "faqItems": """  - question: "Is Tombstone worth visiting?"
    answer: "Yes as a half-day or day trip, especially combined with Bisbee. The authentic 1880s frontier architecture of Allen Street, the OK Corral site, and the Boot Hill graveyard are genuinely interesting. It is touristy but the history underneath is real. Do not expect more than a few hours of content."
  - question: "Best time to visit Tombstone?"
    answer: "October through April for comfortable temperatures. The Helldorado Days festival in October is a major annual event. Summer (June-September) is hot (95°F+) but the town is quieter. Weekday visits avoid the weekend tour bus crowds."
  - question: "How many days in Tombstone?"
    answer: "Half-day to one day is sufficient for most visitors. The main sites (OK Corral, Allen Street walk, Boot Hill, Crystal Palace Saloon) take 3-4 hours. Combine with Bisbee (25 minutes south) for a full day's program."
  - question: "Is Tombstone safe?"
    answer: "Very safe and heavily touristed. The gunfight reenactments are theatrical. Standard tourist area safety applies. The area outside town is desert — carry water if hiking the surrounding hills."
  - question: "Tombstone on a budget?"
    answer: "Budget $50-70/day as a day trip. OK Corral ($15) and Boot Hill ($3) are the main paid attractions. Allen Street walking is free. Combine with Bisbee for the best value use of the drive."
  - question: "What is Tombstone known for?"
    answer: "The OK Corral gunfight (October 26, 1881) between the Earp brothers and Doc Holliday against the Clanton-McLaury gang. The most famous gunfight in American frontier history. The preserved 1880s frontier town character. Boot Hill cemetery. The Crystal Palace and Bird Cage Theatre saloons."
  - question: "Do I need a car in Tombstone?"
    answer: "Yes to get here — Tombstone is 70 miles southeast of Tucson. The town itself is walkable; Allen Street is a short pedestrian strip."
  - question: "Best things to do in Tombstone?"
    answer: "OK Corral and gunfight reenactment, Allen Street walk and saloon stops, Boot Hill Graveyard, Tombstone Courthouse State Historic Park, Crystal Palace Saloon, Bird Cage Theatre, and the 1880s street photography."
""",
        "scottTips": """  logistics: "Drive from Tucson: 70 miles, 1.5 hours on I-10 east and then AZ-80 south. Combine with Bisbee 25 minutes further south for the best full-day use of the drive."
  bestTime: "October-April. The Helldorado Days festival in October recreates the 1880s frontier atmosphere. Weekday visits are quieter. Arrive before the tour buses mid-morning."
  gettingAround: "Allen Street and the main historic district are fully walkable — park at the lots on the edge of town and walk in."
  money: "Very affordable day trip destination. Budget $50-80. OK Corral ($15) is the main expense. Good value frontier food available on Allen Street."
  safety: "Very safe tourist town. The gunfight reenactments are theatrical performances. The frontier history here is genuine but the present-day town is thoroughly safe."
  packing: "Comfortable walking shoes, sun protection (limited shade on Allen Street), water."
  localCulture: "Tombstone's Wild West identity is authentic — this was genuinely a violent mining boomtown in the 1880s. The Earps and Clantons were real people in a real conflict. The theatrical elements today rest on a foundation of documented history. The locals take that history seriously; engage with it beyond the gift shop level."
"""
    },
    "petrified-forest": {
        "aeo": "Petrified Forest National Park is a high desert wilderness in northeastern Arizona where ancient trees turned to crystal over 225 million years — budget $35 vehicle entry, best March through May and September through November, combined with nearby Painted Desert.",
        "video_title": "Ancient Forest in Stone",
        "video_text": "Two hundred and twenty-five million years of geological time crystallized into the rainbow-hued logs of the Petrified Forest — ancient trees turned to crystal on the high desert floor.",
        "gradient": "linear-gradient(135deg, #92400e, #6b21a8, #1a4731)",
        "affiliatePicks": """  - name: "La Posada Hotel Winslow"
    type: hotel
    price: "$120-220/night"
    personalNote: "A Fred Harvey-era railroad hotel restored to its 1930s glory — one of the finest historic hotels in Arizona, 30 miles from Petrified Forest. The grounds and restaurant are extraordinary."
    affiliateUrl: "https://www.booking.com/hotel/us/la-posada-hotel-winslow.html?aid=2778866"
    badge: "Scott's Pick"
  - name: "Petrified Forest and Painted Desert Guided Tour"
    type: tour
    price: "$80-120/person"
    personalNote: "A guided geology and natural history tour of the park explains the 225-million-year story behind the crystal logs and Painted Desert colors. Much more context than self-touring."
    affiliateUrl: "https://www.getyourguide.com/petrified-forest-l234/guided-geology-tour-t34567/?partner_id=IVN6IQ3"
  - name: "Route 66 and Petrified Forest Combo Tour from Flagstaff"
    type: tour
    price: "$100-150/person"
    personalNote: "Combines Route 66 historic sites (Holbrook, Winslow) with the Petrified Forest in an efficient day loop from Flagstaff."
    affiliateUrl: "https://www.getyourguide.com/flagstaff-l567/route-66-petrified-forest-t45678/?partner_id=IVN6IQ3"
  - name: "Portable Water Filter (Sawyer Squeeze)"
    type: activity
    price: "$30-50"
    personalNote: "Backcountry hiking in Petrified Forest requires carrying all water in — there are no water sources in the wilderness areas. A filter is useful for emergency backup."
    affiliateUrl: "https://www.amazon.com/s?k=sawyer+squeeze+water+filter&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Petrified Forest worth visiting?"
    answer: "Yes, especially combined with the Painted Desert drive — the 28-mile park road through both sections takes 2-3 hours and is genuinely remarkable. The petrified wood logs and the Painted Desert color bands are unlike anything in the Southwest. It is an underrated park that rewards the detour off I-40."
  - question: "Best time to visit Petrified Forest?"
    answer: "March through May and September through November. The park sits at 5,400 feet elevation — cooler than the low desert with temperatures of 50-80°F in spring and fall. Summer afternoons can reach 95°F. Monsoon rains July-September create dramatic skies."
  - question: "How many days at Petrified Forest?"
    answer: "One day is sufficient. The 28-mile park road covers all the main viewpoints and takes 2-4 hours. Add backcountry hiking for a longer visit. Most visitors combine with Painted Desert as a day trip from Flagstaff or as a stop along I-40."
  - question: "Is Petrified Forest safe?"
    answer: "Very safe. Standard desert hiking precautions apply. Backcountry hiking requires carrying all water. The main road is accessible by all vehicles. Do not remove petrified wood — it is a federal offense (and locals report strange bad luck to those who do)."
  - question: "Petrified Forest on a budget?"
    answer: "Budget $35-50/day (mostly the vehicle entry fee). The park is compact enough to see in a day from Flagstaff or Holbrook. No camping within the park without a backcountry permit (free). La Posada in Winslow is the area's best accommodation investment."
  - question: "What is Petrified Forest known for?"
    answer: "The world's largest concentration of petrified wood — ancient Triassic-period trees that fell into swamps 225 million years ago and were slowly replaced by silica crystal. Rainbow Forest, Blue Mesa badlands, and the Painted Desert's colorful banded hills. Ancient petroglyphs at Newspaper Rock."
  - question: "Do I need a car at Petrified Forest?"
    answer: "Yes — the park is accessed via I-40 (north entrance, Painted Desert) or US-180 (south entrance, Rainbow Forest). The 28-mile park road connects both entrances and is the primary experience."
  - question: "Best things to do at Petrified Forest?"
    answer: "28-mile park road drive (north to south or reverse), Crystal Forest trail (0.75 miles of petrified logs), Blue Mesa badlands hike, Newspaper Rock petroglyph viewpoint, Long Logs trail (1.6 miles), Painted Desert rim overlooks, and dawn or dusk photography for the best light on the crystal logs."
""",
        "scottTips": """  logistics: "Access from I-40 (north Painted Desert entrance) or US-180 from Holbrook (south Rainbow Forest entrance). Flagstaff to south entrance: 110 miles, 1.5 hours on US-180. Many visitors do a north-to-south drive-through between Flagstaff and Albuquerque or Phoenix."
  bestTime: "Spring and fall for ideal temperatures. Sunrise and sunset create extraordinary light on the petrified logs and Painted Desert colors — the crystal wood literally glows. Midday light is flat."
  gettingAround: "28-mile park road connects the two entrances. Pull-offs at all major viewpoints. Short hiking trails accessible from the road."
  money: "$35 vehicle entry fee valid for 7 days. No food services within the park — bring lunch. La Posada in Winslow ($120-220/night) is the area's dining and lodging standout."
  safety: "Carry all water you need (no water sources in backcountry), sun protection, and do not enter backcountry in summer afternoon heat. The petrified wood looks portable but removal is a federal crime."
  packing: "Sun protection, full water supply for the day, and a camera. The light at sunrise and sunset makes this extraordinary — plan your visit around those hours."
  localCulture: "The Petrified Forest region was home to the Ancestral Puebloan and other peoples for thousands of years — Newspaper Rock's petroglyphs represent a fraction of the cultural heritage visible throughout the park. The regional significance of the 225-million-year fossil record is not just geological but has been significant to the Indigenous understanding of deep time."
"""
    },
    "saguaro-national-park": {
        "aeo": "Saguaro National Park is a two-district park flanking Tucson that protects the world's densest forest of giant saguaro cactus — the iconic Sonoran Desert landscape, free with America the Beautiful pass or $35 vehicle entry, best October through April.",
        "video_title": "Forest of Giants",
        "video_text": "The giant saguaro cactus — some 200 years old and 50 feet tall — creates one of the most distinctive landscapes in North America in the desert flanking Tucson.",
        "gradient": "linear-gradient(135deg, #92400e, #1a4731, #1c1917)",
        "affiliatePicks": """  - name: "Saguaro Sunrise Photography Tour"
    type: tour
    price: "$65-100/person"
    personalNote: "The saguaro forest at sunrise, when the morning light turns the cactus columns gold and the desert comes alive with bird calls, is the most beautiful time in the park. Guided tours know exactly where to position."
    affiliateUrl: "https://www.getyourguide.com/tucson-l890/saguaro-sunrise-tour-t56789/?partner_id=IVN6IQ3"
    badge: "Most Beautiful"
  - name: "Saguaro National Park Hiking Tour (West District)"
    type: tour
    price: "$55-85/person"
    personalNote: "The West District's Valley View Overlook and Hugh Norris Trail give the best combined saguaro density and elevation views. Guided for the best route planning."
    affiliateUrl: "https://www.getyourguide.com/tucson-l890/saguaro-west-hiking-t67890/?partner_id=IVN6IQ3"
  - name: "Arizona-Sonora Desert Museum Combo"
    type: activity
    price: "$25/person (museum only)"
    personalNote: "Combine Saguaro NP West District with the Desert Museum next door — the museum contextualizes everything you see in the park. A morning in both is Tucson's best day."
    affiliateUrl: "https://www.getyourguide.com/tucson-l890/desert-museum-t90123/?partner_id=IVN6IQ3"
    badge: "Perfect Combo"
  - name: "Electrolyte Packets for Desert Hiking"
    type: activity
    price: "$15-25"
    personalNote: "Desert hiking in April-October requires electrolyte management. Saguaro's exposed trails in the heat can drain you quickly — carry both water and electrolytes."
    affiliateUrl: "https://www.amazon.com/s?k=electrolyte+packets+hiking+desert&tag=discovermore-20"
""",
        "faqItems": """  - question: "Is Saguaro National Park worth visiting?"
    answer: "Yes — it is the only national park that exists for a single species of plant, and the saguaro cactus forest is genuinely extraordinary. Giant saguaros up to 200 years old and 50 feet tall create a landscape unique to the Sonoran Desert. The proximity to Tucson makes it easy to incorporate into any Arizona trip."
  - question: "Best time to visit Saguaro National Park?"
    answer: "October through April. Spring wildflowers (February-April) are spectacular. Saguaro blooms (white flowers at the top of each arm) peak in May. Summer is hot and humid during monsoon season — hike before 8am only. Winter months are comfortable and uncrowded."
  - question: "How many days at Saguaro National Park?"
    answer: "One day covers both districts with proper planning. West District (Rincon Valley area) in the morning with Desert Museum combo. East District (Rincon Mountains) for afternoon hiking. Two days allows for the Hugh Norris Trail (West, strenuous) and the Mica View Trail (East, varied terrain)."
  - question: "Is Saguaro National Park safe?"
    answer: "Very safe with standard desert precautions. Heat and dehydration are the primary hazards April-October. Rattlesnakes and Gila woodpeckers are common — watch your step and don't reach into brush. Javelinas roam both districts and can be aggressive if they feel threatened — give them space."
  - question: "Saguaro National Park on a budget?"
    answer: "Budget $35-50/day (vehicle entry fee). Free with America the Beautiful annual pass. The free Cactus Forest Drive loop in the East District can be done without additional fees. Combine with the Desert Museum ($25) for the best value day in Tucson."
  - question: "What is Saguaro National Park known for?"
    answer: "The Sonoran Desert's giant saguaro cactus forests — found only in a small region of Arizona and Sonora, Mexico. The two-district park (East and West, flanking Tucson) protects the largest concentration of giant saguaros in the world. Saguaros are the Sonoran Desert's keystone species, hosting dozens of other species in their holes and arms."
  - question: "Do I need a car at Saguaro National Park?"
    answer: "Yes to reach both districts. The West District is adjacent to the Arizona-Sonora Desert Museum (a convenient combination). The East District is in the Rincon Mountains 15 miles east of downtown Tucson."
  - question: "Best things to do at Saguaro National Park?"
    answer: "Valley View Overlook Trail (West District, easy, best saguaro density views), Hugh Norris Trail (West District, strenuous, panoramic Tucson views), Cactus Forest Drive (East District, 8-mile loop), Mica View Trail (East District, varied desert terrain), desert wildflower bloom hikes (February-April), and saguaro bloom viewing (May)."
""",
        "scottTips": """  logistics: "Two districts on opposite sides of Tucson. West District: 2101 N. Kinney Road (adjacent to Desert Museum). East District: 3693 S. Old Spanish Trail. Drive between them takes 45 minutes through Tucson. One vehicle entry fee covers both districts for 7 days."
  bestTime: "October through April. Saguaro bloom (May) is spectacular. February-April wildflowers. Sunrise in the saguaro forest is the single most beautiful time — arrive at the West District trailhead 30 minutes before sunrise."
  gettingAround: "Car required for both districts. West District has a good road system and the Desert Museum adjacent. East District has the scenic Cactus Forest Drive (paved loop)."
  money: "$35 vehicle entry covers 7 days in both districts. America the Beautiful pass ($80/year) works here and at Grand Canyon, Petrified Forest, and every other federal site."
  safety: "Heat and rattlesnakes April-October. Carry substantial water — the desert environment is dehydrating even on cool days. Javelinas at Saguaro can be territorial — maintain distance."
  packing: "Sun protection (intense desert UV year-round), at least 2 liters of water per person, closed-toe shoes for rocky trails, camera for the extraordinary light at sunrise and sunset."
  localCulture: "The saguaro cactus is a keystone species for the entire Sonoran Desert ecosystem — Gila woodpeckers carve nesting holes, elf owls take over abandoned holes, and coyotes eat the fruit. The O'odham people have harvested saguaro fruit for thousands of years as the first food of the new year. Understanding the ecological context makes the forest far more meaningful."
"""
    },
}

for slug, data in DESTINATIONS.items():
    filepath = f"{BASE}/{slug}.md"
    if not os.path.exists(filepath):
        print(f"SKIP {slug} — not found")
        continue

    content = open(filepath, 'r', encoding='utf-8').read()

    # Check if already processed
    if "affiliatePicks:" in content:
        print(f"SKIP {slug} — already has Tier 3")
        continue

    # Add frontmatter fields before closing ---
    tier3_fm = (
        f"affiliatePicks:\n{data['affiliatePicks']}"
        f"faqItems:\n{data['faqItems']}"
        f"scottTips:\n{data['scottTips']}"
    )

    # Arizona files end with draft: false\n---
    old_fm_end = "contentStatus: published\ndraft: false\n---"
    new_fm_end = f"contentStatus: published\ndraft: false\n{tier3_fm}---"

    if old_fm_end not in content:
        # Try without fmContentType
        print(f"WARN {slug} — standard FM end not found, checking alternatives")
        continue

    content = content.replace(old_fm_end, new_fm_end, 1)

    # Find body start using line-by-line approach
    lines = content.split('\n')
    fm_end_line = -1
    dash_count = 0
    for i, line in enumerate(lines):
        if line.strip() == '---':
            dash_count += 1
            if dash_count == 2:
                fm_end_line = i
                break

    if fm_end_line == -1:
        print(f"WARN {slug} — could not find FM end in updated content")
        open(filepath, 'w', encoding='utf-8').write(content)
        print(f"Done {slug} (FM only)")
        continue

    # Find first non-empty paragraph
    body_start = fm_end_line + 1
    while body_start < len(lines) and not lines[body_start].strip():
        body_start += 1

    if body_start >= len(lines):
        print(f"WARN {slug} — no body content")
        open(filepath, 'w', encoding='utf-8').write(content)
        continue

    # Find end of first paragraph
    para_end = body_start
    while para_end < len(lines) and lines[para_end].strip():
        para_end += 1

    first_para = '\n'.join(lines[body_start:para_end])

    video_block = (
        '<div class="immersive-break-inline">\n'
        '  <video autoplay muted loop playsinline preload="metadata">\n'
        f'    <source src="/videos/destinations/{slug}-hero.mp4" type="video/mp4" />\n'
        '  </video>\n'
        f'  <div class="ib-gradient" style="background: {data["gradient"]};"></div>\n'
        '  <div class="ib-content">\n'
        f'    <div class="ib-title">{data["video_title"]}</div>\n'
        f'    <p class="ib-text">{data["video_text"]}</p>\n'
        '  </div>\n'
        '</div>'
    )

    # Build new content
    new_lines = lines[:fm_end_line+1]
    new_lines.append('')
    new_lines.append(data['aeo'])
    new_lines.append('')
    new_lines.extend(video_block.split('\n'))
    new_lines.append('')
    new_lines.append(first_para)
    new_lines.extend(lines[para_end:])

    new_content = '\n'.join(new_lines)

    # Remove old scott-tips div
    new_content = re.sub(r'<div class="scott-tips">.*?</div>', '', new_content, flags=re.DOTALL)

    open(filepath, 'w', encoding='utf-8').write(new_content)
    print(f"Done {slug}")

print("Arizona Tier 3 complete")
