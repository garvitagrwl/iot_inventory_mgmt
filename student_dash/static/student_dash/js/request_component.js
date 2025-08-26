// request_component.js

document.addEventListener('DOMContentLoaded', function () {
    const toggleBtn = document.getElementById('toggleSidebarBtn');
    const sidebar = document.getElementById('requestSidebar');
    const closeBtn = document.getElementById('closeSidebar');

    if (!toggleBtn || !sidebar || !closeBtn) return;

    toggleBtn.addEventListener('click', function () {
        sidebar.classList.add('open');
        toggleBtn.style.display = 'none';
        renderSelectedComponents();  // comes from shared_component_utils.js
    });

    closeBtn.addEventListener('click', function () {
        sidebar.classList.remove('open');
        toggleBtn.style.display = 'block';
    });
});
