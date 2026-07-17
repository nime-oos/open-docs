/**
 * Frappe HR Documentation - Utility Functions
 * Shared helpers used across components
 */

/**
 * Debounce a function call
 */
function debounce<T extends (...args: unknown[]) => void>(
  func: T,
  wait: number
): (...args: Parameters<T>) => void {
  let timeout: ReturnType<typeof setTimeout>;
  return (...args: Parameters<T>) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => func(...args), wait);
  };
}

/**
 * Throttle a function call
 */
function throttle<T extends (...args: unknown[]) => void>(
  func: T,
  limit: number
): (...args: Parameters<T>) => void {
  let inThrottle = false;
  return (...args: Parameters<T>) => {
    if (!inThrottle) {
      func(...args);
      inThrottle = true;
      setTimeout(() => (inThrottle = false), limit);
    }
  };
}

/**
 * Check if the current platform is Mac
 */
function isMac(): boolean {
  return navigator.platform.toUpperCase().indexOf('MAC') >= 0;
}

/**
 * Get the keyboard shortcut display string
 */
function getSearchShortcut(): string {
  return isMac() ? '⌘K' : 'Ctrl+K';
}

export { debounce, throttle, isMac, getSearchShortcut };
