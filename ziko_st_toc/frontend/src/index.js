import { Streamlit } from "streamlit-component-lib"
import { TableOfContents } from 'zextra/nav'


function onRender(){
  document.body.innerHTML = ''
  const toc = TableOfContents({content : parent.document.body}).mount(document.body);
  const links = toc.toc_list.element.querySelectorAll('a')

    links.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();

      const href = link.getAttribute('href'); // e.g. "#heading-3"
      const id = href.replace('#', '');

      try {
        // Try scrolling parent directly (works in production build)
        const el = parent.document.getElementById(id);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth' });
        }
      } catch (err) {
        // Cross-origin (dev mode) → use postMessage
        window.parent.postMessage({ type: 'toc-scroll', id }, '*');
      }

      // Optional: notify Streamlit about the last clicked heading
      Streamlit.setComponentValue({ last_clicked_id: id });
    });
  });

  Streamlit.setFrameHeight()
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.setComponentReady()
Streamlit.setFrameHeight()


