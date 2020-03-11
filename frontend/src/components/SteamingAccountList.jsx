import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function SteamingAccountList() {
    
    const [streamingAccounts, setStreamingAccounts] = useState([]);
    

    useEffect(() => {
        axios.get('/api/streaming-account/')
          .then(res => setStreamingAccounts(res.data))
    }, [])

    return (
        <div>
            <h1>Streaming Accounts</h1>
            <ul>
                {streamingAccounts.map(streamingAccount => (
                    <li key={streamingAccount.id}>
                        {streamingAccount.owner}, {streamingAccount.streaming_service}, {streamingAccount.login}
                    </li>
                ))}
            </ul>
        </div>
    )
}
