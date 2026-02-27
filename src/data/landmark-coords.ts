// Popular Arizona POI coordinates for itinerary geocoding.
// Keyed by lowercase normalized name. Covers top attractions at all 12 destinations.
// Used by generate-itinerary.ts to resolve activity coordinates without Geocoding API calls.

export const LANDMARK_COORDS: Record<string, { lat: number; lng: number }> = {
  // ── Grand Canyon ──
  'bright angel trail': { lat: 36.0575, lng: -112.1438 },
  'south kaibab trail': { lat: 36.0529, lng: -112.0841 },
  'grand canyon south rim': { lat: 36.0544, lng: -112.1401 },
  'grand canyon north rim': { lat: 36.1980, lng: -112.0567 },
  'mather point': { lat: 36.0614, lng: -112.1075 },
  'yavapai point': { lat: 36.0654, lng: -112.1180 },
  'desert view watchtower': { lat: 36.0441, lng: -111.8267 },
  'hermits rest': { lat: 36.0622, lng: -112.2134 },
  'grand canyon village': { lat: 36.0547, lng: -112.1390 },
  'phantom ranch': { lat: 36.0997, lng: -112.0953 },
  'hopi point': { lat: 36.0725, lng: -112.1563 },
  'toroweap overlook': { lat: 36.2102, lng: -113.0628 },
  'havasu falls': { lat: 36.2553, lng: -112.6979 },

  // ── Sedona ──
  'cathedral rock': { lat: 34.8233, lng: -111.7894 },
  'bell rock': { lat: 34.8078, lng: -111.7631 },
  'devil\'s bridge': { lat: 34.9027, lng: -111.8133 },
  'airport mesa': { lat: 34.8486, lng: -111.7777 },
  'chapel of the holy cross': { lat: 34.8282, lng: -111.7631 },
  'slide rock state park': { lat: 34.9278, lng: -111.7519 },
  'red rock crossing': { lat: 34.8236, lng: -111.7978 },
  'boynton canyon': { lat: 34.9078, lng: -111.8444 },
  'west fork trail': { lat: 34.9550, lng: -111.7450 },
  'tlaquepaque arts village': { lat: 34.8583, lng: -111.7611 },
  'sedona uptown': { lat: 34.8714, lng: -111.7610 },

  // ── Phoenix ──
  'camelback mountain': { lat: 33.5227, lng: -111.9710 },
  'desert botanical garden': { lat: 33.4617, lng: -111.9444 },
  'heard museum': { lat: 33.4728, lng: -112.0722 },
  'south mountain park': { lat: 33.3503, lng: -112.0614 },
  'papago park': { lat: 33.4534, lng: -111.9493 },
  'hole in the rock': { lat: 33.4565, lng: -111.9453 },
  'phoenix sky harbor airport': { lat: 33.4373, lng: -112.0078 },
  'sky harbor': { lat: 33.4373, lng: -112.0078 },
  'phoenix art museum': { lat: 33.4671, lng: -112.0729 },
  'musical instrument museum': { lat: 33.6678, lng: -111.9781 },
  'chase field': { lat: 33.4455, lng: -112.0667 },
  'roosevelt row': { lat: 33.4580, lng: -112.0630 },
  'piestewa peak': { lat: 33.5494, lng: -112.0244 },

  // ── Scottsdale ──
  'old town scottsdale': { lat: 33.4928, lng: -111.9261 },
  'scottsdale fashion square': { lat: 33.5028, lng: -111.9278 },
  'taliesin west': { lat: 33.6067, lng: -111.8444 },
  'mcdowell sonoran preserve': { lat: 33.6531, lng: -111.8569 },
  'scottsdale museum of contemporary art': { lat: 33.4942, lng: -111.9222 },
  'pinnacle peak': { lat: 33.7236, lng: -111.8586 },
  'butterfly wonderland': { lat: 33.5533, lng: -111.8767 },
  'odysea aquarium': { lat: 33.5503, lng: -111.8750 },
  'scottsdale waterfront': { lat: 33.5010, lng: -111.9250 },

  // ── Tucson ──
  'arizona-sonora desert museum': { lat: 32.2452, lng: -111.1668 },
  'mission san xavier del bac': { lat: 32.1072, lng: -111.0078 },
  'mount lemmon': { lat: 32.4432, lng: -110.7884 },
  'pima air and space museum': { lat: 32.1706, lng: -110.8681 },
  'tucson mountain park': { lat: 32.2194, lng: -111.1308 },
  'sabino canyon': { lat: 32.3178, lng: -110.8208 },
  'gate\'s pass': { lat: 32.2250, lng: -111.1111 },
  'university of arizona': { lat: 32.2319, lng: -110.9501 },
  '4th avenue tucson': { lat: 32.2286, lng: -110.9667 },
  'el presidio': { lat: 32.2236, lng: -110.9720 },
  'tucson international airport': { lat: 32.1161, lng: -110.9411 },

  // ── Monument Valley ──
  'monument valley navajo tribal park': { lat: 36.9830, lng: -110.0985 },
  'the mittens': { lat: 36.9833, lng: -110.1000 },
  'merrick butte': { lat: 36.9750, lng: -110.0917 },
  'john ford point': { lat: 36.9571, lng: -110.1164 },
  'artists point monument valley': { lat: 36.9483, lng: -110.1083 },
  'totem pole monument valley': { lat: 36.9367, lng: -110.1133 },
  'forrest gump point': { lat: 37.1013, lng: -109.9908 },
  'the view hotel': { lat: 36.9833, lng: -110.0967 },
  'mystery valley': { lat: 36.9417, lng: -110.1583 },
  'hunts mesa': { lat: 36.9422, lng: -110.0944 },

  // ── Flagstaff ──
  'humphreys peak': { lat: 35.3464, lng: -111.6781 },
  'lowell observatory': { lat: 35.2028, lng: -111.6647 },
  'walnut canyon': { lat: 35.1719, lng: -111.5086 },
  'sunset crater': { lat: 35.3633, lng: -111.5017 },
  'wupatki national monument': { lat: 35.5175, lng: -111.3667 },
  'arizona snowbowl': { lat: 35.3306, lng: -111.7100 },
  'downtown flagstaff': { lat: 35.1983, lng: -111.6513 },
  'museum of northern arizona': { lat: 35.2153, lng: -111.6603 },
  'flagstaff pulliam airport': { lat: 35.1381, lng: -111.6713 },
  'riordan mansion': { lat: 35.2017, lng: -111.6483 },

  // ── Page ──
  'horseshoe bend': { lat: 36.8791, lng: -111.5104 },
  'antelope canyon': { lat: 36.8619, lng: -111.3743 },
  'upper antelope canyon': { lat: 36.8619, lng: -111.3743 },
  'lower antelope canyon': { lat: 36.8412, lng: -111.4086 },
  'lake powell': { lat: 37.0683, lng: -111.2433 },
  'glen canyon dam': { lat: 36.9375, lng: -111.4847 },
  'wahweap marina': { lat: 36.9978, lng: -111.4889 },
  'rainbow bridge': { lat: 37.0778, lng: -110.9642 },
  'page airport': { lat: 36.9261, lng: -111.4486 },
  'hanging garden': { lat: 36.9103, lng: -111.4800 },

  // ── Petrified Forest ──
  'petrified forest national park': { lat: 35.0653, lng: -109.7890 },
  'painted desert': { lat: 35.1333, lng: -109.7833 },
  'blue mesa trail': { lat: 34.9781, lng: -109.8469 },
  'crystal forest': { lat: 34.9200, lng: -109.8033 },
  'newspaper rock petrified forest': { lat: 35.0417, lng: -109.7917 },
  'agate bridge': { lat: 34.9567, lng: -109.8133 },
  'puerco pueblo': { lat: 35.0633, lng: -109.7550 },
  'painted desert inn': { lat: 35.1083, lng: -109.7867 },

  // ── Saguaro National Park ──
  'saguaro national park east': { lat: 32.1797, lng: -110.7383 },
  'saguaro national park west': { lat: 32.2497, lng: -111.2178 },
  'signal hill petroglyphs': { lat: 32.2700, lng: -111.2183 },
  'valley view overlook': { lat: 32.2625, lng: -111.2142 },
  'cactus forest drive': { lat: 32.1778, lng: -110.7267 },
  'freeman homestead trail': { lat: 32.1608, lng: -110.7286 },
  'tanque verde ridge trail': { lat: 32.1733, lng: -110.7333 },
  'hugh norris trail': { lat: 32.2575, lng: -111.2167 },

  // ── Tombstone ──
  'ok corral': { lat: 31.7131, lng: -110.0669 },
  'boothill graveyard': { lat: 31.7189, lng: -110.0700 },
  'bird cage theatre': { lat: 31.7125, lng: -110.0658 },
  'tombstone courthouse': { lat: 31.7133, lng: -110.0672 },
  'allen street tombstone': { lat: 31.7128, lng: -110.0667 },
  'big nose kate\'s saloon': { lat: 31.7128, lng: -110.0669 },
  'tombstone epitaph museum': { lat: 31.7125, lng: -110.0672 },

  // ── Bisbee ──
  'queen mine tour': { lat: 31.4378, lng: -109.9200 },
  'bisbee mining museum': { lat: 31.4489, lng: -109.9283 },
  'brewery gulch': { lat: 31.4481, lng: -109.9272 },
  'lavender pit': { lat: 31.4333, lng: -109.9117 },
  'bisbee stairs': { lat: 31.4478, lng: -109.9289 },
  'main street bisbee': { lat: 31.4487, lng: -109.9283 },
  'copper queen hotel': { lat: 31.4489, lng: -109.9281 },
  'bisbee restoration museum': { lat: 31.4489, lng: -109.9283 },
};
