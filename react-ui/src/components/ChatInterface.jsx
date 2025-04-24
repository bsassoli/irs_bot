import React, { useState, useRef, useEffect } from 'react';
import { Button } from './ui/button';
import { Input } from './ui/input';
import { Avatar, AvatarFallback, AvatarImage } from './ui/avatar';
import ChatMessage from './ChatMessage';
import { Send } from 'lucide-react';

export default function ChatInterface() {
  const [messages, setMessages] = useState([
    { id: "welcome-message", text: "Welcome to the Philosophy of Science Assistant. I can answer questions about concepts from the Recipes for Science textbook. What would you like to know?", isUser: false }
  ]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [sourceContext, setSourceContext] = useState([]);
  const [isSourceExpanded, setIsSourceExpanded] = useState(false);
  const [isInitialized, setIsInitialized] = useState(false);
  
  const messagesEndRef = useRef(null);

  useEffect(() => {
    // Initialize the app when component mounts
    const initializeApp = async () => {
      try {
        setIsLoading(true);
        console.log('Initializing app...');
        
        const response = await fetch('/api/initialize', {
          method: 'POST',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          }
        });
        
        console.log('Response status:', response.status);
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        const contentType = response.headers.get('content-type');
        if (!contentType || !contentType.includes('application/json')) {
          console.error('Response is not JSON:', contentType);
          throw new Error('Server returned non-JSON response');
        }
        
        const text = await response.text();
        console.log('Response body:', text);
        
        let data;
        try {
          data = JSON.parse(text);
        } catch (e) {
          console.error('Error parsing JSON response:', e);
          throw new Error('Invalid JSON response from server');
        }
        
        if (data.status === 'success' || data.status === 'already_initialized') {
          console.log('Initialization successful');
          setIsInitialized(true);
        } else {
          console.error('Initialization failed:', data.message);
          addSystemMessage(`Error: ${data.message}. Please reload the page.`);
        }
      } catch (error) {
        console.error('Initialization error:', error);
        addSystemMessage(`Error initializing the application: ${error.message}. Please reload the page.`);
      } finally {
        setIsLoading(false);
      }
    };

    initializeApp();
  }, []);

  useEffect(() => {
    // Scroll to bottom when messages change
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  // Use a UUID-like function to generate unique IDs
  const generateUniqueId = () => {
    return `msg_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  };

  const addSystemMessage = (text) => {
    setMessages(prev => [...prev, { id: generateUniqueId(), text, isUser: false }]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!inputValue.trim() || isLoading || !isInitialized) return;
    
    const userInput = inputValue.trim();
    setInputValue('');
    
    // Add user message
    setMessages(prev => [...prev, { id: generateUniqueId(), text: userInput, isUser: true }]);
    
    // Show thinking indicator
    setIsLoading(true);
    
    try {
      console.log('Sending query:', userInput);
      
      const response = await fetch('/api/query', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: userInput }),
      });
      
      console.log('Query response status:', response.status);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      
      const contentType = response.headers.get('content-type');
      if (!contentType || !contentType.includes('application/json')) {
        console.error('Response is not JSON:', contentType);
        throw new Error('Server returned non-JSON response');
      }
      
      const text = await response.text();
      console.log('Response body length:', text.length);
      
      let data;
      try {
        data = JSON.parse(text);
      } catch (e) {
        console.error('Error parsing JSON response:', e);
        throw new Error('Invalid JSON response from server');
      }
      
      if (data.status === 'success') {
        console.log('Query successful');
        // Add assistant response
        addSystemMessage(data.response);
        
        // Update source context
        setSourceContext(data.context || []);
      } else {
        console.error('Query failed:', data.message);
        addSystemMessage(`Error: ${data.message}. Please try again.`);
      }
    } catch (error) {
      console.error('Query error:', error);
      addSystemMessage(`Error processing your query: ${error.message}. Please try again.`);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-[calc(100vh-2rem)] max-w-3xl mx-auto">
      <div className="flex-none py-4 px-4 border-b">
        <h1 className="text-2xl font-bold text-center text-primary">Philosophy of Science Assistant</h1>
        <p className="text-center text-muted-foreground">Ask questions about the Recipes for Science textbook</p>
      </div>
      
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map(message => (
          <ChatMessage 
            key={message.id} 
            message={message} 
            isUser={message.isUser} 
          />
        ))}
        
        {isLoading && (
          <div className="flex gap-3">
            <Avatar className="h-8 w-8">
              <AvatarFallback className="bg-primary/10 text-primary">AI</AvatarFallback>
            </Avatar>
            <div className="bg-muted rounded-lg px-4 py-3 max-w-[80%]">
              <div className="flex space-x-2">
                <div className="h-2 w-2 bg-primary/50 rounded-full animate-bounce"></div>
                <div className="h-2 w-2 bg-primary/50 rounded-full animate-bounce delay-75"></div>
                <div className="h-2 w-2 bg-primary/50 rounded-full animate-bounce delay-150"></div>
              </div>
            </div>
          </div>
        )}
        
        <div ref={messagesEndRef} />
      </div>
      
      {sourceContext.length > 0 && (
        <div className="flex-none border-t">
          <div className="p-2 flex justify-between items-center">
            <h3 className="text-sm font-medium">Source Context</h3>
            <Button variant="ghost" size="sm" onClick={() => setIsSourceExpanded(!isSourceExpanded)}>
              {isSourceExpanded ? 'Hide Sources' : 'Show Sources'}
            </Button>
          </div>
          
          {isSourceExpanded && (
            <div className="max-h-48 overflow-y-auto p-2 space-y-2">
              {sourceContext.map((source, index) => (
                <div key={index} className="text-xs bg-muted p-2 rounded">
                  {source}
                </div>
              ))}
            </div>
          )}
        </div>
      )}
      
      <div className="flex-none p-4 border-t">
        <form onSubmit={handleSubmit} className="flex gap-2">
          <Input
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            placeholder="Ask a question about philosophy of science..."
            disabled={isLoading || !isInitialized}
            className="flex-1"
          />
          <Button type="submit" disabled={isLoading || !isInitialized || !inputValue.trim()}>
            <Send className="h-4 w-4" />
          </Button>
        </form>
      </div>
    </div>
  );
}