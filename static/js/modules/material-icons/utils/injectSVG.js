/**
 * @license
 * Copyright (c) 2021. CRON LLC. All rights reserved.
 * The copyright notice above does not evidence any actual or
 * intended publication of such source code. The code contains
 * CRON LLC Confidential Proprietary Information.
 */

// Injecting SVG Sprites into DOM
// https://css-tricks.com/ajaxing-svg-sprite/
function injectSVG(...path) {
  document.addEventListener('DOMContentLoaded', path.map(spriteUrl => {
      fetch(spriteUrl)
        .then(response => {
          if (!response.ok) {
            throw new Error()
          } else {
            return response.text()
          }
        })
        .then(text => {
          const div = document.createElement('div');
          div.innerHTML = text;
          div.style.position = 'absolute';
          div.style.top = '-9999px';
          div.style.left = '-9999px';
          document.body.insertAdjacentElement('afterbegin', div);
        });
    }),
  );
}

export default injectSVG;
