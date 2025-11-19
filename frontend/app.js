document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('uploadForm');
    const fileInput = document.getElementById('fileInput');
    const uploadStatus = document.getElementById('uploadStatus');
    const loadMeetingsBtn = document.getElementById('loadMeetings');
    const meetingsList = document.getElementById('meetingsList');

    // Handle file upload
    uploadForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const file = fileInput.files[0];
        if (!file) {
            showStatus('Please select a file to upload', 'error');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        try {
            showStatus('Uploading and processing...', 'success');
            uploadForm.querySelector('button').disabled = true;
            
            const response = await fetch('http://localhost:8000/upload', {
                method: 'POST',
                body: formData
            });
            
            const result = await response.json();
            
            if (response.ok) {
                showStatus(`File uploaded successfully: ${result.filename}`, 'success');
                // Reload meetings after upload
                setTimeout(loadMeetings, 1000);
            } else {
                showStatus(`Upload failed: ${result.detail || 'Unknown error'}`, 'error');
            }
        } catch (error) {
            showStatus(`Upload failed: ${error.message}`, 'error');
        } finally {
            uploadForm.querySelector('button').disabled = false;
        }
    });

    // Load meetings
    loadMeetingsBtn.addEventListener('click', loadMeetings);

    async function loadMeetings() {
        try {
            meetingsList.innerHTML = '<div class="loading">Loading meetings...</div>';
            
            const response = await fetch('http://localhost:8000/meetings');
            const data = await response.json();
            
            if (response.ok) {
                displayMeetings(data.meetings);
            } else {
                meetingsList.innerHTML = '<div class="error">Failed to load meetings</div>';
            }
        } catch (error) {
            meetingsList.innerHTML = `<div class="error">Error loading meetings: ${error.message}</div>`;
        }
    }

    function displayMeetings(meetings) {
        if (meetings.length === 0) {
            meetingsList.innerHTML = '<p>No meetings found.</p>';
            return;
        }

        const meetingsHtml = meetings.map(meeting => `
            <div class="meeting-item">
                <h3>${meeting.title || 'Untitled Meeting'}</h3>
                <p>Status: ${meeting.status || 'Unknown'}</p>
                <p>Created: ${meeting.created_at ? new Date(meeting.created_at).toLocaleDateString() : 'Unknown'}</p>
                ${meeting.duration ? `<p>Duration: ${meeting.duration} seconds</p>` : ''}
                ${meeting.sentiment_overall ? `<p>Sentiment: ${meeting.sentiment_overall}</p>` : ''}
            </div>
        `).join('');
        
        meetingsList.innerHTML = meetingsHtml;
    }

    function showStatus(message, type) {
        uploadStatus.textContent = message;
        uploadStatus.className = type;
        uploadStatus.style.display = 'block';
        
        // Hide status after 5 seconds
        setTimeout(() => {
            uploadStatus.style.display = 'none';
        }, 5000);
    }

    // Load meetings on page load
    loadMeetings();
});
