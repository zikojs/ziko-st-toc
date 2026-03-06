import { Streamlit } from "streamlit-component-lib"
import { TableOfContents } from 'zextra/nav'

const ROOT = document.getElementById('root')

function onRender(event){
  const data = event.detail;
  const {theme, args} = data
  const {style, usehash} = args 
  ROOT.innerHTML = ''
  const {backgroundColor, primaryColor} = theme
  const toc = TableOfContents({content : parent.document.body}).style({
    backgroundColor,
    border : `2px solid ${primaryColor}`,
    ...style
  }).mount(ROOT);
  const links = toc.toc_list.element.querySelectorAll('a')

    links.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();

      const href = link.getAttribute('href');
      const id = href.replace('#', '');

      try {
        const el = parent.document.getElementById(id);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth' });
          if(usehash) parent.history.replaceState(null, "", `#${id}`);
        }
      } catch (err) {
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


