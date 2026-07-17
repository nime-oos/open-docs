/**
 * Frappe HR Documentation - Theme Toggle Component
 * Manages light/dark theme with localStorage persistence
 */

class ThemeManager {
  private readonly STORAGE_KEY = 'wiki-theme';
  private isDark: boolean = false;

  constructor() {
    this.loadTheme();
  }

  /**
   * Initialize - apply stored theme and attach toggle listener
   */
  init(): void {
    this.applyTheme();
    this.attachToggleListener();
    this.updateToggleUI();
  }

  /**
   * Load theme preference from localStorage
   */
  private loadTheme(): void {
    const stored = localStorage.getItem(this.STORAGE_KEY);
    this.isDark = stored === 'dark';
  }

  /**
   * Apply the current theme to the document
   */
  private applyTheme(): void {
    document.documentElement.setAttribute(
      'data-theme',
      this.isDark ? 'dark' : 'light'
    );
  }

  /**
   * Toggle between light and dark themes
   */
  toggle(): void {
    this.isDark = !this.isDark;
    this.applyTheme();
    this.updateToggleUI();
    localStorage.setItem(this.STORAGE_KEY, this.isDark ? 'dark' : 'light');
  }

  /**
   * Update the toggle switch UI to reflect current theme
   */
  private updateToggleUI(): void {
    const knob = document.querySelector('.theme-knob') as HTMLElement;
    const sunIcon = document.getElementById('theme-sun');
    const moonIcon = document.getElementById('theme-moon');

    if (knob) {
      knob.style.transform = this.isDark ? 'translateX(24px)' : 'translateX(0)';
    }

    if (sunIcon && moonIcon) {
      sunIcon.style.display = this.isDark ? 'none' : 'block';
      moonIcon.style.display = this.isDark ? 'block' : 'none';
    }
  }

  /**
   * Attach click listener to theme toggle button
   */
  private attachToggleListener(): void {
    const toggleBtn = document.getElementById('theme-toggle');
    toggleBtn?.addEventListener('click', () => this.toggle());
  }
}

export { ThemeManager };
