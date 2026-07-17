/**
 * Frappe HR Documentation - Main Application Entry Point
 * Initializes all components when the DOM is ready
 *
 * This is compiled to a single JS file (js/app.js) that combines
 * all component logic for use without a module bundler.
 */

// ============================================================
// UTILITIES
// ============================================================

function isMac() {
  return navigator.platform.toUpperCase().indexOf('MAC') >= 0;
}

function getSearchShortcut() {
  return isMac() ? '⌘K' : 'Ctrl+K';
}

// ============================================================
// TECH DROPDOWN
// ============================================================

class TechDropdown {
  constructor(wrapper) {
    this.wrapper = wrapper;
    this.btn = wrapper.querySelector('.tech-dropdown-btn');
    this.menu = wrapper.querySelector('.tech-dropdown-menu');
    this.isOpen = false;
  }
  
  init() {
    if (!this.btn || !this.menu) return;
    
    this.btn.addEventListener('click', (e) => {
      e.stopPropagation();
      this.toggle();
    });
    
    document.addEventListener('click', (e) => {
      if (this.isOpen && !this.btn.contains(e.target) && !this.menu.contains(e.target)) {
        this.close();
      }
    });
  }
  
  toggle() {
    this.isOpen ? this.close() : this.open();
  }
  
  open() {
    this.isOpen = true;
    this.menu.classList.add('is-open');
  }
  
  close() {
    this.isOpen = false;
    this.menu.classList.remove('is-open');
  }
}

function initTechDropdowns() {
  document.querySelectorAll('.tech-dropdown').forEach(wrapper => {
    new TechDropdown(wrapper).init();
  });
}

// ============================================================
// SIDEBAR MANAGER
// ============================================================

class SidebarManager {
  constructor() {
    this.expandedGroups = new Set();
    this.currentPage = this.getCurrentPageFromURL();
    this.STORAGE_KEY = 'frappe-hr-sidebar-expanded';
    this.loadState();
  }

  init() {
    this.attachToggleListeners();
    this.setActivePage();
    this.expandParentOfActivePage();
    this.updateArrowStates();
  }

  getCurrentPageFromURL() {
    const path = window.location.pathname;
    let filename = path.split('/').pop() || 'introduction.html';
    if (!filename) filename = 'introduction.html';
    return filename.replace('.html', '');
  }

  loadState() {
    try {
      const stored = localStorage.getItem(this.STORAGE_KEY);
      if (stored) {
        const parsed = JSON.parse(stored);
        this.expandedGroups = new Set(parsed);
      } else {
        // default expanded
        this.expandedGroups = new Set(['intro', 'org', 'attendance', 'shift', 'mobile']);
      }
    } catch (e) {
      this.expandedGroups = new Set(['intro', 'org', 'attendance', 'shift', 'mobile']);
    }
  }

  saveState() {
    try {
      localStorage.setItem(this.STORAGE_KEY, JSON.stringify(Array.from(this.expandedGroups)));
    } catch (e) {}
  }

  toggleGroup(groupId) {
    const children = document.getElementById(`${groupId}-children`);
    const arrow = document.querySelector(`[data-group-id="${groupId}"] .sidebar-arrow`);
    if (!children) return;

    if (this.expandedGroups.has(groupId)) {
      this.expandedGroups.delete(groupId);
      children.style.display = 'none';
      if (arrow) arrow.classList.remove('expanded');
    } else {
      this.expandedGroups.add(groupId);
      children.style.display = 'block';
      if (arrow) arrow.classList.add('expanded');
    }
    this.saveState();
  }

  attachToggleListeners() {
    document.querySelectorAll('.sidebar-group-btn').forEach((btn) => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const groupId = btn.getAttribute('data-group-id');
        if (groupId) this.toggleGroup(groupId);
      });
    });
  }

  setActivePage() {
    document.querySelectorAll('.sidebar-link.active').forEach((link) => {
      link.classList.remove('active');
      link.removeAttribute('aria-current');
    });

    const activeLink = document.querySelector(`.sidebar-link[data-route="${this.currentPage}"]`);
    if (activeLink) {
      activeLink.classList.add('active');
      activeLink.setAttribute('aria-current', 'page');
    }
  }

  expandParentOfActivePage() {
    const activeLink = document.querySelector('.sidebar-link.active');
    if (!activeLink) return;

    let parent = activeLink.parentElement;
    while (parent) {
      if (parent.classList.contains('sidebar-children')) {
        const groupId = parent.id.replace('-children', '');
        this.expandedGroups.add(groupId);
        parent.style.display = 'block';
        const arrow = document.querySelector(`[data-group-id="${groupId}"] .sidebar-arrow`);
        if (arrow) arrow.classList.add('expanded');
      }
      parent = parent.parentElement;
    }
    this.saveState();
  }

  updateArrowStates() {
    document.querySelectorAll('.sidebar-group-btn').forEach((btn) => {
      const groupId = btn.getAttribute('data-group-id');
      if (!groupId) return;
      const children = document.getElementById(`${groupId}-children`);
      const arrow = btn.querySelector('.sidebar-arrow');

      if (this.expandedGroups.has(groupId)) {
        if (children) children.style.display = 'block';
        if (arrow) arrow.classList.add('expanded');
      } else {
        if (children) children.style.display = 'none';
        if (arrow) arrow.classList.remove('expanded');
      }
    });
  }
}

// ============================================================
// TABLE OF CONTENTS
// ============================================================

class TableOfContents {
  constructor() {
    this.headings = [];
    this.observer = null;
    this.activeId = '';
    this.tocContainer = document.getElementById('wiki-toc-list');
    this.visibleHeadings = new Set();
  }

  init() {
    this.scanHeadings();
    this.renderToc();
    this.initScrollSpy();
    this.attachClickListeners();
  }

  scanHeadings() {
    const content = document.getElementById('wiki-content');
    if (!content) return;

    this.headings = [];
    content.querySelectorAll('h2, h3, h4').forEach((heading) => {
      if (heading.id) {
        this.headings.push({
          id: heading.id,
          text: heading.textContent?.trim() || '',
          level: parseInt(heading.tagName.substring(1), 10),
        });
      }
    });
  }

  renderToc() {
    if (!this.tocContainer || this.headings.length === 0) return;

    this.tocContainer.innerHTML = this.headings
      .map((h) => {
        const paddingLeft = (h.level - 2) * 0.75;
        return `<li><a href="#${h.id}" data-toc-link="${h.id}" class="toc-link toc-h${h.level}" style="padding-left: ${paddingLeft}rem">${this.escapeHtml(h.text)}</a></li>`;
      })
      .join('');
  }

  initScrollSpy() {
    if (this.observer) this.observer.disconnect();
    this.visibleHeadings.clear();

    const els = this.headings.map((h) => document.getElementById(h.id)).filter((el) => el !== null);
    if (els.length === 0) return;

    this.observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            this.visibleHeadings.add(entry.target.id);
          } else {
            this.visibleHeadings.delete(entry.target.id);
          }
        });
        this.updateActiveHeading();
      },
      { rootMargin: '-80px 0px -60% 0px', threshold: 0 }
    );

    els.forEach((el) => this.observer.observe(el));
  }

  updateActiveHeading() {
    let newActiveId = '';
    if (this.visibleHeadings.size > 0) {
      for (const h of this.headings) {
        if (this.visibleHeadings.has(h.id)) { newActiveId = h.id; break; }
      }
    }

    if (newActiveId !== this.activeId) {
      if (this.activeId) {
        document.querySelector(`[data-toc-link="${this.activeId}"]`)?.classList.remove('active');
      }
      if (newActiveId) {
        document.querySelector(`[data-toc-link="${newActiveId}"]`)?.classList.add('active');
      }
      this.activeId = newActiveId;
    }
  }

  attachClickListeners() {
    this.tocContainer?.addEventListener('click', (e) => {
      const link = e.target.closest('.toc-link');
      if (!link) return;
      e.preventDefault();
      const id = link.getAttribute('data-toc-link');
      if (!id) return;
      const heading = document.getElementById(id);
      if (heading) {
        const top = heading.getBoundingClientRect().top + window.scrollY - 80;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  }

  escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }
}

// ============================================================
// SEARCH MODAL
// ============================================================

class SearchModal {
  constructor() {
    this.modal = document.getElementById('search-modal');
    this.overlay = document.getElementById('search-overlay');
    this.input = document.getElementById('search-input');
    this.resultsContainer = document.getElementById('search-results');
    this.emptyState = document.getElementById('search-empty');
    this.isOpen = false;
  }

  init() {
    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        this.open();
      }
      if (e.key === 'Escape' && this.isOpen) this.close();
    });

    document.getElementById('search-btn')?.addEventListener('click', () => this.open());
    document.getElementById('mobile-search-btn')?.addEventListener('click', () => this.open());
    this.overlay?.addEventListener('click', (e) => {
      if (e.target === this.overlay) this.close();
    });
    document.getElementById('search-close')?.addEventListener('click', () => this.close());
    
    this.input?.addEventListener('input', (e) => this.handleSearch(e.target.value));
  }

  handleSearch(query) {
    if (!query.trim()) {
      this.resultsContainer.innerHTML = '';
      this.emptyState.style.display = 'block';
      this.emptyState.textContent = 'Escribe para buscar...';
      return;
    }
    
    this.emptyState.style.display = 'none';
    const q = query.toLowerCase();
    
    if (window.SEARCH_DATA) {
      const results = window.SEARCH_DATA.filter(item => item.title.toLowerCase().includes(q));
      
      if (results.length === 0) {
        this.resultsContainer.innerHTML = '';
        this.emptyState.style.display = 'block';
        this.emptyState.textContent = 'No se encontraron resultados.';
      } else {
        this.resultsContainer.innerHTML = results.map(r => 
          `<a href="${r.route}" class="search-result-item">${r.title}</a>`
        ).join('');
      }
    }
  }

  open() {
    if (!this.modal || !this.overlay) return;
    this.isOpen = true;
    this.modal.classList.add('is-open');
    this.overlay.classList.add('is-open');
    document.body.style.overflow = 'hidden';
    requestAnimationFrame(() => this.input?.focus());
  }

  close() {
    if (!this.modal || !this.overlay) return;
    this.isOpen = false;
    this.modal.classList.remove('is-open');
    this.overlay.classList.remove('is-open');
    document.body.style.overflow = '';
    if (this.input) {
      this.input.value = '';
      this.resultsContainer.innerHTML = '';
      this.emptyState.style.display = 'block';
      this.emptyState.textContent = 'Escribe para buscar...';
    }
  }
}

// ============================================================
// THEME MANAGER
// ============================================================

class ThemeManager {
  constructor() {
    this.STORAGE_KEY = 'wiki-theme';
    const stored = localStorage.getItem(this.STORAGE_KEY);
    this.isDark = stored === 'dark';
  }

  init() {
    this.applyTheme();
    this.updateToggleUI();
    document.getElementById('theme-toggle')?.addEventListener('click', () => this.toggle());
  }

  applyTheme() {
    document.documentElement.setAttribute('data-theme', this.isDark ? 'dark' : 'light');
  }

  toggle() {
    this.isDark = !this.isDark;
    this.applyTheme();
    this.updateToggleUI();
    localStorage.setItem(this.STORAGE_KEY, this.isDark ? 'dark' : 'light');
  }

  updateToggleUI() {
    const knob = document.querySelector('.theme-knob');
    const sunIcon = document.getElementById('theme-sun');
    const moonIcon = document.getElementById('theme-moon');

    if (knob) knob.style.transform = this.isDark ? 'translateX(24px)' : 'translateX(0)';
    if (sunIcon) sunIcon.style.display = this.isDark ? 'none' : 'block';
    if (moonIcon) moonIcon.style.display = this.isDark ? 'block' : 'none';
  }
}

// ============================================================
// MOBILE NAV
// ============================================================

class MobileNav {
  constructor() {
    this.sidebarOpen = false;
    this.menuBtn = document.getElementById('mobile-menu-btn');
    this.sidebar = document.getElementById('mobile-sidebar');
    this.overlay = document.getElementById('mobile-overlay');
  }

  init() {
    this.menuBtn?.addEventListener('click', () => this.toggleSidebar());
    this.overlay?.addEventListener('click', () => this.closeSidebar());
  }

  toggleSidebar() {
    this.sidebarOpen ? this.closeSidebar() : this.openSidebar();
  }

  openSidebar() {
    this.sidebarOpen = true;
    this.sidebar?.classList.add('is-open');
    this.overlay?.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  }

  closeSidebar() {
    this.sidebarOpen = false;
    this.sidebar?.classList.remove('is-open');
    this.overlay?.classList.remove('is-open');
    document.body.style.overflow = '';
  }
}

// ============================================================
// CODE BLOCKS (COPY BUTTON)
// ============================================================

function initCodeBlocks() {
  document.querySelectorAll('.code-block').forEach(block => {
    const copyBtn = block.querySelector('.copy-code-btn');
    const codeEl = block.querySelector('code');
    if (!copyBtn || !codeEl) return;

    copyBtn.addEventListener('click', async () => {
      try {
        const textToCopy = codeEl.innerText || codeEl.textContent;
        await navigator.clipboard.writeText(textToCopy);
        
        // Show success state
        copyBtn.classList.add('copied');
        copyBtn.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>`;
        
        // Reset after 2 seconds
        setTimeout(() => {
          copyBtn.classList.remove('copied');
          copyBtn.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>`;
        }, 2000);
      } catch (err) {
        console.error('Failed to copy text: ', err);
      }
    });
  });
}

// ============================================================
// APP INITIALIZATION
// ============================================================

document.addEventListener('DOMContentLoaded', () => {
  const shortcutEl = document.getElementById('search-shortcut');
  if (shortcutEl) shortcutEl.textContent = getSearchShortcut();

  document.querySelectorAll('.tech-dropdown').forEach(el => new TechDropdown(el).init());

  const sidebar = new SidebarManager();
  sidebar.init();

  const toc = new TableOfContents();
  toc.init();

  const search = new SearchModal();
  search.init();

  const theme = new ThemeManager();
  theme.init();

  const mobileNav = new MobileNav();
  mobileNav.init();

  initCodeBlocks();
});
