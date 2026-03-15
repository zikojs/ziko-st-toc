import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "ziko-st-toc",
  description: "Streamlit Table of Contents generator",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Get started', link: '/intro/get-started' }
    ],

    sidebar: [
      {
        text : 'Introduction',
        base : '/intro/',
        items : [
          { text: "Get started", link: "get-started" },
          { text: "Supports", link: "supports" },
        ]
      },
      {
        text: 'Examples',
        items: [
          { text: 'Markdown Examples', link: '/markdown-examples' },
          { text: 'Runtime API Examples', link: '/api-examples' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/zikojs/ziko-st-toc' }
    ]
  }
})
