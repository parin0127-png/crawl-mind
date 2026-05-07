# Technical SEO: Infrastructure, Performance, and Crawlability

## 1. Page Speed Optimization
Page speed is a confirmed ranking factor for both desktop and mobile. Fast pages improve crawl efficiency and user experience.
- **Server Response Time (TTFB)**: Time to First Byte should be under 200ms. Utilize CDNs (Content Delivery Networks) and reliable hosting.
- **Resource Minification**: Minify HTML, CSS, and JavaScript files by removing unnecessary characters, spaces, and comments.
- **Caching**: Implement aggressive browser caching and server-side caching (e.g., Redis, Memcached).
- **Render-Blocking Resources**: Defer or asynchronously load non-critical JavaScript and CSS. Keep the critical rendering path as short as possible.
- **Lazy Loading**: Implement native lazy loading (`loading="lazy"`) for images and iframes below the fold.

## 2. Core Web Vitals (CWV)
Core Web Vitals are a specific set of metrics Google uses to measure user experience, focusing on loading, interactivity, and visual stability.
- **Largest Contentful Paint (LCP)**: Measures loading performance.
  - **Threshold**: Must occur within **2.5 seconds** of when the page first starts loading.
  - **Fixes**: Preload hero images, optimize fonts, reduce server response times.
- **Interaction to Next Paint (INP)**: (Replaced FID in 2024). Measures responsiveness.
  - **Threshold**: Should be under **200 milliseconds**.
  - **Fixes**: Break up long JavaScript tasks, optimize third-party scripts, yield to the main thread.
- **Cumulative Layout Shift (CLS)**: Measures visual stability.
  - **Threshold**: Maintain a score of **0.1 or less**.
  - **Fixes**: Always include size attributes (width and height) on images and video elements, never insert content above existing content dynamically.

## 3. Mobile-Friendliness
Google uses Mobile-First Indexing, meaning the mobile version of the website is the baseline for indexing and ranking.
- **Viewport Meta Tag**: Must include `<meta name="viewport" content="width=device-width, initial-scale=1">`.
- **Touch Targets**: Buttons and links must be at least 48x48 pixels and have enough spacing to prevent accidental clicks.
- **Font Size**: Use a base font size of at least 16px to ensure readability on small screens without zooming.
- **Content Parity**: Ensure the mobile site contains the exact same vital content, metadata, and structured data as the desktop site.

## 4. Crawlability and Indexability
If Google can't crawl or index a page, it cannot rank.
- **Crawl Budget**: The number of pages Googlebot crawls and indexes on a site within a given timeframe. Optimize by removing duplicate content, fixing broken links, and blocking low-value URLs.
- **HTTP Status Codes**:
  - **200 (OK)**: Ideal state for indexable pages.
  - **301 (Permanent Redirect)**: Use when permanently moving a page. Passes ~90-99% of link equity.
  - **302 (Temporary Redirect)**: Do not use for permanent changes, as it does not pass link equity efficiently.
  - **404 (Not Found)**: Serve a custom 404 page. Do not redirect all 404s to the homepage (soft 404s are penalized).
  - **410 (Gone)**: Use when a page is permanently deleted and will never return. Speeds up de-indexing.
  - **5xx (Server Errors)**: Monitor closely. Frequent 500 errors will force Googlebot to slow down crawling.

## 5. Robots.txt Rules
The `robots.txt` file sits at the root of the domain and gives instructions to web crawlers.
- **Syntax**: Uses `User-agent`, `Allow`, and `Disallow` directives.
- **Security Check**: Never use `robots.txt` to hide sensitive data; it is publicly visible.
- **Important Directives**: Always include the absolute path to the XML sitemap at the bottom of the file (e.g., `Sitemap: https://www.example.com/sitemap.xml`).
- **Common Mistakes**: Accidentally blocking CSS/JS files (which prevents Google from rendering the page correctly) or accidentally disallowing the entire site (`Disallow: /`).

## 6. Sitemap Structure
XML Sitemaps help search engines intelligently crawl a site.
- **Format**: Must be valid XML.
- **Limits**: Maximum 50,000 URLs per sitemap and maximum uncompressed file size of 50MB. If exceeding this, use a Sitemap Index file.
- **Dynamic Updates**: Ensure the sitemap updates dynamically when new pages are published or deleted.
- **Exclusions**: Do NOT include 404 pages, 301 redirects, or canonicalized (non-primary) pages in the sitemap. Only include 200 OK canonical URLs.

## 7. Canonical Tags
Canonical tags (`rel="canonical"`) solve duplicate content issues by telling Google which version of a URL is the "master" copy.
- **Self-Referencing**: Every page should ideally have a self-referencing canonical tag.
- **Absolute URLs**: Always use absolute URLs (e.g., `https://www.site.com/page/`), never relative (`/page/`).
- **Cross-Domain Canonicals**: Can be used when syndicating content to other websites to ensure the original site gets the SEO credit.
- **Consistency**: Canonical tags must match the internal linking structure and sitemap URLs.

## 8. Structured Data (Schema Markup)
Structured data translates page content into a machine-readable format for search engines, enabling Rich Snippets.
- **Format**: Use **JSON-LD** format (Google's strongly preferred method).
- **Essential Types**:
  - `Organization` / `LocalBusiness`: For the homepage.
  - `Article` / `NewsArticle`: For blog posts.
  - `Product`: For e-commerce pages (essential for showing price, reviews, and availability in SERPs).
  - `FAQPage`: Highly effective for capturing more SERP real estate.
  - `BreadcrumbList`: Enhances URL display in SERPs.
- **Validation**: Always validate markup using the Google Rich Results Test tool.

## 9. HTTPS and Security
Security is a confirmed, albeit lightweight, ranking signal.
- **SSL Certificate**: The entire site must be served over HTTPS.
- **Mixed Content Issues**: Ensure all resources (images, scripts, CSS) are loaded over HTTPS. Loading an HTTP image on an HTTPS page breaks the secure padlock and is flagged by Google.
- **HSTS (HTTP Strict Transport Security)**: Implement HSTS to force browsers to use secure connections.

# Technical SEO: Infrastructure, Performance, and Crawlability

## 1. Page Speed Optimization
Page speed is a confirmed ranking factor for both desktop and mobile. Fast pages improve crawl efficiency and user experience.
- **Server Response Time (TTFB)**: Time to First Byte should be under 200ms. Utilize CDNs (Content Delivery Networks) and reliable hosting.
- **Resource Minification**: Minify HTML, CSS, and JavaScript files by removing unnecessary characters, spaces, and comments.
- **Caching**: Implement aggressive browser caching and server-side caching (e.g., Redis, Memcached).
- **Render-Blocking Resources**: Defer or asynchronously load non-critical JavaScript and CSS. Keep the critical rendering path as short as possible.
- **Lazy Loading**: Implement native lazy loading (`loading="lazy"`) for images and iframes below the fold.

## 2. Core Web Vitals (CWV)
Core Web Vitals are a specific set of metrics Google uses to measure user experience, focusing on loading, interactivity, and visual stability.
- **Largest Contentful Paint (LCP)**: Measures loading performance.
  - **Threshold**: Must occur within **2.5 seconds** of when the page first starts loading.
  - **Fixes**: Preload hero images, optimize fonts, reduce server response times.
- **Interaction to Next Paint (INP)**: (Replaced FID in 2024). Measures responsiveness.
  - **Threshold**: Should be under **200 milliseconds**.
  - **Fixes**: Break up long JavaScript tasks, optimize third-party scripts, yield to the main thread.
- **Cumulative Layout Shift (CLS)**: Measures visual stability.
  - **Threshold**: Maintain a score of **0.1 or less**.
  - **Fixes**: Always include size attributes (width and height) on images and video elements, never insert content above existing content dynamically.

## 3. Mobile-Friendliness
Google uses Mobile-First Indexing, meaning the mobile version of the website is the baseline for indexing and ranking.
- **Viewport Meta Tag**: Must include `<meta name="viewport" content="width=device-width, initial-scale=1">`.
- **Touch Targets**: Buttons and links must be at least 48x48 pixels and have enough spacing to prevent accidental clicks.
- **Font Size**: Use a base font size of at least 16px to ensure readability on small screens without zooming.
- **Content Parity**: Ensure the mobile site contains the exact same vital content, metadata, and structured data as the desktop site.

## 4. Crawlability and Indexability
If Google can't crawl or index a page, it cannot rank.
- **Crawl Budget**: The number of pages Googlebot crawls and indexes on a site within a given timeframe. Optimize by removing duplicate content, fixing broken links, and blocking low-value URLs.
- **HTTP Status Codes**:
  - **200 (OK)**: Ideal state for indexable pages.
  - **301 (Permanent Redirect)**: Use when permanently moving a page. Passes ~90-99% of link equity.
  - **302 (Temporary Redirect)**: Do not use for permanent changes, as it does not pass link equity efficiently.
  - **404 (Not Found)**: Serve a custom 404 page. Do not redirect all 404s to the homepage (soft 404s are penalized).
  - **410 (Gone)**: Use when a page is permanently deleted and will never return. Speeds up de-indexing.
  - **5xx (Server Errors)**: Monitor closely. Frequent 500 errors will force Googlebot to slow down crawling.

## 5. Robots.txt Rules
The `robots.txt` file sits at the root of the domain and gives instructions to web crawlers.
- **Syntax**: Uses `User-agent`, `Allow`, and `Disallow` directives.
- **Security Check**: Never use `robots.txt` to hide sensitive data; it is publicly visible.
- **Important Directives**: Always include the absolute path to the XML sitemap at the bottom of the file (e.g., `Sitemap: https://www.example.com/sitemap.xml`).
- **Common Mistakes**: Accidentally blocking CSS/JS files (which prevents Google from rendering the page correctly) or accidentally disallowing the entire site (`Disallow: /`).

## 6. Sitemap Structure
XML Sitemaps help search engines intelligently crawl a site.
- **Format**: Must be valid XML.
- **Limits**: Maximum 50,000 URLs per sitemap and maximum uncompressed file size of 50MB. If exceeding this, use a Sitemap Index file.
- **Dynamic Updates**: Ensure the sitemap updates dynamically when new pages are published or deleted.
- **Exclusions**: Do NOT include 404 pages, 301 redirects, or canonicalized (non-primary) pages in the sitemap. Only include 200 OK canonical URLs.

## 7. Canonical Tags
Canonical tags (`rel="canonical"`) solve duplicate content issues by telling Google which version of a URL is the "master" copy.
- **Self-Referencing**: Every page should ideally have a self-referencing canonical tag.
- **Absolute URLs**: Always use absolute URLs (e.g., `https://www.site.com/page/`), never relative (`/page/`).
- **Cross-Domain Canonicals**: Can be used when syndicating content to other websites to ensure the original site gets the SEO credit.
- **Consistency**: Canonical tags must match the internal linking structure and sitemap URLs.

## 8. Structured Data (Schema Markup)
Structured data translates page content into a machine-readable format for search engines, enabling Rich Snippets.
- **Format**: Use **JSON-LD** format (Google's strongly preferred method).
- **Essential Types**:
  - `Organization` / `LocalBusiness`: For the homepage.
  - `Article` / `NewsArticle`: For blog posts.
  - `Product`: For e-commerce pages (essential for showing price, reviews, and availability in SERPs).
  - `FAQPage`: Highly effective for capturing more SERP real estate.
  - `BreadcrumbList`: Enhances URL display in SERPs.
- **Validation**: Always validate markup using the Google Rich Results Test tool.

## 9. HTTPS and Security
Security is a confirmed, albeit lightweight, ranking signal.
- **SSL Certificate**: The entire site must be served over HTTPS.
- **Mixed Content Issues**: Ensure all resources (images, scripts, CSS) are loaded over HTTPS. Loading an HTTP image on an HTTPS page breaks the secure padlock and is flagged by Google.
- **HSTS (HTTP Strict Transport Security)**: Implement HSTS to force browsers to use secure connections.

# Technical SEO: Infrastructure, Performance, and Crawlability

## 1. Page Speed Optimization
Page speed is a confirmed ranking factor for both desktop and mobile. Fast pages improve crawl efficiency and user experience.
- **Server Response Time (TTFB)**: Time to First Byte should be under 200ms. Utilize CDNs (Content Delivery Networks) and reliable hosting.
- **Resource Minification**: Minify HTML, CSS, and JavaScript files by removing unnecessary characters, spaces, and comments.
- **Caching**: Implement aggressive browser caching and server-side caching (e.g., Redis, Memcached).
- **Render-Blocking Resources**: Defer or asynchronously load non-critical JavaScript and CSS. Keep the critical rendering path as short as possible.
- **Lazy Loading**: Implement native lazy loading (`loading="lazy"`) for images and iframes below the fold.

## 2. Core Web Vitals (CWV)
Core Web Vitals are a specific set of metrics Google uses to measure user experience, focusing on loading, interactivity, and visual stability.
- **Largest Contentful Paint (LCP)**: Measures loading performance.
  - **Threshold**: Must occur within **2.5 seconds** of when the page first starts loading.
  - **Fixes**: Preload hero images, optimize fonts, reduce server response times.
- **Interaction to Next Paint (INP)**: (Replaced FID in 2024). Measures responsiveness.
  - **Threshold**: Should be under **200 milliseconds**.
  - **Fixes**: Break up long JavaScript tasks, optimize third-party scripts, yield to the main thread.
- **Cumulative Layout Shift (CLS)**: Measures visual stability.
  - **Threshold**: Maintain a score of **0.1 or less**.
  - **Fixes**: Always include size attributes (width and height) on images and video elements, never insert content above existing content dynamically.

## 3. Mobile-Friendliness
Google uses Mobile-First Indexing, meaning the mobile version of the website is the baseline for indexing and ranking.
- **Viewport Meta Tag**: Must include `<meta name="viewport" content="width=device-width, initial-scale=1">`.
- **Touch Targets**: Buttons and links must be at least 48x48 pixels and have enough spacing to prevent accidental clicks.
- **Font Size**: Use a base font size of at least 16px to ensure readability on small screens without zooming.
- **Content Parity**: Ensure the mobile site contains the exact same vital content, metadata, and structured data as the desktop site.

## 4. Crawlability and Indexability
If Google can't crawl or index a page, it cannot rank.
- **Crawl Budget**: The number of pages Googlebot crawls and indexes on a site within a given timeframe. Optimize by removing duplicate content, fixing broken links, and blocking low-value URLs.
- **HTTP Status Codes**:
  - **200 (OK)**: Ideal state for indexable pages.
  - **301 (Permanent Redirect)**: Use when permanently moving a page. Passes ~90-99% of link equity.
  - **302 (Temporary Redirect)**: Do not use for permanent changes, as it does not pass link equity efficiently.
  - **404 (Not Found)**: Serve a custom 404 page. Do not redirect all 404s to the homepage (soft 404s are penalized).
  - **410 (Gone)**: Use when a page is permanently deleted and will never return. Speeds up de-indexing.
  - **5xx (Server Errors)**: Monitor closely. Frequent 500 errors will force Googlebot to slow down crawling.

## 5. Robots.txt Rules
The `robots.txt` file sits at the root of the domain and gives instructions to web crawlers.
- **Syntax**: Uses `User-agent`, `Allow`, and `Disallow` directives.
- **Security Check**: Never use `robots.txt` to hide sensitive data; it is publicly visible.
- **Important Directives**: Always include the absolute path to the XML sitemap at the bottom of the file (e.g., `Sitemap: https://www.example.com/sitemap.xml`).
- **Common Mistakes**: Accidentally blocking CSS/JS files (which prevents Google from rendering the page correctly) or accidentally disallowing the entire site (`Disallow: /`).

## 6. Sitemap Structure
XML Sitemaps help search engines intelligently crawl a site.
- **Format**: Must be valid XML.
- **Limits**: Maximum 50,000 URLs per sitemap and maximum uncompressed file size of 50MB. If exceeding this, use a Sitemap Index file.
- **Dynamic Updates**: Ensure the sitemap updates dynamically when new pages are published or deleted.
- **Exclusions**: Do NOT include 404 pages, 301 redirects, or canonicalized (non-primary) pages in the sitemap. Only include 200 OK canonical URLs.

## 7. Canonical Tags
Canonical tags (`rel="canonical"`) solve duplicate content issues by telling Google which version of a URL is the "master" copy.
- **Self-Referencing**: Every page should ideally have a self-referencing canonical tag.
- **Absolute URLs**: Always use absolute URLs (e.g., `https://www.site.com/page/`), never relative (`/page/`).
- **Cross-Domain Canonicals**: Can be used when syndicating content to other websites to ensure the original site gets the SEO credit.
- **Consistency**: Canonical tags must match the internal linking structure and sitemap URLs.

## 8. Structured Data (Schema Markup)
Structured data translates page content into a machine-readable format for search engines, enabling Rich Snippets.
- **Format**: Use **JSON-LD** format (Google's strongly preferred method).
- **Essential Types**:
  - `Organization` / `LocalBusiness`: For the homepage.
  - `Article` / `NewsArticle`: For blog posts.
  - `Product`: For e-commerce pages (essential for showing price, reviews, and availability in SERPs).
  - `FAQPage`: Highly effective for capturing more SERP real estate.
  - `BreadcrumbList`: Enhances URL display in SERPs.
- **Validation**: Always validate markup using the Google Rich Results Test tool.

## 9. HTTPS and Security
Security is a confirmed, albeit lightweight, ranking signal.
- **SSL Certificate**: The entire site must be served over HTTPS.
- **Mixed Content Issues**: Ensure all resources (images, scripts, CSS) are loaded over HTTPS. Loading an HTTP image on an HTTPS page breaks the secure padlock and is flagged by Google.
- **HSTS (HTTP Strict Transport Security)**: Implement HSTS to force browsers to use secure connections.

