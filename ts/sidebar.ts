/**
 * Frappe HR Documentation - Sidebar Navigation Component
 * Handles expand/collapse, active state tracking, and localStorage persistence
 */

interface SidebarGroup {
  id: string;
  title: string;
  children: SidebarItem[];
}

interface SidebarItem {
  title: string;
  href: string;
  route: string;
}

interface NavigationData {
  groups: SidebarGroup[];
}

class SidebarManager {
  private expandedGroups: Set<string>;
  private currentPage: string;
  private readonly STORAGE_KEY = 'frappe-hr-sidebar-expanded';

  constructor() {
    this.expandedGroups = new Set<string>();
    this.currentPage = this.getCurrentPageFromURL();
    this.loadState();
  }

  /**
   * Initialize the sidebar - attach event listeners and set active states
   */
  init(): void {
    this.attachToggleListeners();
    this.setActivePage();
    this.expandParentOfActivePage();
    this.updateArrowStates();
  }

  /**
   * Get current page slug from URL
   */
  private getCurrentPageFromURL(): string {
    const path = window.location.pathname;
    const filename = path.split('/').pop() || 'introduction.html';
    return filename.replace('.html', '');
  }

  /**
   * Load expanded state from localStorage
   */
  private loadState(): void {
    try {
      const stored = localStorage.getItem(this.STORAGE_KEY);
      if (stored) {
        const parsed = JSON.parse(stored) as string[];
        this.expandedGroups = new Set(parsed);
      }
    } catch {
      // Silently fail if localStorage is unavailable
    }
  }

  /**
   * Save expanded state to localStorage
   */
  private saveState(): void {
    try {
      const arr = Array.from(this.expandedGroups);
      localStorage.setItem(this.STORAGE_KEY, JSON.stringify(arr));
    } catch {
      // Silently fail
    }
  }

  /**
   * Toggle a sidebar group's expanded/collapsed state
   */
  toggleGroup(groupId: string): void {
    const children = document.getElementById(`${groupId}-children`);
    const arrow = document.querySelector(`[data-group-id="${groupId}"] .sidebar-arrow`) as HTMLElement;

    if (!children) return;

    if (this.expandedGroups.has(groupId)) {
      this.expandedGroups.delete(groupId);
      children.style.display = 'none';
      arrow?.classList.remove('expanded');
    } else {
      this.expandedGroups.add(groupId);
      children.style.display = 'block';
      arrow?.classList.add('expanded');
    }

    this.saveState();
  }

  /**
   * Attach click listeners to all sidebar group toggle buttons
   */
  private attachToggleListeners(): void {
    const groupButtons = document.querySelectorAll<HTMLButtonElement>('.sidebar-group-btn');
    groupButtons.forEach((btn) => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const groupId = btn.getAttribute('data-group-id');
        if (groupId) {
          this.toggleGroup(groupId);
        }
      });
    });
  }

  /**
   * Set the active page in the sidebar
   */
  private setActivePage(): void {
    // Remove all active states
    document.querySelectorAll('.sidebar-link.active').forEach((link) => {
      link.classList.remove('active');
      link.removeAttribute('aria-current');
    });

    // Find and activate the current page link
    const activeLink = document.querySelector(
      `.sidebar-link[data-route="${this.currentPage}"]`
    ) as HTMLElement;

    if (activeLink) {
      activeLink.classList.add('active');
      activeLink.setAttribute('aria-current', 'page');
    }
  }

  /**
   * Expand the parent group of the currently active page
   */
  private expandParentOfActivePage(): void {
    const activeLink = document.querySelector('.sidebar-link.active');
    if (!activeLink) return;

    // Walk up the DOM to find the parent group
    let parent = activeLink.parentElement;
    while (parent) {
      if (parent.classList.contains('sidebar-children')) {
        const groupId = parent.id.replace('-children', '');
        this.expandedGroups.add(groupId);
        parent.style.display = 'block';

        const arrow = document.querySelector(
          `[data-group-id="${groupId}"] .sidebar-arrow`
        ) as HTMLElement;
        arrow?.classList.add('expanded');
      }
      parent = parent.parentElement;
    }

    this.saveState();
  }

  /**
   * Update all arrow rotation states based on expanded groups
   */
  private updateArrowStates(): void {
    document.querySelectorAll<HTMLElement>('.sidebar-group-btn').forEach((btn) => {
      const groupId = btn.getAttribute('data-group-id');
      if (!groupId) return;

      const children = document.getElementById(`${groupId}-children`);
      const arrow = btn.querySelector('.sidebar-arrow') as HTMLElement;

      if (this.expandedGroups.has(groupId)) {
        if (children) children.style.display = 'block';
        arrow?.classList.add('expanded');
      } else {
        if (children) children.style.display = 'none';
        arrow?.classList.remove('expanded');
      }
    });
  }
}

export { SidebarManager };
