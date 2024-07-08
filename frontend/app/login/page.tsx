'use client'

import { useState } from 'react';
import { useRouter } from 'next/navigation'; // Import from 'next/router' instead of 'next/navigation'
import Link from 'next/link'; 
import { authenticate } from '../actions';

export default function Page() {
    const [errorMessage, setErrorMessage] = useState<string | null>(null);
    const [pending, setPending] = useState(false);
    const router = useRouter();

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        const formData = new FormData(event.currentTarget);

        try {
            setPending(true);
            const auth = await authenticate(formData);
            if (auth) {
                router.push('./form');
            } else {
                setErrorMessage('Invalid credentials.');
            }
        } catch (error) {
            setErrorMessage('Something went wrong.');
        } finally {
            setPending(false);
        }
    };

    const handleClick = (event: React.MouseEvent<HTMLButtonElement, MouseEvent>) => {
        if (pending) {
            event.preventDefault();
        }
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-black">
            <div className="bg-gray-900 p-8 rounded-lg shadow-lg w-full max-w-md">
                <h2 className="text-2xl font-semibold mb-6 text-center text-white">Enter your credentials</h2>
                <form onSubmit={handleSubmit} className="space-y-6">
                    <div>
                        <input
                            type="email"
                            name="email"
                            placeholder="Email"
                            required
                            className="w-full px-4 py-2 border border-gray-700 rounded-lg bg-gray-800 text-white focus:outline-none focus:ring-2 focus:ring-green-500"
                        />
                    </div>
                    <div>
                        <input
                            type="password"
                            name="password"
                            placeholder="Password"
                            required
                            className="w-full px-4 py-2 border border-gray-700 rounded-lg bg-gray-800 text-white focus:outline-none focus:ring-2 focus:ring-green-500"
                        />
                    </div>
                    {errorMessage && <p className="text-red-500 text-sm">{errorMessage}</p>}
                    <div>
                        <button
                            aria-disabled={pending}
                            type="submit"
                            onClick={handleClick}
                            className="w-full py-2 px-4 bg-green-600 text-white rounded-lg hover:bg-green-700 transition duration-300 disabled:opacity-50"
                        >
                            Login
                        </button>
                    </div>
                    <div className="text-center text-gray-400 text-sm">
                        Don't have an account?{' '}
                        <Link href="/signup" className="text-green-500 hover:text-green-400">
                            Click here
                        </Link>
                    </div>
                </form>
            </div>
        </div>
    );
}
