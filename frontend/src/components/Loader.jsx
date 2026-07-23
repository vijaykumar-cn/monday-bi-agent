function Loader() {
  return (
    <div className="flex items-center gap-3 p-4">

      <div className="flex gap-1">

        <div className="w-2 h-2 rounded-full bg-blue-500 animate-bounce"></div>

        <div
          className="w-2 h-2 rounded-full bg-blue-500 animate-bounce"
          style={{ animationDelay: "0.2s" }}
        ></div>

        <div
          className="w-2 h-2 rounded-full bg-blue-500 animate-bounce"
          style={{ animationDelay: "0.4s" }}
        ></div>

      </div>

      <span className="text-gray-500">
        AI is analyzing your data...
      </span>

    </div>
  );
}

export default Loader;