document.addEventListener('DOMContentLoaded', () => {
    // DOM elements
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const chatMessages = document.getElementById('chat-messages');
    const sendButton = document.getElementById('send-button');
    const loadingIndicator = document.getElementById('loading-indicator');
    const errorMessage = document.getElementById('error-message');
    const contextPanel = document.getElementById('context-panel');
    const contextContent = document.getElementById('context-content');
    const toggleContext = document.getElementById('toggle-context');

    // State
    let isProcessing = false;
    let currentContext = [];

    // Initialize the app
    initializeApp();

    // Event listeners
    chatForm.addEventListener('submit', handleSubmit);
    toggleContext.addEventListener('click', toggleContextPanel);

    // Functions
    async function initializeApp() {
        showLoading(true);
        try {
            const response = await fetch('/api/initialize', {
                method: 'POST'
            });
            const data = await response.json();
            
            if (data.status === 'success' || data.status === 'already_initialized') {
                showLoading(false);
            } else {
                showError(`Initialization failed: ${data.message}`);
            }
        } catch (error) {
            console.error('Initialization error:', error);
            showError('Failed to initialize the application. Please refresh and try again.');
        }
    }

    async function handleSubmit(event) {
        event.preventDefault();
        
        const query = userInput.value.trim();
        if (!query || isProcessing) return;
        
        // Clear input
        userInput.value = '';
        
        // Show user message
        addMessage('user', query);
        
        // Show processing state
        isProcessing = true;
        sendButton.disabled = true;
        addThinkingIndicator();
        
        try {
            const response = await fetch('/api/query', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ query })
            });
            
            const data = await response.json();
            
            // Remove thinking indicator
            removeThinkingIndicator();
            
            if (data.status === 'success') {
                // Show assistant response
                addMessage('assistant', data.response);
                
                // Update context panel
                updateContextPanel(data.context);
            } else {
                showError(`Query failed: ${data.message}`);
            }
        } catch (error) {
            console.error('Query error:', error);
            removeThinkingIndicator();
            showError('Failed to process your query. Please try again.');
        } finally {
            isProcessing = false;
            sendButton.disabled = false;
        }
    }

    function addMessage(role, content) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${role}`;
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        
        // Process markdown-like formatting
        const formattedContent = formatText(content);
        contentDiv.innerHTML = `<p>${formattedContent}</p>`;
        
        messageDiv.appendChild(contentDiv);
        chatMessages.appendChild(messageDiv);
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function formatText(text) {
        // Simple markdown-like formatting
        // Bold
        text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
        // Italic
        text = text.replace(/\*(.*?)\*/g, '<em>$1</em>');
        // Line breaks
        text = text.replace(/\n/g, '<br>');
        
        return text;
    }

    function addThinkingIndicator() {
        const thinkingDiv = document.createElement('div');
        thinkingDiv.className = 'message assistant thinking';
        thinkingDiv.innerHTML = `
            <div class="message-content">
                <div class="thinking-indicator">
                    <span class="dot"></span>
                    <span class="dot"></span>
                    <span class="dot"></span>
                </div>
            </div>
        `;
        chatMessages.appendChild(thinkingDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function removeThinkingIndicator() {
        const thinkingIndicator = document.querySelector('.thinking');
        if (thinkingIndicator) {
            thinkingIndicator.remove();
        }
    }

    function updateContextPanel(context) {
        // Save current context
        currentContext = context;
        
        // Clear previous context
        contextContent.innerHTML = '';
        
        // Add new context items
        context.forEach((item, index) => {
            const contextItem = document.createElement('div');
            contextItem.className = 'context-item';
            contextItem.textContent = item;
            contextContent.appendChild(contextItem);
        });
        
        // Show context panel
        if (context.length > 0) {
            contextPanel.classList.remove('hidden');
        } else {
            contextPanel.classList.add('hidden');
        }
    }

    function toggleContextPanel() {
        contextPanel.classList.toggle('collapsed');
        contextPanel.classList.toggle('expanded');
    }

    function showLoading(show) {
        if (show) {
            loadingIndicator.classList.remove('hidden');
            chatForm.classList.add('hidden');
        } else {
            loadingIndicator.classList.add('hidden');
            chatForm.classList.remove('hidden');
        }
    }

    function showError(message) {
        errorMessage.querySelector('p').textContent = message;
        errorMessage.classList.remove('hidden');
        showLoading(false);
        
        // Hide error after 5 seconds
        setTimeout(() => {
            errorMessage.classList.add('hidden');
        }, 5000);
    }
});