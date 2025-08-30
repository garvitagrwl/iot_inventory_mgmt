// shared_component_utils.js
function getSelectedComponents() {
  return JSON.parse(localStorage.getItem("selectedComponents") || "[]");
}

function setSelectedComponents(comps) {
  localStorage.setItem("selectedComponents", JSON.stringify(comps));
}

function renderSelectedComponents() {
  const componentList = document.getElementById("selected-components-list");
  const formHiddenFields = document.getElementById("form-hidden-fields");

  if (!componentList || !formHiddenFields) return;

  const selected = getSelectedComponents();
  componentList.innerHTML = '';
  formHiddenFields.innerHTML = '';

  if (selected.length === 0) {
    componentList.innerHTML = '<p>No components selected.</p>';
    return;
  }

  selected.forEach(item => {
    const name = item.name || `Component ID: ${item.id}`;
    const quantity = item.quantity || 1;

    componentList.innerHTML += `
      <div class="mb-2 border-bottom pb-2">
          <p><strong>${name}</strong> - ${quantity}</p>
      </div>
    `;

    formHiddenFields.innerHTML += `
      <input type="hidden" name="component_ids[]" value="${item.id}">
      <input type="hidden" name="quantities[]" value="${quantity}">
    `;
  });
}
document.addEventListener('DOMContentLoaded', function() {
    // Check for clear localStorage cookie
    if (document.cookie.indexOf('clearLocalStorage=true') !== -1) {
        localStorage.removeItem('selectedComponents');
        // Clear the cookie
        document.cookie = 'clearLocalStorage=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/';
        console.log('LocalStorage cleared after form submission');
    }
});
document.addEventListener('DOMContentLoaded', function () {
    const toggleBtn = document.getElementById('toggleSidebarBtn');
    const sidebar = document.getElementById('requestSidebar');
    const closeBtn = document.getElementById('closeSidebar');

    if (!toggleBtn || !sidebar || !closeBtn) return;

    toggleBtn.addEventListener('click', function () {
        sidebar.classList.add('open');
        toggleBtn.style.display = 'none';
        renderSelectedComponents();
    });

    closeBtn.addEventListener('click', function () {
        sidebar.classList.remove('open');
        toggleBtn.style.display = 'block';
    });
  });