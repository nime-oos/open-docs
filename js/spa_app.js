function loadScript(src) {
    return new Promise((resolve, reject) => {
        const s = document.createElement('script');
        s.src = src;
        s.onload = resolve;
        s.onerror = reject;
        document.head.appendChild(s);
    });
}

document.addEventListener('DOMContentLoaded', async () => {
    const urlParams = new URLSearchParams(window.location.search);
    let currentTech = urlParams.get('tech') || 'frappe';
    let currentPage = urlParams.get('page') || 'introduction';
    
    if (!window.TECHNOLOGIES) window.TECHNOLOGIES = [{id:'frappe',title:'Frappe HR', logo: ''}];

    const activeTechObj = window.TECHNOLOGIES.find(t => t.id === currentTech) || window.TECHNOLOGIES[0];

    // Build Dropdown
    let dropdownHTML = `
        <button class="tech-dropdown-btn">
            <span style="display:flex; align-items:center; color:var(--color-green-600); margin-right:4px;">${activeTechObj.logo || ''}</span>
            <span class="header-space-name">${activeTechObj.title}</span>
            <svg class="header-chevron" viewBox="0 0 20 20" fill="currentColor" width="16" height="16"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
        </button>
        <div class="tech-dropdown-menu">
    `;
    window.TECHNOLOGIES.forEach(tech => {
        dropdownHTML += `<a href="?tech=${tech.id}" class="tech-dropdown-item" style="display:flex; align-items:center; gap:8px;">
            <span style="display:flex; width:16px; justify-content:center; color:var(--ink-gray-6);">${tech.logo || ''}</span>
            ${tech.title}
        </a>`;
    });
    dropdownHTML += `</div>`;
    
    const drop1 = document.getElementById('spa-dropdown-container');
    const drop2 = document.getElementById('spa-mobile-dropdown-container');
    if (drop1) drop1.innerHTML = dropdownHTML;
    if (drop2) drop2.innerHTML = dropdownHTML;

    try {
        await loadScript(`${currentTech}/config.js`);
    } catch (e) {
        document.getElementById('wiki-content').innerHTML = `<p>Error loading configuration for ${currentTech}. Make sure the folder exists.</p>`;
        return;
    }

    const configVar = 'CONFIG_' + currentTech.toUpperCase();
    const config = window[configVar];
    if (!config) return;

    let allPages = [];
    config.sidebar.forEach(group => {
        if (group.children) {
            group.children.forEach(child => allPages.push(child));
        }
    });

    let currentRoute = currentPage + '.html';
    if (currentPage !== 'all') {
        const pageRoute = currentPage + '.html';
        if (!config.contents[pageRoute] && allPages.length > 0) {
            currentPage = allPages[0].route.replace('.html', '');
            currentRoute = currentPage + '.html';
        }
    }

    // Build Sidebar
        let sidebarHTML = `
      <div style="padding: 12px 16px 20px 16px; border-bottom: 1px solid var(--outline-gray-1); margin-bottom: 16px;">
        <a href="?tech=${currentTech}&page=all" class="btn btn-secondary" style="width: 100%; display: flex; justify-content: center; align-items: center; gap: 8px; font-size: 0.875rem; padding: 10px 16px; border-radius: 8px; background-color: var(--surface-gray-1);">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
            <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
          </svg>
          Vista Continua
        </a>
      </div>
    `;
    config.sidebar.forEach(group => {
        sidebarHTML += `
          <div class="sidebar-group">
            <button class="sidebar-group-btn" data-group-id="${group.id}" aria-expanded="true">
              <svg class="sidebar-arrow expanded" viewBox="0 0 12 12" fill="currentColor"><path d="M4 8.54V3.46c0-.4.455-.64.787-.41l3.628 2.54a.5.5 0 010 .82L4.787 8.95A.5.5 0 014 8.54z"/></svg>
              <span class="sidebar-group-title">${group.title}</span>
            </button>
            <div class="sidebar-children" id="${group.id}-children" style="display: block;">
              <div class="sidebar-list">
        `;
        group.children.forEach(child => {
            const childRoute = child.route.replace('.html', '');
            const isActive = child.route === currentRoute ? 'active' : '';
            sidebarHTML += `
            <div class="sidebar-item">
              <a href="?tech=${currentTech}&page=${childRoute}" class="sidebar-link ${isActive}">
                <span class="sidebar-link-title">${child.title}</span>
              </a>
            </div>
            `;
        });
        sidebarHTML += `</div></div></div>`;
    });
    
    document.getElementById('spa-sidebar').innerHTML = sidebarHTML;

    document.querySelectorAll('.sidebar-group-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const expanded = this.getAttribute('aria-expanded') === 'true';
            this.setAttribute('aria-expanded', !expanded);
            const arrow = this.querySelector('.sidebar-arrow');
            if(arrow) arrow.classList.toggle('expanded');
            const targetId = this.getAttribute('data-group-id') + '-children';
            const target = document.getElementById(targetId);
            if(target) target.style.display = expanded ? 'none' : 'block';
        });
    });

    // Content
    if (currentPage === 'all') {
        document.title = `Todo en Uno - ${config.title}`;
        document.getElementById('page-title').innerText = `Manual Completo: ${config.title}`;
        
        let allContentHTML = '';
        for (const route in config.contents) {
            const pageData = config.contents[route];
            const pageId = route.replace('.html', '');
            allContentHTML += `
            <div id="${pageId}" style="padding-top: 20px;">
                <h2 style="color: var(--color-green-600); border-bottom: 1px solid var(--outline-gray-1); padding-bottom: 8px; margin-top: 40px;">${pageData.title}</h2>
                ${pageData.content}
            </div>
            `;
        }
        document.getElementById('wiki-content').innerHTML = allContentHTML;
    } else {
        const pageData = config.contents[currentRoute] || { title: 'No encontrado', content: '<p>Página no encontrada.</p>' };
        document.title = `${pageData.title} - ${config.title}`;
        document.getElementById('page-title').innerText = pageData.title;
        document.getElementById('wiki-content').innerHTML = pageData.content;
    }

    // Prev / Next Nav
    const currentIndex = allPages.findIndex(p => p.route === currentRoute);
    let navHTML = '';
    if (currentIndex > 0) {
        const prev = allPages[currentIndex - 1];
        navHTML += `<a href="?tech=${currentTech}&page=${prev.route.replace('.html','')}" class="page-nav-link prev"><svg class="page-nav-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg><div class="page-nav-text"><span class="page-nav-label">Anterior</span><span class="page-nav-title">${prev.title}</span></div></a>`;
    }
    if (currentIndex !== -1 && currentIndex < allPages.length - 1) {
        const next = allPages[currentIndex + 1];
        navHTML += `<a href="?tech=${currentTech}&page=${next.route.replace('.html','')}" class="page-nav-link next"><div class="page-nav-text"><span class="page-nav-label">Siguiente</span><span class="page-nav-title">${next.title}</span></div><svg class="page-nav-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg></a>`;
    }
    document.getElementById('spa-nav-links').innerHTML = currentPage === 'all' ? '' : navHTML;

    window.dispatchEvent(new Event('spa-content-loaded'));
});
