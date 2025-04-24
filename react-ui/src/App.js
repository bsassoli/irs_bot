import React from 'react';
import ChatInterface from './components/ChatInterface';
import { ToastProvider } from './components/ui/toast';

function App() {
  return (
    <ToastProvider>
      <div className="min-h-screen bg-background">
        <div className="container py-4">
          <ChatInterface />
        </div>
      </div>
    </ToastProvider>
  );
}

export default App;