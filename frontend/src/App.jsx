import { useState, useEffect } from "react"

// Deploy edilince Vercel/Netlify'da VITE_API_URL environment variable'i ile
// gercek backend adresi set edilir. Lokal gelistirmede localhost kullanilir.
const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000"

function App() {
  const [invoices, setInvoices] = useState([])
  const [form, setForm] = useState({
    recipient: "", seller: "", product: "",
    quantity: "", unit_price: "", vat_rate: ""
  })

  const fetchInvoices = async () => {
    const res = await fetch(`${API_URL}/invoices`)
    const data = await res.json()
    setInvoices(data)
  }

  useEffect(() => {
    fetchInvoices()
  }, [])

  const handleSubmit = async () => {
    await fetch(`${API_URL}/invoices`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        ...form,
        quantity: parseInt(form.quantity),
        unit_price: parseFloat(form.unit_price),
        vat_rate: parseFloat(form.vat_rate)
      })
    })
    setForm({ recipient: "", seller: "", product: "", quantity: "", unit_price: "", vat_rate: "" })
    fetchInvoices()
  }

  return (
    <div style={{ maxWidth: 700, margin: "40px auto", fontFamily: "sans-serif" }}>
      <h1>Invoice Creator</h1>

      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 10, marginBottom: 20 }}>
        {["recipient", "seller", "product", "quantity", "unit_price", "vat_rate"].map(field => (
          <input
            key={field}
            placeholder={field.replace("_", " ")}
            value={form[field]}
            onChange={e => setForm({ ...form, [field]: e.target.value })}
            style={{ padding: 8, fontSize: 14 }}
          />
        ))}
      </div>

      <button onClick={handleSubmit} style={{ padding: "10px 24px", fontSize: 14, marginBottom: 30 }}>
        Create Invoice
      </button>

      <h2>Invoices</h2>
      <table width="100%" style={{ borderCollapse: "collapse" }}>
        <thead>
          <tr style={{ background: "#f0f0f0" }}>
            {["Recipient", "Seller", "Product", "Qty", "Unit Price", "VAT%", "Total", "Date"].map(h => (
              <th key={h} style={{ padding: 8, textAlign: "left", border: "1px solid #ddd" }}>{h}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {invoices.map(inv => (
            <tr key={inv.id}>
              <td style={{ padding: 8, border: "1px solid #ddd" }}>{inv.recipient}</td>
              <td style={{ padding: 8, border: "1px solid #ddd" }}>{inv.seller}</td>
              <td style={{ padding: 8, border: "1px solid #ddd" }}>{inv.product}</td>
              <td style={{ padding: 8, border: "1px solid #ddd" }}>{inv.quantity}</td>
              <td style={{ padding: 8, border: "1px solid #ddd" }}>{inv.unit_price}</td>
              <td style={{ padding: 8, border: "1px solid #ddd" }}>{inv.vat_rate}%</td>
              <td style={{ padding: 8, border: "1px solid #ddd" }}>{inv.total} TL</td>
              <td style={{ padding: 8, border: "1px solid #ddd" }}>{inv.date}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default App