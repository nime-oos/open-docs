/**
 * Frappe HR Documentation - Search Modal Component
 * Handles Ctrl+K keyboard shortcut and modal open/close
 */

class SearchModal {
  private modal: HTMLElement | null = null;
  private overlay: HTMLElement | null = null;
  private input: HTMLInputElement | null = null;
  private isOpen: boolean = false;

  constructor() {
    this.modal = document.getElementById('search-modal');
    this.overlay = document.getElementById('search-overlay');
    this.input = document.getElementById('search-input') as HTMLInputElement;
  }

  /**
   * Initialize - attach keyboard shortcuts and click handlers
   */
  init(): void {
    // Keyboard shortcut: Ctrl+K or Cmd+K
    document.addEventListener('keydown', (e: KeyboardEvent) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        this.open();
      }

      if (e.key === 'Escape' && this.isOpen) {
        this.close();
      }
    });

    // Search button click
    const searchBtn = document.getElementById('search-btn');
    searchBtn?.addEventListener('click', () => this.open());

    // Overlay click to close
    this.overlay?.addEventListener('click', () => this.close());

    // Close button
    const closeBtn = document.getElementById('search-close');
    closeBtn?.addEventListener('click', () => this.close());
  }

  /**
   * Open the search modal
   */
  open(): void {
    if (!this.modal || !this.overlay) return;

    this.isOpen = true;
    this.modal.classList.add('is-open');
    this.overlay.classList.add('is-open');
    document.body.style.overflow = 'hidden';

    // Focus input after transition
    requestAnimationFrame(() => {
      this.input?.focus();
    });
  }

  /**
   * Close the search modal
   */
  close(): void {
    if (!this.modal || !this.overlay) return;

    this.isOpen = false;
    this.modal.classList.remove('is-open');
    this.overlay.classList.remove('is-open');
    document.body.style.overflow = '';

    if (this.input) {
      this.input.value = '';
    }
  }
}

export { SearchModal };
