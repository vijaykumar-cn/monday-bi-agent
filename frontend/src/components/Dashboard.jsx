import { useEffect, useState } from "react";
import { getDashboard } from "../services/dashboard";
import KpiCard from "./KpiCard";
import DashboardCharts from "./DashboardCharts";
import { formatCurrency } from "../utils/format";
function Dashboard() {
  const [data, setData] = useState(null);

  async function loadDashboard() {
    try {
      const res = await getDashboard();
      setData(res);
    } catch (error) {
      console.error(error);
    }
  }

  useEffect(() => {
    loadDashboard();
  }, []);

  if (!data) {
    return (
      <div className="p-6">
        <h2>Loading Dashboard...</h2>
      </div>
    );
  }

  return (
    <div className="p-6 bg-gray-100 h-full overflow-auto">

      <div className="flex justify-between items-center mb-6">

        <h2 className="text-2xl font-bold">
          Dashboard
        </h2>

        <button
          onClick={loadDashboard}
          className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg"
        >
          Refresh
        </button>

      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-5">

        <KpiCard
          title="Total Deals"
          value={data.pipeline.total_deals}
        />

       <KpiCard
    title="Pipeline Value"
    value={formatCurrency(data.pipeline.pipeline_value)}
/>

        <KpiCard
          title="Open Deals"
          value={data.open_deals}
        />

        <KpiCard
    title="Average Deal"
    value={formatCurrency(data.pipeline.average_deal_size)}
/>

      </div>

      <DashboardCharts data={data} />

    </div>
  );
}

export default Dashboard;