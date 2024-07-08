import React from 'react';

interface Song {
  name: string;
  artists: string;
  year: number;
}

interface SongCardProps {
  song: Song;
  value: React.Key;
}

const SongCard: React.FC<SongCardProps> = ({ value, song }) => {
  const artistsArray = JSON.parse(song.artists.replace(/'/g, '"'));

  return (
    <div className="max-w-xs rounded-lg overflow-hidden shadow-lg bg-spotifyGreen text-white m-4">
      <img
        className="w-full h-40 object-cover object-center"
        src={`/${value}.jpeg`}
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

export default SongCard;
