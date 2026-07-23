import {
  ResponsiveContainer,
  BarChart,
  Bar,
  PieChart,
  Pie,
  Cell,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
} from "recharts";

function objectToArray(obj) {
  if (!obj) return [];

  return Object.entries(obj).map(([name, value]) => ({
    name,
    value,
  }));
}

function DashboardCharts({ data }) {
  const stageData = objectToArray(data.pipeline_by_stage);
  const statusData = objectToArray(data.deal_status);
  const sectorData = objectToArray(data.revenue_by_sector);
  const ownerData = objectToArray(data.top_owners);

  const colors = [
    "#2563eb",
    "#16a34a",
    "#f59e0b",
    "#ef4444",
    "#8b5cf6",
    "#06b6d4",
  ];

  return (
    <div className="grid grid-cols-2 gap-6 mt-8">

      {/* Pipeline by Stage */}
      <div className="bg-white rounded-xl shadow p-5">
        <h2 className="font-bold mb-4">Pipeline by Stage</h2>

        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={stageData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="value" fill="#2563eb" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* Deal Status */}
      <div className="bg-white rounded-xl shadow p-5">
        <h2 className="font-bold mb-4">Deal Status</h2>

        <ResponsiveContainer width="100%" height={300}>
          <PieChart>
            <Pie
              data={statusData}
              dataKey="value"
              nameKey="name"
              outerRadius={100}
              label
            >
              {statusData.map((_, index) => (
                <Cell
                  key={index}
                  fill={colors[index % colors.length]}
                />
              ))}
            </Pie>

            <Tooltip />
            <Legend />
          </PieChart>
        </ResponsiveContainer>
      </div>

      {/* Revenue by Sector */}
      <div className="bg-white rounded-xl shadow p-5">
        <h2 className="font-bold mb-4">Revenue by Sector</h2>

        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={sectorData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="value" fill="#16a34a" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* Top Owners */}
      <div className="bg-white rounded-xl shadow p-5">
        <h2 className="font-bold mb-4">Top Owners</h2>

        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={ownerData} layout="vertical">
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis type="number" />
            <YAxis dataKey="name" type="category" />
            <Tooltip />
            <Bar dataKey="value" fill="#8b5cf6" />
          </BarChart>
        </ResponsiveContainer>
      </div>

    </div>
  );
}

export default DashboardCharts;