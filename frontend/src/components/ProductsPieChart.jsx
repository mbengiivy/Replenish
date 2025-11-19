import React from "react";
import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

export default function ProductsPieChart({ data }) {
  const COLORS = [
    "#FF6384",
    "#36A2EB",
    "#FFCE56",
    "#00C49F",
    "#845EC2",
    "#FF6F91",
    "#FFC75F",
    "#2C73D2",
    "#008F7A",
    "#C34A36",
  ];

  if (!data || !data.length) return <p>No data available.</p>;

  return (
    <div style={{ width: "100%", height: 350 }}>
      <h3 style={{ textAlign: "center", marginBottom: 10 }}>
        Product Quantities
      </h3>

      <ResponsiveContainer>
        <PieChart>
          <Pie
            dataKey="quantity"
            data={data}
            nameKey="name"
            cx="50%"
            cy="50%"
            outerRadius={120}
            label
          >
            {data.map((entry, index) => (
              <Cell key={index} fill={COLORS[index % COLORS.length]} />
            ))}
          </Pie>

          <Tooltip />
          <Legend />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}
