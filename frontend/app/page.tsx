import { Key } from "react";

interface Song {
  name: string;
  artists: string;
  year: number;
}

// Define props interface for SongCard component
interface SongCardProps {
  song: Song;
}

// SongCard component
const SongCard: React.FC<SongCardProps> = ({ song }) => {
  // Parse the artists string into an array
  const artistsArray = JSON.parse(song.artists.replace(/'/g, '"'));

  return (
    <div className="max-w-xs rounded-lg overflow-hidden shadow-lg bg-spotifyGreen text-white m-4">
      <img
        className="w-full h-40 object-cover object-center"
        src="https://via.placeholder.com/400x200"
        alt="Song Cover"
      />
      <div className="px-6 py-4">
        <div className="font-semibold text-lg mb-2">{song.name}</div>
        <p className="text-sm text-spotifyBlack font-semibold mb-2">
          {artistsArray.join(', ')}
        </p>
        <p className="text-sm text-spotifyBlack font-semibold">{song.year}</p>
      </div>
    </div>
  );
};

export default async function Home() {
  const { posts } = await getData()
  return (
    <div className="flex flex-wrap justify-center bg-spotifyBlack">
      {posts.map((song: any, index: Key | null | undefined) => (
        <SongCard key={index} song={song} />
      ))}
    </div>
  )
}

async function getData() {
  const res = await fetch('http://127.0.0.1:5001/recommend');
  const posts = await res.json();
  console.log(posts)
  // By returning { props: { posts } }, the component will receive `posts` as a prop at build time
  if (!res.ok) {
    // This will activate the closest `error.js` Error Boundary
    throw new Error('Failed to fetch data')
  }

  return {
    posts
  }
}