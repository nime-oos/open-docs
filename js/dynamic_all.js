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
    // Build Dropdown
    if (!window.TECHNOLOGIES) window.TECHNOLOGIES = [{id:'frappe',title:'Frappe HR'}];
    
    let dropdownHTML = `
        <button class="tech-dropdown-btn">
            <span style="display:flex; align-items:center; color:var(--color-green-600); margin-right:4px;">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M4 6h16v2H4zm0 5h16v2H4zm0 5h16v2H4z"/></svg>
            </span>
            <span class="header-space-name">Todo en Uno</span>
            <svg class="header-chevron" viewBox="0 0 20 20" fill="currentColor" width="16" height="16"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
        </button>
        <div class="tech-dropdown-menu">
    `;
    window.TECHNOLOGIES.forEach(tech => {
        dropdownHTML += `<a href="docs.html?tech=${tech.id}" class="tech-dropdown-item" style="display:flex; align-items:center; gap:8px;">
            <span style="display:flex; width:16px; justify-content:center; color:var(--ink-gray-6);">${tech.logo || ''}</span>
            ${tech.title}
        </a>`;
    });
    dropdownHTML += `
        <hr style="margin: 4px 0; border-color: var(--outline-gray-1);">
        <a href="all.html" class="tech-dropdown-item" style="color: var(--color-green-600); font-weight: 600;">Todo en Uno</a>
        </div>
    `;
    
    const drop1 = document.querySelector('#spa-dropdown-container') || document.querySelector('.header-left.tech-dropdown:not(#spa-mobile-dropdown-container)');
    const drop2 = document.getElementById('spa-mobile-dropdown-container');
    if (drop1) drop1.innerHTML = dropdownHTML;
    if (drop2) drop2.innerHTML = dropdownHTML;

    const sidebarContainer = document.getElementById('dynamic-sidebar') || document.getElementById('spa-sidebar');
    const contentContainer = document.getElementById('dynamic-content') || document.getElementById('wiki-content');
    if (!sidebarContainer || !contentContainer) return;
    
    let sidebarHTML = '';
    let contentHTML = '';
    
    for (const tech of window.TECHNOLOGIES) {
        try {
            await loadScript(`${tech.id}/config.js`);
        } catch (e) {
            console.error("Could not load", tech.id);
            continue;
        }
        
        const configVar = 'CONFIG_' + tech.id.toUpperCase();
        const data = window[configVar];
        if (!data) continue;
        
        // 1. Build Sidebar
        sidebarHTML += `<div style="padding: 8px; font-weight: bold; color: var(--color-green-600); margin-top: 10px;">${tech.title}</div>`;
        for (const group of data.sidebar) {
            sidebarHTML += `
            <div class="sidebar-group">
                <button class="sidebar-group-btn" data-group-id="${tech.id}-${group.id}-dyn" aria-expanded="true" onclick="dynToggleSidebarGroup(this)">
                    <svg class="sidebar-arrow expanded" viewBox="0 0 12 12" fill="currentColor"><path d="M4 8.54V3.46c0-.4.455-.64.787-.41l3.628 2.54a.5.5 0 010 .82L4.787 8.95A.5.5 0 014 8.54z"/></svg>
                    <span class="sidebar-group-title">${group.title}</span>
                </button>
                <div class="sidebar-children" id="${tech.id}-${group.id}-dyn-children" style="display: block;">
                    <div class="sidebar-list">
            `;
            for (const child of group.children) {
                const childId = `${tech.id}-${child.route.replace('.html', '')}`;
                sidebarHTML += `
                <div class="sidebar-item">
                    <a href="#${childId}" class="sidebar-link">
                        <span class="sidebar-link-title">${child.title}</span>
                    </a>
                </div>
                `;
            }
            sidebarHTML += `</div></div></div>`;
        }
        
        // 2. Build Content
        contentHTML += `<h1 style="color: var(--color-green-700); margin-top: 60px; font-size: 2.5rem; border-bottom: 2px solid var(--color-green-500); padding-bottom: 10px; display:flex; align-items:center; gap:16px;">
          <span style="color:var(--color-green-600); width:40px; height:40px; display:flex;">${tech.logo || ''}</span>
          ${tech.title}
        </h1>`;
        
        for (const route in data.contents) {
            const pageData = data.contents[route];
            const pageId = `${tech.id}-${route.replace('.html', '')}`;
            
            contentHTML += `
            <div id="${pageId}" style="padding-top: 20px; margin-top: -20px;">
                <h2 style="color: var(--color-green-600); margin-top: 40px;">${pageData.title}</h2>
                ${pageData.content}
            </div>
            <hr style="margin: 40px 0;">
            `;
        }
    }
    
    sidebarContainer.innerHTML = sidebarHTML;
    contentContainer.innerHTML = contentHTML;
    document.getElementById('page-title').innerText = "Documentación Completa (Todo en Uno)";
    
    // Add smooth scrolling for sidebar links
    sidebarContainer.querySelectorAll('a.sidebar-link').forEach(link => {
        link.addEventListener('click', (e) => {
            const targetId = link.getAttribute('href').substring(1);
            const targetEl = document.getElementById(targetId);
            if (targetEl) {
                e.preventDefault();
                targetEl.scrollIntoView({ behavior: 'smooth' });
                history.pushState(null, null, `#${targetId}`);
            }
        });
    });
});

window.dynToggleSidebarGroup = function(btn) {
    const isExpanded = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', !isExpanded);
    const arrow = btn.querySelector('.sidebar-arrow');
    if (arrow) {
        if (!isExpanded) {
            arrow.classList.add('expanded');
        } else {
            arrow.classList.remove('expanded');
        }
    }
    
    const targetId = btn.getAttribute('data-group-id') + '-children';
    const target = document.getElementById(targetId);
    if (target) {
        target.style.display = isExpanded ? 'none' : 'block';
    }
};
