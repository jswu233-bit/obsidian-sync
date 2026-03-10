const STOCK_URL = "../stock.yaml";

const state = {
  raw: null,
  query: "",
  onlyLow: false,
};

const els = {
  meta: document.getElementById("meta"),
  health: document.getElementById("health"),
  summary: document.getElementById("summary"),
  urgent: document.getElementById("urgent"),
  cards: document.getElementById("cards"),
  search: document.getElementById("search"),
  onlyLow: document.getElementById("only-low"),
  reload: document.getElementById("reload"),
};

function stockBadge(item) {
  const n = Number(item.current_stock ?? 0);
  if (n <= 1) return `<span class="badge danger">${n}${item.unit || ""}</span>`;
  if (n <= 2) return `<span class="badge low">${n}${item.unit || ""}</span>`;
  return `<span class="badge">${n}${item.unit || ""}</span>`;
}

function stockPercent(item) {
  const n = Number(item.current_stock ?? 0);
  return Math.max(2, Math.min(100, n <= 2 ? n * 20 : Math.log10(n + 1) * 45));
}

function renderSummary(data, visibleItems) {
  const total = data.items?.length || 0;
  const visible = visibleItems.length;
  const lowVisible = visibleItems.filter(i => Number(i.current_stock) <= 2).length;
  const catCount = new Set((visibleItems || []).map(i => i.category)).size;

  els.summary.innerHTML = `
    <div class="metric"><div class="label">总物品数</div><div class="value">${total}</div></div>
    <div class="metric"><div class="label">当前显示</div><div class="value">${visible}</div></div>
    <div class="metric"><div class="label">低库存（当前筛选）</div><div class="value">${lowVisible}</div></div>
    <div class="metric"><div class="label">涉及分类</div><div class="value">${catCount}</div></div>
  `;
}

function renderUrgent(items) {
  const urgent = [...items]
    .filter(i => Number(i.current_stock) <= 2)
    .sort((a, b) => Number(a.current_stock) - Number(b.current_stock))
    .slice(0, 8);

  if (!urgent.length) {
    els.urgent.innerHTML = "";
    return;
  }

  els.urgent.innerHTML = `
    <div class="urgent-box">
      <div class="urgent-title">⚠️ 建议优先补货</div>
      <div class="chips">
        ${urgent.map(i => `<span class="chip">${i.name} · ${i.current_stock}${i.unit || ""}</span>`).join("")}
      </div>
    </div>
  `;
}

function renderCards(data) {
  const items = (data.items || []).filter(item => {
    const matchQ = !state.query || item.name?.includes(state.query);
    const matchLow = !state.onlyLow || Number(item.current_stock) <= 2;
    return matchQ && matchLow;
  });

  renderSummary(data, items);
  renderUrgent(items);

  const groups = (data.categories || []).map(cat => ({
    cat,
    list: items.filter(i => i.category === cat),
  })).filter(g => g.list.length > 0);

  if (groups.length === 0) {
    els.cards.innerHTML = `<p class="empty">没有匹配到库存项，换个关键词试试～</p>`;
    return;
  }

  els.cards.innerHTML = groups.map(g => `
    <article class="card">
      <h3>${g.cat}<span class="count">${g.list.length} 项</span></h3>
      ${g.list.map(item => `
        <div class="item">
          <div>
            <div class="left">${item.name}</div>
            <div class="spec">${item.spec || "-"} · 更新：${item.last_updated || "-"}</div>
          </div>
          <div class="item-right">
            <div>${stockBadge(item)}</div>
            <div class="bar"><span style="width:${stockPercent(item)}%"></span></div>
          </div>
        </div>
      `).join("")}
    </article>
  `).join("");
}

async function loadData() {
  try {
    const res = await fetch(STOCK_URL, { cache: "no-store" });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const yamlText = await res.text();
    const data = jsyaml.load(yamlText);

    state.raw = data;
    const lowCount = (data.items || []).filter(i => Number(i.current_stock) <= 2).length;
    els.health.textContent = lowCount > 0 ? `库存状态：有 ${lowCount} 项偏低` : "库存状态：健康";
    els.meta.textContent = `数据源：inventory/stock.yaml · 最后刷新：${new Date().toLocaleString()}`;
    renderCards(data);
  } catch (e) {
    console.error(e);
    els.meta.textContent = "加载失败：请确认用本地服务器打开（不要直接双击 html）";
    els.cards.innerHTML = `<p class="empty">读取 stock.yaml 失败：${e.message}</p>`;
  }
}

els.search.addEventListener("input", (e) => {
  state.query = e.target.value.trim();
  if (state.raw) renderCards(state.raw);
});

els.onlyLow.addEventListener("change", (e) => {
  state.onlyLow = e.target.checked;
  if (state.raw) renderCards(state.raw);
});

els.reload.addEventListener("click", loadData);

loadData();
