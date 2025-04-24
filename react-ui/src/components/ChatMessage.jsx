import React from 'react';
import { Avatar, AvatarFallback, AvatarImage } from './ui/avatar';
import ReactMarkdown from 'react-markdown';

export default function ChatMessage({ message, isUser }) {
  return (
    <div className={`flex gap-3 mb-4 ${isUser ? 'justify-end' : 'justify-start'}`}>
      {!isUser && (
        <Avatar className="h-8 w-8">
          <AvatarImage src="/bot-avatar.png" alt="AI" />
          <AvatarFallback className="bg-primary/10 text-primary">AI</AvatarFallback>
        </Avatar>
      )}
      
      <div className={`max-w-[80%] rounded-lg px-4 py-3 ${
        isUser 
          ? 'bg-primary text-primary-foreground' 
          : 'bg-muted'
      }`}>
        {isUser ? (
          <p>{message.text}</p>
        ) : (
          <ReactMarkdown className="prose prose-sm max-w-none dark:prose-invert">
            {message.text}
          </ReactMarkdown>
        )}
      </div>
      
      {isUser && (
        <Avatar className="h-8 w-8">
          <AvatarImage src="/user-avatar.png" alt="User" />
          <AvatarFallback className="bg-primary/10">U</AvatarFallback>
        </Avatar>
      )}
    </div>
  );
}