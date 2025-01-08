import { useState } from "react";
import { Button } from "./components/ui/button";
import { Input } from "./components/ui/input";
import { ScrollArea } from "./components/ui/scroll-area";
import { Send, Database, Loader2 } from "lucide-react";
import ReactMarkdown from "react-markdown";
import axios from "axios";

interface Message {
  id: number;
  content: string;
  sender: "user" | "assistant";
  timestamp: Date;
}

function App() {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: 1,
      content: "Hello! How can I assist you today?",
      sender: "assistant",
      timestamp: new Date(),
    },
  ]);

  const [newMessage, setNewMessage] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleSend = async () => {
    if (newMessage.trim()) {
      setMessages([
        ...messages,
        {
          id: messages.length + 1,
          content: newMessage,
          sender: "user",
          timestamp: new Date(),
        },
      ]);
      setNewMessage("");
      setIsLoading(true);

      try {
        const response = await axios.post("http://localhost:8000/api/chat", {
          user_query: newMessage,
        });

        setMessages((prevMessages) => [
          ...prevMessages,
          {
            id: prevMessages.length + 1,
            content: response.data,
            sender: "assistant",
            timestamp: new Date(),
          },
        ]);

        setIsLoading(false);
      } catch (error) {
        console.error("Error sending message:", error);
      }
    }
  };

  const formatTime = (date: Date) => {
    return date.toLocaleTimeString("en-US", {
      hour: "numeric",
      minute: "2-digit",
      hour12: true,
    });
  };

  return (
    <div className="flex flex-col h-screen bg-zinc-900">
      <div className="border-b border-zinc-800 bg-zinc-900/95 backdrop-blur supports-[backdrop-filter]:bg-zinc-900/75">
        <div className="flex h-14 items-center px-4">
          <div className="flex items-center gap-2 font-semibold text-zinc-100">
            <Database className="h-5 w-5 text-blue-500" />
            <span>Crust Data</span>
          </div>
        </div>
      </div>

      <ScrollArea className="flex-1 p-4">
        <div className="space-y-6 max-w-2xl mx-auto">
          {messages.map((message) => (
            <div
              key={message.id}
              className={`flex ${
                message.sender === "user" ? "justify-end" : "justify-start"
              }`}
            >
              <div
                className={`max-w-[80%] break-words rounded-lg p-3 word-break break-all ${
                  message.sender === "user"
                    ? "bg-blue-600 text-white"
                    : "bg-zinc-800 text-zinc-100"
                }`}
              >
                <div className="whitespace-pre-wrap">
                  {message.sender === "assistant" ? (
                    <ReactMarkdown className="prose prose-invert max-w-none break-words whitespace-pre-wrap">
                      {message.content}
                    </ReactMarkdown>
                  ) : (
                    <p>{message.content}</p>
                  )}
                </div>
                <span className="text-xs opacity-70 mt-2 block">
                  {formatTime(message.timestamp)}
                </span>
              </div>
            </div>
          ))}
          {isLoading && (
            <div className="flex justify-start">
              <div className="max-w-[80%] break-words rounded-lg p-3 bg-zinc-800 text-zinc-100">
                <div className="flex items-center gap-2">
                  <Loader2 className="h-4 w-4 animate-spin" />
                  <span>Thinking...</span>
                </div>
              </div>
            </div>
          )}
        </div>
      </ScrollArea>

      <div className="p-4 border-t border-zinc-800 bg-zinc-900">
        <div className="flex gap-2 max-w-2xl mx-auto">
          <Input
            placeholder="Type a message..."
            value={newMessage}
            onChange={(e) => setNewMessage(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSend()}
            className="flex-1 bg-zinc-800 border-zinc-700 text-zinc-100"
          />
          <Button
            onClick={handleSend}
            className="bg-blue-600 hover:bg-blue-700"
          >
            <Send className="h-4 w-4" />
          </Button>
        </div>
      </div>
    </div>
  );
}

export default App;
