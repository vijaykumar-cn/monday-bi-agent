import { useState, useEffect, useRef } from "react";
import api from "../services/api";
import ChatMessage from "./ChatMessage";
import Loader from "./Loader";

function ChatBox() {
  const [message, setMessage] = useState("");

  const [messages, setMessages] = useState(() => {
    const saved = localStorage.getItem("chat_history");
    return saved ? JSON.parse(saved) : [];
  });

  const [loading, setLoading] = useState(false);

  const messagesEndRef = useRef(null);

  useEffect(() => {
    localStorage.setItem("chat_history", JSON.stringify(messages));
  }, [messages]);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loading]);

  async function sendMessage(customMessage = null) {
    const prompt = customMessage || message;

    if (!prompt.trim()) return;

    setMessages((prev) => [
      ...prev,
      {
        sender: "user",
        text: prompt,
      },
    ]);

    setMessage("");
    setLoading(true);

    try {
      const res = await api.post("/chat/", {
        message: prompt,
      });

      setMessages((prev) => [
        ...prev,
        {
          sender: "ai",
          text: res.data.answer,
        },
      ]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          sender: "ai",
          text: "Unable to connect to backend.",
        },
      ]);
    }

    setLoading(false);
  }

  function clearChat() {
    localStorage.removeItem("chat_history");
    setMessages([]);
  }

  const suggestions = [
    "Give me pipeline summary",
    "Show revenue by sector",
    "Which owner has highest deal value?",
    "List all open deals",
  ];

  return (
    <div className="flex flex-col h-full bg-white">

      {/* Header */}

      <div className="flex justify-between items-center p-4 border-b">

        <div>

          <h2 className="text-xl font-bold">
            🤖 Monday BI Assistant
          </h2>

          <p className="text-sm text-gray-500">
            AI Powered Business Intelligence
          </p>

        </div>

        <button
          onClick={clearChat}
          className="text-red-500 hover:text-red-700"
        >
          Clear Chat
        </button>

      </div>

      {/* Messages */}

      <div className="flex-1 overflow-y-auto p-5">

        {messages.length === 0 && (

          <div className="flex flex-col items-center justify-center h-full">

            <h1 className="text-3xl font-bold mb-4">
              Welcome 👋
            </h1>

            <p className="text-gray-500 mb-6">
              Try one of these questions
            </p>

            <div className="grid gap-3 w-full max-w-lg">

              {suggestions.map((q) => (

                <button
                  key={q}
                  onClick={() => sendMessage(q)}
                  className="border rounded-lg p-4 hover:bg-gray-100 text-left"
                >
                  {q}
                </button>

              ))}

            </div>

          </div>

        )}

        {messages.map((msg, index) => (

          <ChatMessage
            key={index}
            sender={msg.sender}
            text={msg.text}
          />

        ))}

        {loading && <Loader />}

        <div ref={messagesEndRef}></div>

      </div>

      {/* Input */}

      <div className="border-t bg-white p-4 flex gap-3">

        <input
          className="flex-1 border rounded-lg p-3 outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Ask anything..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              sendMessage();
            }
          }}
        />

        <button
          onClick={() => sendMessage()}
          disabled={loading}
          className="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white px-6 rounded-lg"
        >
          {loading ? "..." : "Send"}
        </button>

      </div>

    </div>
  );
}

export default ChatBox;