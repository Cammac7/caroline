const https = require('https');

// Hardcoded values
const SONG_NAME = 'Hey Jude';
const ARTIST_NAME = 'The Beatles';
const WOMENS_NAME = 'Jude';

function fetchLyrics(artist, song) {
  return new Promise((resolve, reject) => {
    const url = `https://api.lyrics.ovh/v1/${encodeURIComponent(artist)}/${encodeURIComponent(song)}`;
    
    https.get(url, (res) => {
      let data = '';
      
      res.on('data', (chunk) => {
        data += chunk;
      });
      
      res.on('end', () => {
        if (res.statusCode === 200) {
          try {
            const parsed = JSON.parse(data);
            resolve(parsed.lyrics || '');
          } catch (error) {
            reject(new Error('Failed to parse response'));
          }
        } else {
          reject(new Error(`API returned status code ${res.statusCode}`));
        }
      });
    }).on('error', (error) => {
      reject(error);
    });
  });
}

async function checkNameInLyrics() {
  try {
    console.log(`Fetching lyrics for "${SONG_NAME}" by ${ARTIST_NAME}...`);
    
    const lyrics = await fetchLyrics(ARTIST_NAME, SONG_NAME);
    
    if (!lyrics) {
      console.log('No lyrics found for this song.');
      return;
    }
    
    // Case-insensitive search for the name
    const nameRegex = new RegExp(`\\b${WOMENS_NAME}\\b`, 'i');
    const nameAppears = nameRegex.test(lyrics);
    
    console.log(`\nSearching for the name "${WOMENS_NAME}" in the lyrics...`);
    
    if (nameAppears) {
      console.log(`✓ The name "${WOMENS_NAME}" appears in the song lyrics!`);
      
      // Count occurrences
      const matches = lyrics.match(new RegExp(`\\b${WOMENS_NAME}\\b`, 'gi'));
      console.log(`  It appears ${matches.length} time(s) in the song.`);
    } else {
      console.log(`✗ The name "${WOMENS_NAME}" does not appear in the song lyrics.`);
    }
    
  } catch (error) {
    console.error('Error:', error.message);
  }
}

// Run the script
checkNameInLyrics();