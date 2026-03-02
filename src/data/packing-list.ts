import type { PackingItem, PackingConfig, GearRecommendation } from './packing-base';

export const ARIZONA_ESSENTIALS: PackingItem[] = [
  { id: 'az-water', name: 'Hydration System (3L minimum)', category: 'destination', description: 'Grand Canyon day hikes in summer require 4+ liters of water. Dehydration comes fast at 105°F. Rangers rescue hundreds of people per year who underestimated water needs. 3L minimum, always.', essential: true, amazonSearchFallback: 'hydration+pack+3+liter+hiking', affiliatePrice: '$40–70' },
  { id: 'az-sunprotect', name: 'Full Sun Protection Kit', category: 'destination', description: 'SPF 50+ sunscreen, UPF 50 long-sleeved shirt, wide-brim hat, sunglasses. Arizona UV regularly hits 11+ (extreme). Exposed skin burns in 10 minutes in summer.', essential: true, amazonSearchFallback: 'upf+50+sun+protection+shirt+long+sleeve', affiliatePrice: '$30–50' },
  { id: 'az-hikeboots', name: 'Hiking Boots (ankle support)', category: 'destination', description: 'Grand Canyon, Antelope Canyon approach trails, Sedona red rock — loose rock, uneven terrain, and significant elevation changes. Trail runners minimum, ankle boots preferred.', essential: true, amazonSearchFallback: 'hiking+boots+ankle+support+trail', affiliatePrice: '$80–150' },
  { id: 'az-electrolytes', name: 'Electrolyte Packets', category: 'destination', description: 'Drinking water alone isn\'t enough in extreme heat. You sweat out sodium and potassium faster than you can drink. Nuun, Liquid IV, or similar — pack plenty.', essential: true, amazonSearchFallback: 'electrolyte+packets+hydration+nuun+travel', affiliatePrice: '$15–25' },
];

export const ARIZONA_GEAR_RECOMMENDATIONS: GearRecommendation[] = [
  { id: 'gr-az-hydration', name: 'Hydration Pack (3L reservoir)', reason: 'Grand Canyon rangers pull people out every summer for dehydration. A hydration pack keeps water hands-free and makes it easy to drink constantly — exactly what you need at 105°F.', amazonSearchFallback: 'hydration+pack+3+liter+reservoir+hiking', affiliatePrice: '~$55' },
  { id: 'gr-az-sunshirt', name: 'UPF 50 Long-Sleeve Sun Shirt', reason: 'Arizona UV regularly hits 11 (extreme). A UPF 50 long-sleeve shirt is lighter and more effective than reapplying sunscreen every 90 minutes in the desert heat.', amazonSearchFallback: 'upf+50+long+sleeve+sun+shirt+outdoor', affiliatePrice: '~$40' },
  { id: 'gr-az-hat', name: 'Wide-Brim Sun Hat', reason: 'Your neck, ears, and face get cooked on canyon trails. A wide-brim hat — not a baseball cap — protects 360 degrees of exposure that would otherwise burn in an hour.', amazonSearchFallback: 'wide+brim+hat+upf+sun+protection+hiking', affiliatePrice: '~$30' },
  { id: 'gr-az-boots', name: 'Ankle-Support Hiking Boots', reason: 'Sedona red rock, Grand Canyon rim-to-river, Antelope Canyon approaches — loose volcanic and sandstone rock. Ankle support prevents the twisted ankles that end trips early.', amazonSearchFallback: 'hiking+boots+ankle+support+waterproof+trail', affiliatePrice: '~$120' },
  { id: 'gr-az-electrolytes', name: 'Electrolyte Packets', reason: 'Water alone isn\'t enough in Arizona heat. Sodium and potassium depletion causes cramping, dizziness, and heat exhaustion. Nuun or Liquid IV in every water bottle on hot hike days.', amazonSearchFallback: 'electrolyte+packets+nuun+liquid+iv+hydration', affiliatePrice: '~$20' },
];

export const ARIZONA_CONFIG: PackingConfig = {
  sitePrefix: 'daz',
  destination: 'Arizona',
  climate: ['desert'],
  currency: 'USD',
  plugType: 'Type A/B',
  plugVoltage: '120V',
  affiliateTag: 'discovermore-20',
  destinationEssentials: ARIZONA_ESSENTIALS,
  gearRecommendations: ARIZONA_GEAR_RECOMMENDATIONS,
};

export const SITE_CONFIG = ARIZONA_CONFIG;

export const ARIZONA_PACKING_FAQS = [
  { question: 'What should I pack for Arizona?', answer: 'The non-negotiables are a hydration pack or large water bottles (3L minimum for any desert hike), full sun protection kit (SPF 50+, UPF shirt, wide-brim hat), electrolyte packets for extreme heat days, and ankle-supporting hiking boots for Grand Canyon and Sedona red rock trails. Our interactive checklist covers 60+ items for Arizona\'s desert climate.' },
  { question: 'How much water do I need for the Grand Canyon?', answer: 'The National Park Service recommends 1 liter per hour of hiking in summer heat. A rim-to-river day hike of 6–8 hours means 6–8 liters minimum. More is always right. Grand Canyon has emergency water stations at some points but they can be offline. Carry more than you think you need — rangers pull people out every summer for under-preparation.' },
  { question: 'What power adapter do I need for Arizona?', answer: 'No adapter needed. Arizona uses US standard Type A/B outlets at 120V.' },
  { question: 'Can I buy outdoor gear in Arizona?', answer: 'Yes — REI and other outdoor stores are in Phoenix, Scottsdale, Tucson, and Flagstaff. However, specialty sizes and your preferred brands are better sourced before your trip. Grand Canyon Village has a small general store but limited gear selection at high prices.' },
  { question: 'How many outfits should I pack for Arizona?', answer: 'Pack for 5–7 days with emphasis on technical sun-protection clothing rather than quantity. Laundromats are in every town ($2–4/load). Arizona is casual everywhere — even nicer Scottsdale restaurants are smart-casual.' },
  { question: 'What should I NOT bring to Arizona?', answer: 'Cotton base layers for hiking (holds sweat and gets heavy). Dark-colored clothing for desert hikes (absorbs heat faster). A single standard water bottle instead of a hydration system. And don\'t underestimate the heat — even experienced hikers get into serious trouble in Arizona summers.' },
];
