'use server'

export async function fetchSongs(songs = [
  { "name": "Shape of You", "year": 2017, "artists": "Ed Sheeran" },
  { "name": "Havana", "year": 2017, "artists": "Camila Cabello ft. Young Thug" },
  { "name": "Blinding Lights", "year": 2019, "artists": "The Weeknd" },
  { "name": "Shallow", "year": 2018, "artists": "Lady Gaga & Bradley Cooper" },
  { "name": "Bad Guy", "year": 2019, "artists": "Billie Eilish" }
]) {
  // const songs = [
  //   { "name": "Shape of You", "year": 2017, "artists": "Ed Sheeran" },
  //   { "name": "Havana", "year": 2017, "artists": "Camila Cabello ft. Young Thug" },
  //   { "name": "Blinding Lights", "year": 2019, "artists": "The Weeknd" },
  //   { "name": "Shallow", "year": 2018, "artists": "Lady Gaga & Bradley Cooper" },
  //   { "name": "Bad Guy", "year": 2019, "artists": "Billie Eilish" }
  // ];

  const requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ songs })
  };
  const res = await fetch('http://127.0.0.1:5001/recommend', requestOptions);
  if (!res.ok) {
    throw new Error('Failed to fetch data');
  }

  const posts = await res.json();
  return posts;
}

export async function authenticate(formData: FormData) {
  const requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      email: formData.get('email'),
      password: formData.get('password')
    })
  };

  const res = await fetch('http://127.0.0.1:5001/login', requestOptions);
  const auth = await res.json();
  return auth.authenticated;
}

export async function signup(formData: FormData) {
  const requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      email: formData.get('email'),
      password: formData.get('password')
    })
  };

  const res = await fetch('http://127.0.0.1:5001/signup', requestOptions);
  const auth = await res.json();
  return auth.authenticated;
}