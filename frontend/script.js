const chatDiv = document.getElementById('chat');
const inputField = document.getElementById('userInput');
const sendButton = document.getElementById('sendBtn');

// --- Add message ---
function addMessage(role, text, isSpinner = false) {
    const p = document.createElement('p');
    p.className = role;

    if (isSpinner) {
        const spinner = document.createElement('span');
        spinner.className = 'spinner';

        const textSpan = document.createElement('span');
        textSpan.textContent = ' Processing... ';

        const timerSpan = document.createElement('span');
        timerSpan.textContent = '(0s)';

        p.style.display = 'flex';
        p.style.alignItems = 'center';
        p.style.gap = '5px';

        p.appendChild(spinner);
        p.appendChild(textSpan);
        p.appendChild(timerSpan);

        chatDiv.appendChild(p);
        chatDiv.scrollTop = chatDiv.scrollHeight;

        let seconds = 0;
        const interval = setInterval(() => {
            seconds++;
            timerSpan.textContent = `(${seconds}s)`;
        }, 1000);

        return { p, interval };
    } else {
        p.textContent = `${role}: ${text}`;
        chatDiv.appendChild(p);
        chatDiv.scrollTop = chatDiv.scrollHeight;
        return { p };
    }
}

// --- Send message ---
async function sendMessage() {
    const text = inputField.value.trim();
    if (!text) return;

    addMessage('user', text);
    inputField.value = '';
    inputField.focus();

    const { p: spinnerMsg, interval } = addMessage('assistant', '', true);

    try {
        const response = await fetch('http://127.0.0.1:8000/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text })
        });

        // Make sure response is JSON
        const data = await response.json();

        clearInterval(interval);

        // Safely set text
        spinnerMsg.textContent = `assistant: ${data.reply}`;

        chatDiv.scrollTop = chatDiv.scrollHeight;
    } catch (error) {
        clearInterval(interval);
        spinnerMsg.textContent = 'assistant: Error: Could not reach backend.';
        console.error(error);
    }
}

// --- Event listeners ---
sendButton.addEventListener('click', sendMessage);

inputField.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
        e.preventDefault();
    }
});
