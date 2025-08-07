let selectedComponents = [];
function filterComponents() {
  const search = document.getElementById("searchInput").value.toLowerCase();
  const items = document.getElementsByClassName("component-item");
  let visibleCount = 0;

  for (let item of items) {
    const name = item.getAttribute("data-name");
    const show = name.includes(search);
    item.style.display = show ? "flex" : "none";
    if (show) visibleCount++;
  }

  document.getElementById("noResult").style.display = visibleCount === 0 ? "block" : "none";
}

function startQuantityControl(id, maxQty, name) {
  const controlContainer = document.getElementById(`control-${id}`);
  const safeName = name.replace(/'/g, "\\'").replace(/"/g, '&quot;');

  controlContainer.innerHTML = `
    <div style="display: flex; align-items: center; gap: 10px;">
      <button onclick="decrease(${id}, ${maxQty})">-</button>
      <input type="number" id="qty-${id}" value="1" min="1" max="${maxQty}" style="width: 40px; text-align:center;" readonly>
      <button onclick="increase(${id}, ${maxQty})">+</button>
      <button onclick="addToRequest(this)">✔</button>
    </div>
  `;
}
// function startQuantityControl(id, maxQty, name) {
//   const controlContainer = document.getElementById(`control-${id}`);
//   controlContainer.innerHTML = `
//     <div style="display: flex; align-items: center; gap: 10px;">
//       <button onclick="decrease(${id}, ${maxQty})">-</button>
//       <input id="qty-${id}" type="number" value="1" min="1" max="${maxQty}" style="width: 40px; text-align:center;" readonly>
//       <button onclick="increase(${id}, ${maxQty})">+</button>
//       <button onclick="addToRequest(${id}, '${name.replace(/'/g, "\\'")}')">✔</button>
//     </div>
//   `;
// }


function increase(id, maxQty) {
  const input = document.getElementById("qty-" + id);
  let val = parseInt(input.value);
  if (val < maxQty) input.value = val + 1;
}

function decrease(id, maxQty) {
  const input = document.getElementById("qty-" + id);
  let val = parseInt(input.value);
  if (val > 1) {
    input.value = val - 1;
  } else {
    // Revert to Add button
    const container = document.getElementById("control-" + id);
    container.innerHTML = `<button onclick="startQuantityControl(${id}, ${maxQty})">Add</button>`;
  }
}

function addToRequest(button) {
  const container = button.closest(".component-item");
  const id = parseInt(container.querySelector("[id^='control-']").id.replace("control-", ""));
  const name = container.querySelector("strong").textContent.trim();
  const qty = document.getElementById(`qty-${id}`).value;

  let selectedComponents = JSON.parse(localStorage.getItem("selectedComponents") || "[]");

  if (selectedComponents.some(comp => comp.id === id)) {
    alert("Component already added.");
    return;
  }

  selectedComponents.push({ id: id, name: name, quantity: qty });
  localStorage.setItem("selectedComponents", JSON.stringify(selectedComponents));

  document.getElementById("control-" + id).innerHTML = `
  <span style="color: green;">Added</span>
  <button onclick="removeComponent(${id})" style="margin-left: 10px;">❌ Remove</button>
  `;
}

// function addToRequest(id) {
//   const qty = document.getElementById(`qty-${id}`).value;
//   const name = getComponentName(id);  // auto-extract name from DOM

//   let selectedComponents = JSON.parse(localStorage.getItem("selectedComponents") || "[]");

//   if (selectedComponents.some(comp => comp.id === id)) {
//     alert("Component already added.");
//     return;
//   }

//   selectedComponents.push({ id: id, name: name, quantity: qty });
//   localStorage.setItem("selectedComponents", JSON.stringify(selectedComponents));

//   const container = document.getElementById("control-" + id);
//   container.innerHTML = `<span style="color: green;">Added</span>`;
// }

function getComponentName(id) {
  const item = document.querySelector(`[id="control-${id}"]`).closest(".component-item");
  return item ? item.querySelector("strong").textContent.trim() : `Component ID: ${id}`;
}
function removeComponent(id) {
  let selectedComponents = JSON.parse(localStorage.getItem("selectedComponents") || "[]");
  selectedComponents = selectedComponents.filter(comp => comp.id !== id);
  localStorage.setItem("selectedComponents", JSON.stringify(selectedComponents));

  const controlDiv = document.getElementById("control-" + id);
  controlDiv.innerHTML = `
    <button onclick="changeQty(${id}, -1)">-</button>
    <input type="number" id="qty-${id}" value="1" min="1" readonly style="width: 40px;" />
    <button onclick="changeQty(${id}, 1)">+</button>
    <button onclick="addToRequest(this)">✔</button>
  `;
}
