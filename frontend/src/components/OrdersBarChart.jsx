import React from "react";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

export default function OrdersBarChart({ data }) {
  if (!data || !data.length) return <p>No data available.</p>;

  return (
    <div style={{ width: "100%", height: 350 }}>
      <h3 style={{ textAlign: "center", marginBottom: 10 }}>
        Order Status Overview
      </h3>

      <ResponsiveContainer>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="status" />
          <YAxis allowDecimals={false} />
          <Tooltip />
          <Legend />
          <Bar dataKey="count" fill="#0088FE" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
