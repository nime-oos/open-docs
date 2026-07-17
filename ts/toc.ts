/**
 * Frappe HR Documentation - Table of Contents Component
 * Auto-generates "On this page" sidebar from content headings with scroll spy
 */

interface TocHeading {
  id: string;
  text: string;
  level: number;
}

class TableOfContents {
  private headings: TocHeading[] = [];
  private observer: IntersectionObserver | null = null;
  private activeId: string = '';
  private tocContainer: HTMLElement | null = null;
  private visibleHeadings: Set<string> = new Set();

  constructor() {
    this.tocContainer = document.getElementById('wiki-toc-list');
  }

  /**
   * Initialize - scan headings, build TOC, setup scroll spy
   */
  init(): void {
    this.scanHeadings();
    this.renderToc();
    this.initScrollSpy();
    this.attachClickListeners();
  }

  /**
   * Scan the content area for H2, H3, H4 headings
   */
  private scanHeadings(): void {
    const content = document.getElementById('wiki-content');
    if (!content) return;

    const headingElements = content.querySelectorAll('h2, h3, h4');
    this.headings = [];

    headingElements.forEach((el) => {
      const heading = el as HTMLHeadingElement;
      if (heading.id) {
        this.headings.push({
          id: heading.id,
          text: heading.textContent?.trim() || '',
          level: parseInt(heading.tagName.substring(1), 10),
        });
      }
    });
  }

  /**
   * Render the table of contents HTML
   */
  private renderToc(): void {
    if (!this.tocContainer || this.headings.length === 0) return;

    const html = this.headings
      .map((heading) => {
        const levelClass = `toc-h${heading.level}`;
        const paddingLeft = (heading.level - 2) * 0.75;
        return `<li>
          <a href="#${heading.id}"
             data-toc-link="${heading.id}"
             class="toc-link ${levelClass}"
             style="padding-left: ${paddingLeft}rem">
            ${this.escapeHtml(heading.text)}
          </a>
        </li>`;
      })
      .join('\n');

    this.tocContainer.innerHTML = html;
  }

  /**
   * Setup IntersectionObserver for scroll spy
   */
  private initScrollSpy(): void {
    if (this.observer) {
      this.observer.disconnect();
    }

    this.visibleHeadings.clear();

    const headingElements = this.headings
      .map((h) => document.getElementById(h.id))
      .filter((el): el is HTMLElement => el !== null);

    if (headingElements.length === 0) return;

    this.observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          const id = entry.target.id;
          if (entry.isIntersecting) {
            this.visibleHeadings.add(id);
          } else {
            this.visibleHeadings.delete(id);
          }
        });

        this.updateActiveHeading();
      },
      {
        rootMargin: '-80px 0px -60% 0px',
        threshold: 0,
      }
    );

    headingElements.forEach((el) => {
      this.observer!.observe(el);
    });
  }

  /**
   * Update the active heading in the TOC based on visible headings
   */
  private updateActiveHeading(): void {
    let newActiveId = '';

    if (this.visibleHeadings.size > 0) {
      // Pick the first visible heading in document order
      for (const heading of this.headings) {
        if (this.visibleHeadings.has(heading.id)) {
          newActiveId = heading.id;
          break;
        }
      }
    }

    if (newActiveId !== this.activeId) {
      // Remove old active
      if (this.activeId) {
        const oldLink = document.querySelector(
          `[data-toc-link="${this.activeId}"]`
        );
        oldLink?.classList.remove('active');
      }

      // Set new active
      if (newActiveId) {
        const newLink = document.querySelector(
          `[data-toc-link="${newActiveId}"]`
        );
        newLink?.classList.add('active');
      }

      this.activeId = newActiveId;
    }
  }

  /**
   * Attach click listeners for smooth scrolling
   */
  private attachClickListeners(): void {
    if (!this.tocContainer) return;

    this.tocContainer.addEventListener('click', (e) => {
      const target = e.target as HTMLElement;
      const link = target.closest('.toc-link') as HTMLAnchorElement;
      if (!link) return;

      e.preventDefault();
      const id = link.getAttribute('data-toc-link');
      if (!id) return;

      const heading = document.getElementById(id);
      if (heading) {
        const offset = 80; // Account for sticky header
        const top = heading.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  }

  /**
   * Escape HTML entities in text
   */
  private escapeHtml(text: string): string {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  /**
   * Cleanup - disconnect observer
   */
  destroy(): void {
    if (this.observer) {
      this.observer.disconnect();
      this.observer = null;
    }
  }
}

export { TableOfContents };
