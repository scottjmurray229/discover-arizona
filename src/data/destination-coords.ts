// Shared destination coordinates — single source of truth
// Used by plan page + companion app + generate-itinerary API.

export const DESTINATION_COORDS: Record<string, { lat: number; lng: number; label: string }> = {
  'grand-canyon': { lat: 36.0544, lng: -112.1401, label: 'Grand Canyon' },
  sedona: { lat: 34.8697, lng: -111.7610, label: 'Sedona' },
  phoenix: { lat: 33.4484, lng: -112.0740, label: 'Phoenix' },
  scottsdale: { lat: 33.4942, lng: -111.9261, label: 'Scottsdale' },
  tucson: { lat: 32.2226, lng: -110.9747, label: 'Tucson' },
  'monument-valley': { lat: 36.9830, lng: -110.0985, label: 'Monument Valley' },
  flagstaff: { lat: 35.1983, lng: -111.6513, label: 'Flagstaff' },
  page: { lat: 36.9147, lng: -111.4558, label: 'Page' },
  'petrified-forest': { lat: 35.0653, lng: -109.7890, label: 'Petrified Forest' },
  'saguaro-national-park': { lat: 32.1797, lng: -111.1661, label: 'Saguaro NP' },
  tombstone: { lat: 31.7129, lng: -110.0676, label: 'Tombstone' },
  bisbee: { lat: 31.4487, lng: -109.9284, label: 'Bisbee' },
};
