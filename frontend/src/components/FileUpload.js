import React, { useState } from 'react';
import axios from 'axios';

const FileUpload = () => {
    const [selectedFile, setSelectedFile] = useState(null);
    const [summary, setSummary] = useState('');

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    const handleUpload = async () => {
        const formData = new FormData();
        formData.append('files', selectedFile);

        try {
            const uploadResponse = await axios.post('http://localhost:8000/upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });

            const filePath = uploadResponse.data.file_paths[0];
            const summaryResponse = await axios.post('http://localhost:8000/summarize', { file_path: filePath }, {
                headers: {
                    'Content-Type': 'application/json',
                },
            });
            setSummary(summaryResponse.data.summary);
        } catch (error) {
            console.error('Error uploading file:', error);
        }
    };

    return (
        <div>
            <h1>Document Summarizer</h1>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload and Summarize</button>
            <p>This may take upto 2 min.</p>
            {summary && (
                <>
                    <h2>Summary:</h2>
                    <p>{summary}</p>
                </>
            )}
        </div>
    );
};

export default FileUpload;
