'use client'
import { ChangeEvent, useState } from 'react';
import { useRouter } from 'next/navigation'
import { fetchSongs } from '../actions';

const SongForm = () => {
    const router = useRouter()

    const [songs, setSongs] = useState([
        { name: '', year: 0, artists: '' },
        { name: '', year: 0, artists: '' },
        { name: '', year: 0, artists: '' },
        { name: '', year: 0, artists: '' },
        { name: '', year: 0, artists: '' }
    ]);

    const handleSubmit = async (e: { preventDefault: () => void; }) => {
        e.preventDefault();
        try {
            const newSongs = await fetchSongs(songs);
            console.log(newSongs);
            localStorage.setItem('songsData', JSON.stringify(newSongs));
            router.push('./')
            // Handle success or navigate to another page
        } catch (error) {
            console.error('Error submitting songs:', error);
        }
    };

    const handleChange = (index: number, event: ChangeEvent<HTMLInputElement>) => {
        const { name, value } = event.target;
        const newSongs = [...songs];
        newSongs[index] = { ...newSongs[index], [name]: name === 'year' ? parseInt(value) || 0 : value };
        setSongs(newSongs);
    };

    return (
        <div className="text-white p-4 rounded-lg shadow-lg max-w-md mx-auto">
            <h2 className="text-2xl font-semibold mb-4 text-center">Enter Songs Data</h2>
            <form onSubmit={handleSubmit}>
                {songs.map((song, index) => (
                    <div key={index} className="bg-gray-800 rounded-lg p-4 mb-4">
                        <div className="mb-4">
                            <input
                                type="text"
                                name="name"
                                placeholder="Song Name"
                                value={song.name}
                                onChange={(e) => handleChange(index, e)}
                                className="bg-gray-700 text-white px-4 py-2 rounded-md w-full focus:outline-none focus:ring focus:border-blue-300"
                            />
                        </div>
                        <div className="mb-4">
                            <input
                                type="number"
                                name="year"
                                placeholder="Year"
                                value={song.year}
                                onChange={(e) => handleChange(index, e)}
                                className="bg-gray-700 text-white px-4 py-2 rounded-md w-full focus:outline-none focus:ring focus:border-blue-300"
                            />
                        </div>
                        <div>
                            <input
                                type="text"
                                name="artists"
                                placeholder="Artists"
                                value={song.artists}
                                onChange={(e) => handleChange(index, e)}
                                className="bg-gray-700 text-white px-4 py-2 rounded-md w-full focus:outline-none focus:ring focus:border-blue-300"
                            />
                        </div>
                    </div>
                ))}
                <button
                    type="submit"
                    className="w-full py-2 px-4 bg-green-600 text-white rounded-lg hover:bg-green-700 transition duration-300 disabled:opacity-50"
                >
                    Recommend Songs
                </button>
            </form>
        </div>
    );
};

export default SongForm;
