import Dashboard from "../components/Dashboard";
import ChatBox from "../components/ChatBox";

function Home() {
  return (
    <div className="h-screen bg-gray-100">

      <div className="bg-blue-700 text-white p-4 text-2xl font-bold shadow">
        Monday Business Intelligence Agent
      </div>

      <div className="grid grid-cols-12 h-[calc(100vh-72px)]">

        {/* Dashboard */}

        <div className="col-span-7 overflow-auto border-r bg-gray-100">
          <Dashboard />
        </div>

        {/* Chat */}

        <div className="col-span-5 bg-white">
          <ChatBox />
        </div>

      </div>

    </div>
  );
}

export default Home;