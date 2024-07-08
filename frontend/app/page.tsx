'use client';

import SongCard from './components/SongCard';
import { Key } from 'react';

export default function Home() {
  let posts = [];
  const savedSongs = localStorage.getItem('songsData');
  if (savedSongs) {
    posts = JSON.parse(savedSongs);
  }

  const chunkArray = (array: any[], size: number) => {
    return array.reduce((acc, _, index) => {
      if (index % size === 0) {
        acc.push(array.slice(index, index + size));
      }
      return acc;
    }, []);
  };

  // Chunking the posts array into groups of 5
  const chunkedPosts = chunkArray(posts, 5);

  return (
    <div className="flex flex-wrap justify-center">
      {chunkedPosts.length > 0 ? (
        chunkedPosts.map((chunk: any[], chunkIndex: Key | null | undefined) => (
          <div key={chunkIndex} className="flex flex-wrap justify-center">
            {chunk.map((song: any, index: number) => (
              <SongCard key={index} value={index} song={song} />
            ))}
          </div>
        ))
      ) : (
        <p className="text-white mt-8 text-xl font-semibold">
          No songs found. Please add some songs to the list!
        </p>
      )}
    </div>
  );
}