const fs = require('fs');
const path = require('path');

const SITE_TITLE = 'Frappe HR';

// The full sidebar structure
const sidebarData = [
  {
    id: 'intro',
    title: 'Introduction',
    color: 'orange',
    children: [
      { id: 'introduction', title: 'Frappe HR', route: 'introduction.html' },
      { id: 'videos', title: 'Videos', route: 'videos.html' }
    ]
  },
  {
    id: 'mobile',
    title: 'Frappe HR Mobile',
    color: 'orange',
    children: [
      { id: 'mobile-app-installation', title: 'Mobile App Installation', route: 'mobile-app-installation.html' },
      { id: 'push-notification', title: 'Push Notification', route: 'push-notification.html' }
    ]
  },
  {
    id: 'org',
    title: 'Organization Management',
    color: 'orange',
    children: [
      { id: 'employee', title: 'Employee', route: 'employee.html' },
      { id: 'employment-type', title: 'Employment Type', route: 'employment-type.html' },
      { id: 'branch', title: 'Branch', route: 'branch.html' },
      { id: 'department', title: 'Department', route: 'department.html' },
      { id: 'designation', title: 'Designation', route: 'designation.html' },
      { id: 'employee-grade', title: 'Employee Grade', route: 'employee-grade.html' },
      { id: 'employee-group', title: 'Employee Group', route: 'employee-group.html' },
      { id: 'employee-health-insurance', title: 'Employee Health Insurance', route: 'employee-health-insurance.html' },
      { id: 'organizational-chart', title: 'Organizational Chart', route: 'organizational-chart.html' }
    ]
  },
  {
    id: 'attendance',
    title: 'Attendance',
    color: 'orange',
    children: [
      { id: 'attendance-page', title: 'Attendance', route: 'attendance.html' },
      { id: 'employee-attendance-tool', title: 'Employee Attendance Tool', route: 'employee-attendance-tool.html' },
      { id: 'attendance-request', title: 'Attendance Request', route: 'attendance-request.html' },
      { id: 'upload-attendance', title: 'Upload Attendance', route: 'upload-attendance.html' },
      { id: 'employee-checkin', title: 'Employee Checkin', route: 'employee-checkin.html' },
      { id: 'auto-attendance', title: 'Auto Attendance', route: 'auto-attendance.html' },
      { id: 'integrating-bio', title: 'Integrating Frappe HR With Biometric Attendance Devices', route: 'integrating-frappe-hr-with-bio.html' }
    ]
  },
  {
    id: 'shift',
    title: 'Shift Management',
    color: 'orange',
    children: [
      { id: 'shift-management', title: 'Shift Management', route: 'shift-management.html' },
      { id: 'shift-type', title: 'Shift Type', route: 'shift-type.html' },
      { id: 'shift-location', title: 'Shift Location', route: 'shift-location.html' },
      { id: 'shift-request', title: 'Shift Request', route: 'shift-request.html' },
      { id: 'shift-assignment', title: 'Shift Assignment', route: 'shift-assignment.html' }
    ]
  }
];

// Flatten the pages for easy next/prev linking
const pages = [];
sidebarData.forEach(group => {
  group.children.forEach(child => {
    pages.push(child);
  });
});

// Specific page contents
const pageContents = {
  'introduction.html': {
    title: 'Frappe HR',
    content: `
      <p>Frappe HR is an open Source, modern, and easy-to-use HR and Payroll Software for all organizations. It has everything you need to drive excellence within the company. It is a complete HRMS solution with over 13 different modules right from Employee Management, Onboarding, Leaves, to Payroll, Taxation, and more!</p>
      <img src="assets/images/placeholder.png" alt="Employee Profile Screenshot" />
      
      <h2 id="why-frappe-hr">Why Frappe HR</h2>
      <p>Businesses often struggle with scattered HR processes, manual payroll calculations, disconnected employee records, and time-consuming approvals.</p>
      <ul>
        <li>Frappe HR brings everything under one roof so HR teams can focus on people, not paperwork.</li>
        <li>Built for organizations that need a flexible and cost-effective solution, Frappe HR eliminates inefficiencies, ensures compliance, and gives employees a seamless experience.</li>
        <li>Whether you are managing a handful of employees or scaling to thousands, it helps you stay organized without getting bogged down in administrative overhead.</li>
      </ul>
      
      <h2 id="key-features">Key Features</h2>
      <ul>
        <li><strong>Employee Lifecycle</strong>: From onboarding employees, managing promotions and transfers, all the way to documenting feedback with exit interviews, make life easier for employees throughout their life cycle.</li>
        <li><strong>Leave and Attendance</strong>: Configure leave policies, pull regional holidays with a click, check-in and check-out with geolocation capturing, track leave balances and attendance with reports.</li>
        <li><strong>Expense Claims and Advances</strong>: Manage employee advances, claim expenses, configure multi-level approval workflows, all this with seamless integration with ERPNext accounting.</li>
        <li><strong>Performance Management</strong>: Track goals, align goals with key result areas (KRAs), enable employees to evaluate themselves, make managing appraisal cycles easy.</li>
        <li><strong>Payroll & Taxation</strong>: Create salary structures, configure income tax slabs, run standard payroll, accomodate additional salaries and off cycle payments, view income breakup on salary slips and so much more.</li>
        <li><strong>Frappe HR Mobile App</strong>: Apply for and approve leaves on the go, check-in and check-out, access employee profile right from the mobile app.</li>
      </ul>
      <p>And more.</p>
      
      <h2 id="under-the-hood">Under the Hood</h2>
      <ul>
        <li><strong><a href="#">Frappe Framework</a></strong>: A full-stack web application framework written in Python and Javascript. The framework provides a robust foundation for building web applications, including a database abstraction layer, user authentication, and a REST API.</li>
        <li><strong><a href="#">Frappe UI</a></strong>: A Vue-based UI library, to provide a modern user interface. The Frappe UI library provides a variety of components that can be used to build single-page applications on top of the Frappe Framework.</li>
      </ul>
      
      <h2 id="installation">Installation</h2>
      <p>To install/setup the app, follow the <a href="#">guidelines here</a>.</p>
      
      <h3 id="learning-and-community">Learning and Community</h3>
      <ol>
        <li><a href="#">Frappe School</a> - Learn Frappe Framework and ERPNext from the various courses by the maintainers or from the community.</li>
        <li><a href="#">Documentation</a> - Extensive documentation for Frappe HR.</li>
        <li><a href="#">User Forum</a> - Engage with the community of ERPNext users and service providers.</li>
        <li><a href="#">Telegram Group</a> - Get instant help from the community of users.</li>
      </ol>
    `
  },
  'videos.html': {
    title: 'Videos',
    content: `
      <p>The Human Resources (HR) module covers the processes related to the HR department of a company. It maintains a complete employee database including contact information, salary details, attendance, performance evaluation, leaves, and appraisal records.</p>
      
      <h2 id="talks-and-webinars">Talks & Webinars</h2>
      
      <h3 id="introducing-frappe-hr">Introducing Frappe HR</h3>
      <div style="background:#111; color:white; padding:40px; border-radius:8px; text-align:center; aspect-ratio:16/9; display:flex; align-items:center; justify-content:center; flex-direction:column;">
         <h4>Introducing Frappe HR - Rucha Mahabal, Reema Mehta</h4>
         <p>EC22 Watch on YouTube</p>
      </div>
      <p><strong>Duration: 14:24</strong><br>Introducing Frappe HR at the ERPNext conference 2022</p>

      <h3 id="simplify-hr-payroll">Simplify your HR and Payroll operations with Frappe HR</h3>
      <div style="background:#111; color:white; padding:40px; border-radius:8px; text-align:center; aspect-ratio:16/9; display:flex; align-items:center; justify-content:center; flex-direction:column;">
         <h4>Simplify your HR and Payroll operations</h4>
      </div>
      <p><strong>Duration: 43:27</strong><br>Overview of latest updates</p>
    `
  },
  'mobile-app-installation.html': {
    title: 'Mobile App Installation',
    content: `
      <p>The Frappe HR mobile app is a Progressive Web App (PWA) available in v15+. No APK or IPA download is needed — it is installed directly through your mobile browser.</p>
      
      <h2 id="step-1">Step 1 — Access your site</h2>
      <p>Open your mobile browser (Chrome on Android, Safari on iOS) and navigate to your site URL.</p>
      
      <h2 id="step-2">Step 2 — Install the App</h2>
      <h3 id="android">Android (Chrome)</h3>
      <p>The browser may auto-prompt you to install the app. If not, tap the three-dot menu and select "Add to Home Screen" or "Install app".</p>
      <img src="assets/images/placeholder.png" alt="Android Install" />
      
      <h3 id="ios">iOS (Safari)</h3>
      <p>Tap the Share button and scroll down to "Add to Home Screen".</p>
      <img src="assets/images/placeholder.png" alt="iOS Install" />
    `
  },
  'push-notification.html': {
    title: 'Push Notification',
    content: `
      <p>Available from v15 onwards, primarily for Frappe Cloud hosted sites.</p>
      
      <h2 id="enable-push">Steps to Enable Push Notifications</h2>
      
      <h3 id="site-settings">Step 1: Configure Site Settings</h3>
      <ul>
        <li>Navigate to <strong>Integrations > Push Notification Settings</strong></li>
        <li>Check <strong>"Enable Push Notification Relay"</strong></li>
      </ul>
      
      <h3 id="app-settings">Step 2: Configure Mobile App Settings</h3>
      <ul>
        <li>Open Frappe HR mobile app</li>
        <li>Go to <strong>Profile > Settings</strong></li>
        <li>Click <strong>"Enable Push Notifications"</strong></li>
      </ul>
    `
  }
};

// Generate HTML function
function generateHTML(pageDef, index) {
  const route = pageDef.route;
  const title = pageDef.title;
  const pageId = route.replace('.html', '');
  
  // Use specific content if available, else placeholder
  const contentHTML = pageContents[route] ? pageContents[route].content : `
    <p>This is placeholder content for the <strong>${title}</strong> page.</p>
    <h2 id="section-1">Section 1</h2>
    <p>Details about ${title} go here.</p>
    <h3 id="sub-section">Sub-section</h3>
    <p>More details.</p>
  `;

  // Prev/Next Nav
  const prevPage = index > 0 ? pages[index - 1] : null;
  const nextPage = index < pages.length - 1 ? pages[index + 1] : null;
  
  let prevNavHTML = '';
  if (prevPage) {
    prevNavHTML = \`
      <a href="\${prevPage.route}" class="page-nav-link prev">
        <svg class="page-nav-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
        <div class="page-nav-text">
          <span class="page-nav-label">Previous Page</span>
          <span class="page-nav-title">\${prevPage.title}</span>
        </div>
      </a>
    \`;
  }
  
  let nextNavHTML = '';
  if (nextPage) {
    nextNavHTML = \`
      <a href="\${nextPage.route}" class="page-nav-link next">
        <div class="page-nav-text">
          <span class="page-nav-label">Next Page</span>
          <span class="page-nav-title">\${nextPage.title}</span>
        </div>
        <svg class="page-nav-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
      </a>
    \`;
  }

  // Sidebar Generation
  let sidebarHTML = '';
  sidebarData.forEach(group => {
    sidebarHTML += \`
      <div class="sidebar-group">
        <button class="sidebar-group-btn" data-group-id="\${group.id}" aria-expanded="true">
          <svg class="sidebar-arrow expanded" viewBox="0 0 12 12" fill="currentColor"><path d="M4 8.54V3.46c0-.4.455-.64.787-.41l3.628 2.54a.5.5 0 010 .82L4.787 8.95A.5.5 0 014 8.54z"/></svg>
          <span class="sidebar-group-title">\${group.title}</span>
        </button>
        <div class="sidebar-children" id="\${group.id}-children" style="display: block;">
          <div class="sidebar-list">
    \`;
    
    group.children.forEach(child => {
      const isActive = child.route === route ? 'active' : '';
      const ariaCurrent = child.route === route ? 'aria-current="page"' : '';
      sidebarHTML += \`
        <div class="sidebar-item">
          <a href="\${child.route}" class="sidebar-link \${isActive}" data-route="\${child.route.replace('.html', '')}" \${ariaCurrent}>
            <span class="sidebar-link-title">\${child.title}</span>
          </a>
        </div>
      \`;
    });
    
    sidebarHTML += \`
          </div>
        </div>
      </div>
    \`;
  });

  const html = \`<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>\${title} - \${SITE_TITLE}</title>
    <meta name="description" content="\${title} documentation for Frappe HR">
    
    <!-- CSS -->
    <link rel="stylesheet" href="css/variables.css">
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/typography.css">
    <link rel="stylesheet" href="css/layout.css">
    <link rel="stylesheet" href="css/sidebar.css">
    <link rel="stylesheet" href="css/content.css">
    <link rel="stylesheet" href="css/toc.css">
    <link rel="stylesheet" href="css/navigation.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/responsive.css">
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="site-container">
        <!-- Header -->
        <header class="site-header">
            <div class="header-left">
                <div class="header-logo-icon">
                    <svg viewBox="0 0 24 24"><path d="M5 4h14v2H5V4zm0 5h14v2H5V9zm0 5h9v2H5v-2z"/></svg>
                </div>
                <span class="header-space-name">Frappe HR</span>
                <svg class="header-chevron" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
            </div>
            
            <nav class="header-nav">
                <a href="#" class="header-nav-link">Learn</a>
                <a href="#" class="header-nav-link">Discuss</a>
                <a href="#" class="header-nav-link">Website</a>
            </nav>
            
            <div class="header-actions">
                <button class="search-btn" id="search-btn">
                    <svg class="search-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                    <span class="search-kbd" id="search-shortcut">Ctrl+K</span>
                </button>
                <div class="header-divider"></div>
                <button class="theme-toggle" id="theme-toggle" aria-label="Toggle theme">
                    <div class="theme-knob">
                        <svg id="theme-sun" class="theme-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                        <svg id="theme-moon" class="theme-icon" style="display:none" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
                    </div>
                </button>
                <div class="header-divider"></div>
                <a href="#" class="github-link">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
                </a>
            </div>
        </header>
        
        <!-- Mobile Header (Hidden on Desktop) -->
        <header class="mobile-header">
            <div class="header-left">
                <button class="mobile-menu-btn" id="mobile-menu-btn">
                    <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
                </button>
                <span class="header-space-name">Frappe HR</span>
            </div>
            <button class="search-btn">
                <svg class="search-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
            </button>
        </header>

        <!-- Main Body -->
        <div class="site-body">
            
            <!-- Left Sidebar -->
            <aside class="wiki-sidebar" id="mobile-sidebar">
                <nav class="sidebar-nav">
                    \${sidebarHTML}
                </nav>
            </aside>
            <div class="mobile-sidebar-overlay" id="mobile-overlay"></div>

            <!-- Main Content -->
            <main class="wiki-main">
                <article class="wiki-article">
                    
                    <div class="page-header">
                        <h1 class="page-title" id="page-title">\${title}</h1>
                        <div class="edit-btn-group">
                            <a href="#" class="edit-btn">
                                <svg class="edit-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2"><path d="M17 3a2.85 2.83 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5Z"></path><path d="m15 5 4 4"></path></svg>
                                Edit
                            </a>
                            <button class="edit-dropdown-btn">
                                <svg class="edit-dropdown-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"></path></svg>
                            </button>
                        </div>
                    </div>

                    <div class="wiki-content prose prose-sm max-w-none scroll-smooth" id="wiki-content">
                        \${contentHTML}
                    </div>

                    <!-- Previous/Next Navigation -->
                    <nav class="page-nav">
                        <div class="page-nav-links">
                            \${prevNavHTML}
                            \${nextNavHTML}
                        </div>
                    </nav>
                    
                    <div class="page-meta">
                        <div class="last-updated">Last updated just now</div>
                        <div class="feedback-widget">
                            <span class="feedback-prompt">Was this helpful?</span>
                            <div class="feedback-options">
                                <button class="feedback-btn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M16 16s-1.5-2-4-2-4 2-4 2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg></button>
                                <button class="feedback-btn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="8" y1="15" x2="16" y2="15"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg></button>
                                <button class="feedback-btn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg></button>
                            </div>
                        </div>
                    </div>

                </article>
            </main>

            <!-- Right Sidebar TOC -->
            <aside class="wiki-toc">
                <nav class="toc-sidebar">
                    <h3 class="toc-title">On this page</h3>
                    <ul class="toc-list" id="wiki-toc-list">
                        <!-- Populated by JavaScript -->
                    </ul>
                </nav>
            </aside>

        </div>
    </div>

    <!-- Search Modal -->
    <div class="search-modal-overlay" id="search-overlay">
        <div class="search-modal" id="search-modal">
            <div class="search-header">
                <svg class="search-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                <input type="text" class="search-input" id="search-input" placeholder="Search documentation...">
                <button class="search-close" id="search-close">
                    <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                </button>
            </div>
            <div class="search-results-empty">
                No recent searches
            </div>
        </div>
    </div>

    <!-- Application Logic -->
    <script src="js/app.js"></script>
</body>
</html>\`;

  fs.writeFileSync(path.join(__dirname, route), html, 'utf8');
  console.log(\`Generated \${route}\`);
}

// Ensure directories exist for assets
const assetsDir = path.join(__dirname, 'assets', 'images');
fs.mkdirSync(assetsDir, { recursive: true });

// Create a dummy placeholder image
const placeholderSVG = \`<svg width="800" height="400" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#eee"/>
  <text x="50%" y="50%" font-family="sans-serif" font-size="24" fill="#999" text-anchor="middle" dominant-baseline="middle">Placeholder Image</text>
</svg>\`;
fs.writeFileSync(path.join(assetsDir, 'placeholder.png'), placeholderSVG);

// Generate all pages
pages.forEach((page, index) => generateHTML(page, index));
console.log('Done!');
