export default function StatsCard({ title, value, icon }) {
return (
<div className="bg-white shadow rounded-lg p-6 text-center">
<div className="text-4xl mb-2">{icon}</div>
<h2 className="text-lg font-medium">{title}</h2>
<p className="text-3xl font-bold mt-2">{value}</p>
</div>
)}