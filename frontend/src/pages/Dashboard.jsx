import React, { useEffect, useState } from "react";
import StatsCard from "../components/StatsCard";
import ProductsPieChart from "../components/ProductsPieChart";
import OrdersBarChart from "../components/OrdersBarChart";


export default function Dashboard() {
const [products, setProducts] = useState([]);
const [orders, setOrders] = useState([]);
const [staffCount, setStaffCount] = useState(0);
const [loading, setLoading] = useState(true);


useEffect(() => {
async function load(){
const [pRes, oRes, sRes] = await Promise.all([
fetch('/api/products/'),
fetch('/api/orders/'),
fetch('/api/staff-count/')
]);
const [pJson, oJson, sJson] = await Promise.all([pRes.json(), oRes.json(), sRes.json()]);
setProducts(pJson);
setOrders(oJson);
setStaffCount(sJson.count);
setLoading(false);
}
load();
}, []);


if (loading) return <div className="p-8">Loading dashboard...</div>


return (
<div className="p-6">
<header className="mb-6">
<h1 className="text-2xl font-bold">REPLENISH — Dashboard</h1>
</header>


<div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
<StatsCard title="Staff" value={staffCount} icon="👥" />
<StatsCard title="Products" value={products.length} icon="📦" />
<StatsCard title="Orders" value={orders.length} icon="🚚" />
</div>


<div className="grid grid-cols-1 md:grid-cols-2 gap-6">
<ProductsPieChart products={products} />
<OrdersBarChart orders={orders} />
</div>
</div>
);
}

const logout = () => {
  localStorage.removeItem("access");
  localStorage.removeItem("refresh");
  window.location.href = "/login";
};
