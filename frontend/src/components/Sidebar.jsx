import {
  LayoutDashboard,
  MessageSquare,
  BarChart3,
  RefreshCw,
  Settings,
} from "lucide-react";

function Sidebar() {
  const menu = [
    {
      icon: <LayoutDashboard size={20} />,
      title: "Dashboard",
    },
    {
      icon: <MessageSquare size={20} />,
      title: "AI Chat",
    },
    {
      icon: <BarChart3 size={20} />,
      title: "Analytics",
    },
    {
      icon: <RefreshCw size={20} />,
      title: "Refresh",
    },
    {
      icon: <Settings size={20} />,
      title: "Settings",
    },
  ];

  return (
    <div className="w-64 bg-slate-900 text-white flex flex-col">

      <div className="p-6 border-b border-slate-700">
        <h1 className="text-2xl font-bold">
          Monday BI
        </h1>

        <p className="text-gray-400 text-sm mt-2">
          AI Business Intelligence
        </p>
      </div>

      <div className="flex-1 mt-4">

        {menu.map((item) => (
          <div
            key={item.title}
            className="flex items-center gap-4 px-6 py-4 hover:bg-slate-800 cursor-pointer transition"
          >
            {item.icon}

            <span>{item.title}</span>
          </div>
        ))}

      </div>

      <div className="p-6 border-t border-slate-700">

        <div className="text-sm text-gray-400">
          Powered by
        </div>

        <div className="font-semibold mt-2">
          FastAPI + NVIDIA AI
        </div>

      </div>

    </div>
  );
}

export default Sidebar;