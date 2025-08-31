console.log("Loaded updated sidebar.js");
function getSelectedComponents() {
  return JSON.parse(localStorage.getItem("selectedComponents") || "[]");
}

function setSelectedComponents(comps) {
  localStorage.setItem("selectedComponents", JSON.stringify(comps));
}

// NEW: Remove component from sidebar
function removeComponentFromSidebar(componentId) {
  let selectedComponents = getSelectedComponents();
  
  // Remove the component with matching ID
  selectedComponents = selectedComponents.filter(comp => comp.id !== parseInt(componentId));
  
  // Update localStorage
  setSelectedComponents(selectedComponents);
  
  // Re-render the sidebar to reflect changes
  renderSelectedComponents();
  
  // Optional: Update main page UI if on component listing page
  updateMainPageUI(componentId);
}

// NEW: Update main page UI when removing from sidebar
function updateMainPageUI(componentId) {
  // Check if we're on the component listing page (has control elements)
  const controlElement = document.getElementById(`control-${componentId}`);
  if (controlElement) {
    // Get the max quantity for this component (if available)
    const componentItem = controlElement.closest('.component-item');
    if (componentItem) {
      // Extract max quantity from the available text or button attributes
      const availableText = componentItem.querySelector('div:nth-child(2)').textContent;
      const maxQty = availableText.match(/Available: (\d+)/)?.[1] || '1';
      
      // Reset to Add button
      controlElement.innerHTML = `<button onclick="startQuantityControl('${componentId}', '${maxQty}')">Add</button>`;
    }
  }
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

    // MODIFIED: Add remove button to each component
    componentList.innerHTML += `
      <div class="mb-2 border-bottom pb-2" style="display: flex; justify-content: space-between; align-items: center;">
          <div>
            <p style="margin: 0;"><strong>${name}</strong> - ${quantity}</p>
          </div>
          <button type="button" 
                  onclick="removeComponentFromSidebar(${item.id})" 
                  style="background: #dc3545; color: white; border: none; border-radius: 3px; padding: 2px 6px; cursor: pointer; font-size: 12px;"
                  title="Remove component">
            ×
          </button>
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